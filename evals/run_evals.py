#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Runner ewaluacji skilla humanizer-pl.

Czyta evals.json i sprawdza asercje na ZAMROZONEJ parze (input, output) kazdego
case'a. Bez sieci, bez wywolan LLM, bez zapisow na dysk, wylacznie biblioteka
standardowa. Sciezki liczone wzgledem tego pliku. Kod wyjscia 0 tylko wtedy, gdy
wynik kazdej asercji zgadza sie z mapa `expect` case'a (brak wpisu = oczekiwany
sukces), 1 przy niezgodnosci, 2 przy bledzie samego evals.json.

Uzycie:
    python3 evals/run_evals.py
    python3 evals/run_evals.py --case notatka     # filtr po fragmencie nazwy
    python3 evals/run_evals.py --quiet            # tylko bledy i podsumowanie

Rodowod: pomysl zamrozonych par input/output i zestaw asercji binarnych pochodza
z pielas-activy/humanizer-pl (MIT (C) 2026 Igor Pielas). Mechanika napisana od
nowa: rdzenie fleksyjne z granica wyrazu zamiast dopasowania podciagow, stosunek
dlugosci zamiast twardego porownania, flagi per case, rejestr asercji sterowany
danymi. Szczegoly w CREDITS.md.

Uwaga dla edytujacych: komunikaty ida do terminala po polsku z pelna diakrytyka,
ale cudzyslowy drukarskie wstawia wylacznie funkcja q() - dzieki temu w samych
literalach kodu nie ma znakow, ktore latwo zdegradowac przy edycji.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE / "evals.json"

EM_DASH = "—"
EN_DASH = "–"
QUOTE_OPEN_PL = "„"
QUOTE_CLOSE_PL = "”"
QUOTE_OPEN_EN = "“"
ASCII_QUOTE = '"'
SPACES = (" ", " ", " ")
ELLIPSIS = "…"

STATUS_OK = "OK"
STATUS_FAIL = "BŁĄD"
STATUS_SKIP = "POMIN"

DEFAULT_STEM_TEMPLATE = "\\b<stem>"

# Skladanie diakrytykow: tekst pisany bez ogonkow to osobny gatunek wejscia
# (SPEC, case "tekst bez ogonkow"), a rdzenie w evals.json maja ogonki. Bez tego
# odwzorowania caly slownik AI-slopu przechodzilby przez taki tekst niezauwazony.
DIACRITIC_FOLD = str.maketrans(
    "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
    "acelnoszzACELNOSZZ",
)
PL_DIACRITICS = re.compile("[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]")

# Znaki, ktore w pierwszym wierszu sa tylko dekoracja Markdown i nie zmieniaja
# tego, od czego wiersz zaczyna sie w sensie stylistycznym.
MARKDOWN_LEAD = re.compile(r"^[\s>#*•\-–—.)\]\d]+")


def q(text: str) -> str:
    """Ujmuje fragment w polski cudzyslow drukarski."""
    return f"{QUOTE_OPEN_PL}{text}{QUOTE_CLOSE_PL}"


def fold(text: str) -> str:
    """Usuwa polskie diakrytyki. Odwzorowanie jest 1:1 na znakach, wiec offsety
    dopasowan w tekscie zlozonym zgadzaja sie z offsetami w oryginale."""
    return text.translate(DIACRITIC_FOLD)


def config_error(message: str) -> None:
    """Konczy prace kodem 2 - to blad pliku evals.json, nie porazka asercji."""
    print(f"BŁĄD KONFIGURACJI: {message}", file=sys.stderr)
    raise SystemExit(2)


def load_config(path: Path) -> dict:
    if not path.exists():
        config_error(f"brak pliku {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        config_error(f"{path} nie jest poprawnym JSON-em: {exc}")
    return {}


def resolve_source(cfg: dict, spec: str) -> list:
    """Zwraca liste wskazana sciezka typu config.banned_stems_pl."""
    node: object = cfg
    for part in spec.split("."):
        if not isinstance(node, dict) or part not in node:
            config_error(f"nie znaleziono źródła {q(spec)}")
        node = node[part]  # type: ignore[index]
    if not isinstance(node, list):
        config_error(f"źródło {q(spec)} nie jest listą")
    return list(node)  # type: ignore[arg-type]


def stem_fragment(entry) -> tuple:
    """Rozpakowuje wpis listy rdzeni. Wpis moze byc lancuchem albo obiektem
    {stem, fold, variants, why}. Obiekt sluzy do wylaczenia skladania diakrytykow
    na rdzeniu, ktory po zlozeniu zlepilby sie z innym lematem (G1 5.4), oraz do
    podania jawnych wariantow zamiast polegania na skladaniu.

    Stan uzycia (G1 runda 4, obserwacja 4.3, po weryfikacji): postac obiektowa jest
    uzywana przez jeden rdzen (`niezwykle` w banned_stems_soft, fold wylaczony).
    Nieuzywane pozostaje wylacznie podpole `variants` - zarezerwowane na rdzenie,
    dla ktorych trzeba bedzie wypisac formy recznie zamiast opierac sie na `\\w*`."""
    if isinstance(entry, dict):
        stem = entry.get("stem")
        if not stem:
            config_error("wpis rdzenia bez pola stem")
        variants = entry.get("variants") or []
        fragment = stem if not variants else "(?:" + "|".join([stem] + list(variants)) + ")"
        return fragment, bool(entry.get("fold", True))
    return str(entry), True


def compile_stems(entries: list, template: str, case_insensitive: bool, folding: bool) -> list:
    """Kompiluje rdzenie do krotek (rdzen, regex, czy_szukac_w_tekscie_zlozonym).
    Rdzen z wylaczonym skladaniem zawsze pracuje na tekscie oryginalnym."""
    flags = re.IGNORECASE if case_insensitive else 0
    compiled = []
    for entry in entries:
        fragment, foldable = stem_fragment(entry)
        use_folded = folding and foldable
        pattern = template.replace("<stem>", fold(fragment) if use_folded else fragment)
        try:
            compiled.append((fragment, re.compile(pattern, flags), use_folded))
        except re.error as exc:
            config_error(f"niepoprawne wyrażenie {q(pattern)}: {exc}")
    return compiled


def context(text: str, index: int, width: int = 18) -> str:
    start = max(0, index - width)
    end = min(len(text), index + width)
    return text[start:end].replace("\n", " ")


def format_hits(text: str, hits: list, limit: int = 3) -> str:
    """Fragmenty wycinamy z ORYGINALU po offsetach dopasowania, zeby raport
    pokazywal tekst z ogonkami nawet wtedy, gdy dopasowanie szlo po tekscie
    zlozonym."""
    parts = []
    for match in hits[:limit]:
        fragment = text[match.start():match.end()].strip().replace("\n", " ")
        parts.append(f"{q(fragment)} (poz. {match.start()})")
    suffix = f" i {len(hits) - limit} dalszych" if len(hits) > limit else ""
    return ", ".join(parts) + suffix


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ""


def compile_pattern(pattern: str, case_insensitive: bool):
    try:
        return re.compile(pattern, re.IGNORECASE if case_insensitive else 0)
    except re.error as exc:
        config_error(f"niepoprawne wyrażenie {q(pattern)}: {exc}")
    return None


def check_regex_absent(text: str, pattern: str, case_insensitive: bool) -> tuple:
    hits = list(compile_pattern(pattern, case_insensitive).finditer(text))
    if hits:
        return False, "trafienia: " + format_hits(text, hits)
    return True, "brak trafień"


def check_regex_present(text: str, pattern: str, case_insensitive: bool) -> tuple:
    hits = list(compile_pattern(pattern, case_insensitive).finditer(text))
    if hits:
        return True, f"trafień: {len(hits)}"
    return False, "brak wymaganego wzorca"


def collect_hits(text: str, compiled: list) -> list:
    """Kazdy rdzen szuka w tekscie oryginalnym albo zlozonym, zaleznie od wlasnego
    ustawienia. Offsety sa wspolne, bo skladanie jest odwzorowaniem 1:1."""
    folded = fold(text)
    hits = []
    for _stem, regex, use_folded in compiled:
        hits.extend(regex.finditer(folded if use_folded else text))
    hits.sort(key=lambda match: match.start())
    return hits


def check_stems_absent(text: str, compiled: list, fold_diacritics: bool) -> tuple:
    hits = collect_hits(text, compiled)
    if hits:
        return False, "trafienia: " + format_hits(text, hits)
    tail = " (część rdzeni także w tekście złożonym bez ogonków)" if fold_diacritics else ""
    return True, f"czysto na {len(compiled)} rdzeniach{tail}"


def check_first_line(text: str, openers: list, fold_diacritics: bool) -> tuple:
    line = first_nonempty_line(text)
    raw_probe = MARKDOWN_LEAD.sub("", line).casefold()
    folded_probe = fold(raw_probe)
    for opener in openers:
        fragment, foldable = stem_fragment(opener)
        use_folded = fold_diacritics and foldable
        candidate = fragment.casefold()
        probe = folded_probe if use_folded else raw_probe
        if probe.startswith(fold(candidate) if use_folded else candidate):
            return False, f"pierwszy wiersz otwiera wypełniacz {q(fragment)}"
    preview = line[:48] + (ELLIPSIS if len(line) > 48 else "")
    return True, f"pierwszy wiersz: {q(preview)}"


def check_length_ratio(source: str, target: str, limit: float) -> tuple:
    if not source:
        return not target, "wejście puste, wyjście też musi być puste"
    ratio = len(target) / len(source)
    return ratio <= limit + 1e-9, f"stosunek {ratio:.2f} (limit {limit:.2f})"


def check_density(text: str, compiled: list, limit: float, per_chars: int, min_hits: int) -> tuple:
    """Gestosc zamiast zakazu: pojedyncze wystapienie terminu fachowego czy formuly
    orzeczniczej jest poprawna polszczyzna, tellem jest dopiero nagromadzenie.
    Do min_hits wlacznie przechodzi zawsze. Mianownik ma podloge per_chars, zeby
    krotki tekst nie wybuchal gestoscia przy dwoch trafieniach.

    Uwaga o podlodze: przy obecnych progach (min_hits 2, limit 1.5) NIE zmienia ona
    zadnego werdyktu, bo najmniejsza gestosc ponad progiem to 3/1000 = 3.00, czyli
    i tak powyzej limitu. Podloga wplywa wylacznie na liczbe w raporcie. Dlatego nie
    da sie jej upilnowac case'em regresyjnym - przy limicie 3.0 lub wyzszym zaczela
    by byc nosna, ale takie poluzowanie oslabiloby detektor."""
    hits = collect_hits(text, compiled)
    if len(hits) <= min_hits:
        return True, f"{len(hits)} trafień, próg tolerancji {min_hits}"
    density = len(hits) / max(len(text), per_chars) * per_chars
    detail = (
        f"{len(hits)} trafień na {len(text)} znaków = {density:.2f} "
        f"na {per_chars} (limit {limit:.2f})"
    )
    passed = density <= limit + 1e-9
    if not passed:
        detail += "; " + format_hits(text, hits)
    return passed, detail


def check_endash_pwn(text: str, strict: bool) -> tuple:
    """Norma PWN dopuszcza polpauze w trzech kontekstach: miedzy cyframi bez spacji
    (zakres liczbowy), ze spacjami po obu stronach (pauza zdaniowa) oraz na poczatku
    wiersza ze spacja po niej (pauza dialogowa). Flaga regula_anty_tell zakazuje jej
    wszedzie - w takim case'ie nawet poprawna polpauza jest szukanym tellem."""
    problems = []
    for index, char in enumerate(text):
        if char != EN_DASH:
            continue
        if strict:
            problems.append(f"poz. {index}: {q(ELLIPSIS + context(text, index) + ELLIPSIS)}")
            continue
        previous = text[index - 1] if index > 0 else ""
        following = text[index + 1] if index + 1 < len(text) else ""
        numeric_range = previous.isdigit() and following.isdigit()
        sentence_pause = previous in SPACES and following in SPACES
        dialogue_dash = previous in ("", "\n") and following in SPACES
        if not (numeric_range or sentence_pause or dialogue_dash):
            problems.append(f"poz. {index}: {q(ELLIPSIS + context(text, index) + ELLIPSIS)}")
    if problems:
        head = "; ".join(problems[:3])
        suffix = f" i {len(problems) - 3} dalszych" if len(problems) > 3 else ""
        prefix = "półpauza zakazana w tym case'ie" if strict else "półpauza poza normą PWN"
        return False, f"{prefix}: {head}{suffix}"
    return True, "brak półpauz" if strict else "półpauzy zgodne z normą PWN"


def check_em_dash_pl(text: str, strict: bool, literary: bool) -> tuple:
    """Myslnik em jest w polskiej prozie angielskim tellem, ale norma dopuszcza go
    w zapisie dialogu. Legalne: na poczatku wiersza ze spacja po nim oraz w srodku
    wiersza w konwencji dialogowej - w wierszu otwartym pauza dialogowa albo w
    case'ie oznaczonym flaga gatunek_literacki. Flaga regula_anty_tell zakazuje go
    wszedzie.

    Znana heurystyka (G1 runda 4, obserwacja 4.2): wiersz otwarty pauza dialogowa
    legalizuje wszystkie dalsze pauze w TYM SAMYM wierszu, wiec narracyjny slop
    dopisany do repliki przejdzie. Model zagrozen evals nie obejmuje wyjsc
    preparowanych pod test, a alternatywa (parowanie replik z narracja) kosztuje
    wiecej falszywych alarmow, niz daje. Do rozwazenia przy case'ach literackich."""
    problems = []
    line_starts_with_dash = {}
    for index, char in enumerate(text):
        if char != EM_DASH:
            continue
        if strict:
            problems.append(f"poz. {index}: {q(ELLIPSIS + context(text, index) + ELLIPSIS)}")
            continue
        previous = text[index - 1] if index > 0 else ""
        following = text[index + 1] if index + 1 < len(text) else ""
        line_start = text.rfind("\n", 0, index) + 1
        if line_start not in line_starts_with_dash:
            head = text[line_start:line_start + 2]
            line_starts_with_dash[line_start] = head[:1] == EM_DASH and head[1:2] in SPACES
        dialogue_opening = previous in ("", "\n") and following in SPACES
        dialogue_inline = (
            previous in SPACES
            and following in SPACES
            and (literary or line_starts_with_dash[line_start])
        )
        if not (dialogue_opening or dialogue_inline):
            problems.append(f"poz. {index}: {q(ELLIPSIS + context(text, index) + ELLIPSIS)}")
    if problems:
        head = "; ".join(problems[:3])
        suffix = f" i {len(problems) - 3} dalszych" if len(problems) > 3 else ""
        prefix = (
            "myślnik em zakazany w tym case'ie"
            if strict
            else "myślnik em poza konwencją dialogową"
        )
        return False, f"{prefix}: {head}{suffix}"
    return True, "brak myślników em" if strict else "myślniki em tylko w zapisie dialogu"


def mask_code(text: str) -> str:
    """Zastepuje bloki kodu i wstawki w grawisach spacjami, zachowujac dlugosc i
    podzial na wiersze. Proste cudzyslowy w kodzie sa legalne, wiec nie moga
    obciazac kontroli typograficznej prozy."""

    def blank(match: re.Match) -> str:
        return "".join("\n" if char == "\n" else " " for char in match.group(0))

    text = re.sub(r"```.*?```", blank, text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", blank, text)


def check_english_quotes(text: str) -> tuple:
    """U+201D jest polskim cudzyslowem zamykajacym, wiec nie mozna go zakazac
    wprost. Tellem sa: cudzyslow otwierajacy U+201C, zamykajace U+201D bez pary w
    U+201E, para otwarta U+201E i domknieta prostym cudzyslowem oraz cudzyslow
    niedomkniety do konca akapitu."""
    problems = []
    masked = mask_code(text)
    opening_en = masked.count(QUOTE_OPEN_EN)
    if opening_en:
        problems.append(f"angielski cudzysłów otwierający U+201C: {opening_en}x")
    stray = masked.count(QUOTE_CLOSE_PL) - masked.count(QUOTE_OPEN_PL)
    if stray > 0:
        problems.append(
            f"zamykających U+201D o {stray} więcej niż otwierających U+201E, "
            f"czyli para w stylu angielskim"
        )
    for index, char in enumerate(masked):
        if char != QUOTE_OPEN_PL:
            continue
        paragraph_end = masked.find("\n\n", index)
        segment = masked[index + 1:paragraph_end if paragraph_end != -1 else len(masked)]
        closing_pl = segment.find(QUOTE_CLOSE_PL)
        closing_ascii = segment.find(ASCII_QUOTE)
        if closing_pl == -1 and closing_ascii == -1:
            problems.append(f"cudzysłów otwarty na poz. {index} nie domyka się w akapicie")
        elif closing_ascii != -1 and (closing_pl == -1 or closing_ascii < closing_pl):
            problems.append(
                f"poz. {index}: para otwarta U+201E, domknięta prostym cudzysłowem "
                f"{q(ELLIPSIS + context(text, index) + ELLIPSIS)}"
            )
    if problems:
        head = "; ".join(problems[:3])
        suffix = f" i {len(problems) - 3} dalszych" if len(problems) > 3 else ""
        return False, head + suffix
    return True, "cudzysłowy w normie polskiej"


CUSTOM_CHECKS = ("emdash_pl", "endash_pwn", "english_quotes")


def evaluate(assertion: dict, case: dict, cfg: dict) -> tuple:
    """Zwraca (status, passed, detail). Status POMIN oznacza, ze asercja nie dotyczy
    tego case'a: zawiesila ja flaga, warunek wejsciowy albo jawne pominiecie."""
    aid = assertion.get("id")
    if not aid:
        config_error("asercja bez pola id")
    flags = case.get("flags") or {}
    source_text = case.get("input", "")
    target_text = case.get("output", "")

    for flag in assertion.get("suspended_by_flags", []):
        if flags.get(flag):
            return STATUS_SKIP, None, f"zawieszona przez flagę {q(flag)}"
    if aid in (case.get("skip_assertions") or []):
        return STATUS_SKIP, None, "pominięta jawnie w case'ie"
    when_input = assertion.get("when_input_regex")
    if when_input and not compile_pattern(when_input, False).search(source_text):
        return STATUS_SKIP, None, "wejście nie spełnia warunku when_input_regex"

    kind = assertion.get("type")
    default_ci = bool(assertion.get("case_insensitive", False))

    if kind == "regex_absent":
        return _wrap(check_regex_absent(target_text, assertion["pattern"], default_ci))
    if kind == "regex_present":
        return _wrap(check_regex_present(target_text, assertion["pattern"], default_ci))
    # Skladanie ogonkow wlacza sie tylko wtedy, gdy wejscie faktycznie jest ich
    # pozbawione. Na tekscie pisanym poprawnie skladanie nic nie wnosi, a potrafi
    # zlepic dwa lematy (G1 5.4). Poszczegolne rdzenie moga sie z niego wypisac
    # osobno, przez pole fold w obiekcie rdzenia.
    folding = bool(assertion.get("fold_diacritics", False)) and not PL_DIACRITICS.search(
        source_text
    )

    if kind == "stems_absent":
        compiled = compile_stems(
            resolve_source(cfg, assertion["source"]),
            assertion.get("match", DEFAULT_STEM_TEMPLATE),
            assertion.get("case_insensitive", True),
            folding,
        )
        return _wrap(check_stems_absent(target_text, compiled, folding))
    if kind == "first_nonempty_line_not_startswith":
        return _wrap(
            check_first_line(target_text, resolve_source(cfg, assertion["source"]), folding)
        )
    if kind == "length_ratio_lte":
        return _wrap(check_length_ratio(source_text, target_text, float(assertion["value"])))
    if kind == "density_lte":
        compiled = compile_stems(
            resolve_source(cfg, assertion["source"]),
            assertion.get("match", DEFAULT_STEM_TEMPLATE),
            assertion.get("case_insensitive", True),
            folding,
        )
        return _wrap(
            check_density(
                target_text,
                compiled,
                float(assertion["value"]),
                int(assertion.get("per_chars", 1000)),
                int(assertion.get("min_hits", 0)),
            )
        )
    if kind == "custom":
        check = assertion.get("check")
        if check == "emdash_pl":
            return _wrap(
                check_em_dash_pl(
                    target_text,
                    bool(flags.get("regula_anty_tell")),
                    bool(flags.get("gatunek_literacki")),
                )
            )
        if check == "endash_pwn":
            return _wrap(check_endash_pwn(target_text, bool(flags.get("regula_anty_tell"))))
        if check == "english_quotes":
            return _wrap(check_english_quotes(target_text))
        config_error(
            f"asercja {q(str(aid))}: nieznana kontrola {q(str(check))}, "
            f"dostępne: {', '.join(CUSTOM_CHECKS)}"
        )
    config_error(f"asercja {q(str(aid))}: nieznany typ {q(str(kind))}")
    return STATUS_FAIL, False, ""


def _wrap(result: tuple) -> tuple:
    passed, detail = result
    return (STATUS_OK if passed else STATUS_FAIL), passed, detail


def run_case(case: dict, cfg: dict, quiet: bool) -> tuple:
    """Uruchamia wszystkie asercje na jednym case'ie. Zwraca (liczba_bledow, linie)."""
    lines = []
    errors = 0
    flags = case.get("flags") or {}
    name = case.get("name", "(bez nazwy)")
    genre = case.get("genre", "?")
    markers = [flag for flag, value in flags.items() if value]
    if case.get("mock"):
        markers.append("mock")
    marker_text = f" [{', '.join(markers)}]" if markers else ""
    source_text = case.get("input", "")
    target_text = case.get("output", "")

    lines.append(f"=== {name} (gatunek: {genre}){marker_text}")
    lines.append(f"    znaki: wejście {len(source_text)}, wyjście {len(target_text)}")

    if flags.get("human_control"):
        identical = source_text == target_text
        detail = (
            "wyjście identyczne z wejściem"
            if identical
            else "kontrola ludzka wymaga wyjścia identycznego z wejściem"
        )
        lines.append(
            f"    [{STATUS_OK if identical else STATUS_FAIL}] human_control_identity - {detail}"
        )
        if not identical:
            errors += 1

    for assertion in cfg.get("assertions", []):
        aid = assertion["id"]
        status, passed, detail = evaluate(assertion, case, cfg)
        if status == STATUS_SKIP:
            if not quiet:
                lines.append(f"    [{STATUS_SKIP}] {aid} - {detail}")
            continue
        expected = case.get("expect", {}).get(aid, True)
        if flags.get("human_control") and expected is False:
            lines.append(
                f"    [{STATUS_FAIL}] {aid} - case kontrolny nie może oczekiwać porażki asercji"
            )
            errors += 1
            continue
        mismatch = passed != expected
        if mismatch:
            errors += 1
        note = "" if not mismatch else f"  (oczekiwano: {'sukces' if expected else 'porażka'})"
        if mismatch or not quiet:
            lines.append(f"    [{STATUS_FAIL if mismatch else status}] {aid} - {detail}{note}")

    return errors, lines


def check_expectations_have_assertions(cfg: dict) -> None:
    """Kazde oczekiwanie musi wskazywac istniejaca asercje.

    Bez tej kontroli usuniecie calej asercji z rejestru przechodzi niezauwazone:
    wpis w `expect` przestaje miec do czego sie odnosic, a zestaw milczy. To ta sama
    klasa cichego oslabienia, przed ktora broni blok case'ow regresyjnych, tyle ze
    piętro wyzej - w samym rejestrze zamiast w mechanice pojedynczej kontroli."""
    znane = {assertion.get("id") for assertion in cfg.get("assertions", [])}
    osierocone = {}
    for case in cfg.get("cases", []):
        obce = sorted(set(case.get("expect", {})) - znane)
        if obce:
            osierocone[case.get("name", "(bez nazwy)")] = obce
    if osierocone:
        opis = "; ".join(f"{name}: {', '.join(ids)}" for name, ids in osierocone.items())
        config_error(f"oczekiwania bez odpowiadającej asercji w rejestrze - {opis}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Ewaluacje skilla humanizer-pl (offline).")
    parser.add_argument("--case", help="uruchom tylko case'y zawierające ten fragment nazwy")
    parser.add_argument("--quiet", action="store_true", help="pokaż tylko błędy i podsumowanie")
    args = parser.parse_args()

    cfg = load_config(CONFIG_PATH)
    check_expectations_have_assertions(cfg)
    cases = cfg.get("cases", [])
    if args.case:
        cases = [case for case in cases if args.case.lower() in case.get("name", "").lower()]
    if not cases:
        print("Brak case'ów do uruchomienia.", file=sys.stderr)
        return 1

    print(f"humanizer-pl - ewaluacje z {CONFIG_PATH.name} (wersja {cfg.get('version', '?')})")
    print(f"case'ów: {len(cases)}, asercji w rejestrze: {len(cfg.get('assertions', []))}\n")

    total_errors = 0
    mocks = 0
    for case in cases:
        errors, lines = run_case(case, cfg, args.quiet)
        total_errors += errors
        mocks += 1 if case.get("mock") else 0
        print("\n".join(lines))
        print()

    if mocks:
        print(f"Uwaga: {mocks} case'ów to mocki, Faza 3 zastępuje je zestawem golden.")
    if total_errors:
        print(f"WYNIK: {total_errors} niezgodności z oczekiwaniami.")
        return 1
    print("WYNIK: wszystkie asercje zgodne z oczekiwaniami.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
