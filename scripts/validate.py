#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Walidator pakietu humanizer-pl.

Sprawdza to, czego nie widac golym okiem przy przegladzie plikow: ksztalt
frontmattera SKILL.md, zgodnosc numeru wersji miedzy SKILL.md, plugin.json i
CHANGELOG.md, ciaglosc numeracji 41 wzorcow, budzety linii z SPEC, obecnosc
profili lokalnych w .gitignore, typografie wlasnej dokumentacji (cudzyslowy i
mysliniki em). Na koncu uruchamia evals/run_evals.py.

Bez zaleznosci zewnetrznych, bez sieci, bez zapisow. Sciezki wzgledem tego pliku.

    python3 scripts/validate.py             # tolerancyjnie: brak cudzego pliku = POMIN
    python3 scripts/validate.py --strict    # kazdy POMIN staje sie bledem (tryb CI)

Kody wyjscia: 0 czysto, 1 wykryto bledy.

Rodowod: uklad kontroli (frontmatter bez kluczy nieprzenosnych, synchronizacja
wersji miedzy manifestami, ciaglosc numeracji wzorcow, budzet linii) pochodzi z
blader/humanizer 2.9.1 (MIT). Tutaj przepisany na raport zbiorczy z trybem
tolerancyjnym i scislym zamiast przerywania na pierwszym bledzie. Patrz CREDITS.md.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKILL_NAME = "humanizer-pl"
PATTERN_COUNT = 41
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

QUOTE_OPEN_PL = "„"
QUOTE_CLOSE_PL = "”"

# Budzety linii z tabeli SPEC. Klucz to sciezka wzgledem korzenia repo.
LINE_BUDGETS = {
    "SKILL.md": 250,
    "references/wzorce-pl.md": 550,
    "references/polszczyzna.md": 200,
    "references/typografia.md": 140,
    "references/gatunki.md": 120,
    "references/audyt-semantyczny.md": 150,
    "references/przyklady.md": 300,
}

# Wlasciciele plikow z SPEC - potrzebni tylko po to, zeby komunikat o braku pliku
# mowil, na kogo czekamy.
OWNERS = {
    "SKILL.md": "autor-taksonomii",
    "references/wzorce-pl.md": "autor-taksonomii",
    "references/polszczyzna.md": "autor-taksonomii",
    "references/typografia.md": "autor-taksonomii",
    "references/gatunki.md": "autor-taksonomii",
    "references/audyt-semantyczny.md": "autor-taksonomii",
    "references/przyklady.md": "autor-przykladow",
    "CHANGELOG.md": "dokumentalista",
    "README.md": "dokumentalista",
    "LICENSE": "dokumentalista",
    "NOTICE.md": "dokumentalista",
    "CREDITS.md": "dokumentalista",
}

FORBIDDEN_FRONTMATTER_KEYS = ("allowed-tools", "compatibility", "version")


def q(text: str) -> str:
    return f"{QUOTE_OPEN_PL}{text}{QUOTE_CLOSE_PL}"


class Report:
    """Zbiera wyniki kontroli. W trybie scislym POMIN liczy sie jako blad."""

    def __init__(self, strict: bool) -> None:
        self.strict = strict
        self.errors: list = []
        self.skips: list = []
        self.passed = 0

    def ok(self, message: str) -> None:
        self.passed += 1
        print(f"  [OK] {message}")

    def error(self, message: str) -> None:
        self.errors.append(message)
        print(f"  [BŁĄD] {message}")

    def skip(self, message: str) -> None:
        if self.strict:
            self.errors.append(message)
            print(f"  [BŁĄD] {message} (tryb ścisły)")
        else:
            self.skips.append(message)
            print(f"  [POMIN] {message}")

    def note(self, message: str) -> None:
        print(f"  [INFO] {message}")


def read_optional(relative: str, report: Report) -> str:
    path = ROOT / relative
    if not path.exists():
        owner = OWNERS.get(relative, "?")
        report.skip(f"brak pliku {relative} (właściciel: {owner})")
        return ""
    return path.read_text(encoding="utf-8")


def read_required(relative: str, report: Report) -> str:
    path = ROOT / relative
    if not path.exists():
        report.error(f"brak wymaganego pliku {relative}")
        return ""
    return path.read_text(encoding="utf-8")


def check_skill_frontmatter(report: Report) -> str:
    """Zwraca wersje z metadata.version albo pusty string."""
    print("\nFrontmatter SKILL.md")
    text = read_optional("SKILL.md", report)
    if not text:
        return ""
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        report.error("SKILL.md musi zaczynać się blokiem frontmattera YAML")
        return ""
    frontmatter = match.group(1)

    if re.search(rf"(?m)^name:\s*{re.escape(SKILL_NAME)}\s*$", frontmatter):
        report.ok(f"name: {SKILL_NAME}")
    else:
        report.error(f"frontmatter musi mieć dokładnie name: {SKILL_NAME}")

    if re.search(r"(?m)^description:", frontmatter):
        report.ok("description obecny")
    else:
        report.error("frontmatter bez pola description")

    if re.search(r"(?m)^license:\s*MIT\s*$", frontmatter):
        report.ok("license: MIT")
    else:
        report.error("frontmatter musi mieć license: MIT")

    for key in FORBIDDEN_FRONTMATTER_KEYS:
        if re.search(rf"(?m)^{re.escape(key)}:", frontmatter):
            report.error(f"usuń klucz {q(key)} z poziomu głównego frontmattera")
        else:
            report.ok(f"brak klucza {q(key)} na poziomie głównym")

    version_match = re.search(
        r"(?m)^\s+version:\s*[\"']?(\d+\.\d+\.\d+)[\"']?\s*$", frontmatter
    )
    if not version_match:
        report.error("brak metadata.version w formacie X.Y.Z")
        return ""
    report.ok(f"metadata.version: {version_match.group(1)}")
    return version_match.group(1)


def check_plugin_manifest(report: Report) -> str:
    print("\nManifesty .claude-plugin")
    text = read_required(".claude-plugin/plugin.json", report)
    if not text:
        return ""
    try:
        plugin = json.loads(text)
    except json.JSONDecodeError as exc:
        report.error(f"plugin.json nie jest poprawnym JSON-em: {exc}")
        return ""

    if plugin.get("name") == SKILL_NAME:
        report.ok(f"plugin.json name: {SKILL_NAME}")
    else:
        report.error(f"plugin.json name to {q(str(plugin.get('name')))}, oczekiwano {SKILL_NAME}")

    version = str(plugin.get("version", ""))
    if SEMVER.match(version):
        report.ok(f"plugin.json version: {version}")
    else:
        report.error(f"plugin.json version {q(version)} nie jest wersją semantyczną")

    if plugin.get("license") == "MIT":
        report.ok("plugin.json license: MIT")
    else:
        report.error("plugin.json musi deklarować license: MIT")

    market_text = read_required(".claude-plugin/marketplace.json", report)
    if market_text:
        try:
            marketplace = json.loads(market_text)
            plugins = marketplace.get("plugins", [])
            if not plugins:
                report.error("marketplace.json nie wymienia żadnej wtyczki")
            else:
                entry = plugins[0]
                if entry.get("name") == SKILL_NAME and entry.get("source") == "./":
                    report.ok("marketplace.json wskazuje na wtyczkę z tego repo")
                else:
                    report.error(
                        "marketplace.json musi wskazywać name: "
                        f"{SKILL_NAME} i source: ./"
                    )
        except json.JSONDecodeError as exc:
            report.error(f"marketplace.json nie jest poprawnym JSON-em: {exc}")

    return version


def check_changelog(report: Report) -> str:
    print("\nCHANGELOG.md")
    text = read_optional("CHANGELOG.md", report)
    if not text:
        return ""
    match = re.search(r"(?m)^#{2,3}\s*\[?(\d+\.\d+\.\d+)\]?", text)
    if not match:
        report.error("pierwszy wpis CHANGELOG.md nie zawiera numeru wersji X.Y.Z")
        return ""
    report.ok(f"pierwszy wpis: {match.group(1)}")
    return match.group(1)


def check_versions(report: Report, versions: dict) -> None:
    print("\nSynchronizacja wersji")
    known = {source: value for source, value in versions.items() if value}
    if len(known) < 2:
        report.skip("za mało źródeł wersji, żeby porównać (potrzebne co najmniej dwa)")
        return
    distinct = set(known.values())
    if len(distinct) == 1:
        report.ok(f"zgodne we wszystkich źródłach ({', '.join(sorted(known))}): {distinct.pop()}")
    else:
        detail = ", ".join(f"{source}={value}" for source, value in sorted(known.items()))
        report.error(f"rozjazd wersji: {detail}")


def check_pattern_numbering(report: Report) -> None:
    print("\nNumeracja wzorców w references/wzorce-pl.md")
    text = read_optional("references/wzorce-pl.md", report)
    if not text:
        return
    numbers = [int(value) for value in re.findall(r"(?m)^### (\d+)\.\s", text)]
    expected = list(range(1, PATTERN_COUNT + 1))
    if numbers == expected:
        report.ok(f"ciągła numeracja 1-{PATTERN_COUNT}")
        return
    missing = sorted(set(expected) - set(numbers))
    extra = sorted(set(numbers) - set(expected))
    duplicated = sorted({value for value in numbers if numbers.count(value) > 1})
    problems = []
    if missing:
        problems.append(f"brakuje: {missing}")
    if extra:
        problems.append(f"poza zakresem: {extra}")
    if duplicated:
        problems.append(f"powtórzone: {duplicated}")
    if not problems:
        problems.append(f"zła kolejność: {numbers}")
    report.error("numeracja wzorców niepoprawna - " + "; ".join(problems))


def check_line_budgets(report: Report) -> None:
    print("\nBudżety linii")
    for relative, budget in LINE_BUDGETS.items():
        path = ROOT / relative
        if not path.exists():
            report.skip(f"brak pliku {relative} (właściciel: {OWNERS.get(relative, '?')})")
            continue
        lines = len(path.read_text(encoding="utf-8").splitlines())
        if lines <= budget:
            report.ok(f"{relative}: {lines}/{budget}")
        else:
            report.error(f"{relative}: {lines} linii przekracza budżet {budget}")


def check_gitignore(report: Report) -> None:
    print("\n.gitignore")
    text = read_required(".gitignore", report)
    if not text:
        return
    entries = [line.strip() for line in text.splitlines()]
    if "references/*.local.md" in entries:
        report.ok("profile lokalne (references/*.local.md) poza gitem")
    else:
        report.error("dopisz references/*.local.md do .gitignore")
    stray = sorted(path.name for path in (ROOT / "references").glob("*.local.md"))
    if stray:
        report.note(f"profile lokalne obecne w katalogu roboczym: {', '.join(stray)}")


def load_runner():
    """Importuje runner ewaluacji, zeby walidator uzywal DOKLADNIE tej samej
    definicji normy typograficznej, ktorej pilnuje w wyjsciu skilla."""
    sys.path.insert(0, str(ROOT / "evals"))
    try:
        import run_evals  # type: ignore[import-not-found]

        return run_evals
    except ImportError:
        return None


def mask_exhibits(text: str) -> str:
    """Wygasza wiersze cytatu blokowego. Wedlug SPEC eksponat lamiacy norme wolno
    umiescic wylacznie w cytacie albo w kodzie, wiec kontrola typograficzna
    obejmuje prozy wlasnej, a nie przykladow PRZED."""
    output = []
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(">"):
            output.append("".join("\n" if char == "\n" else " " for char in line))
        else:
            output.append(line)
    return "".join(output)


def check_markdown_typography(report: Report) -> None:
    """Dogfooding: proza wlasnej dokumentacji podlega tej samej normie, ktorej skill
    pilnuje w cudzych tekstach. Trzy warstwy: parzystosc cudzyslowow, pelna logika
    parowania oraz mysliniki em. Straznik klas defektu wykrytych na bramce G1."""
    print("\nTypografia własnej dokumentacji")
    runner = load_runner()
    if runner is None:
        report.skip("nie udało się zaimportować evals/run_evals.py, kontrola pominięta")
        return
    documents = sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and not path.name.endswith(".local.md")
    )
    if not documents:
        report.skip("brak plików .md do sprawdzenia")
        return
    for path in documents:
        relative = path.relative_to(ROOT)
        prose = mask_exhibits(runner.mask_code(path.read_text(encoding="utf-8")))
        problems = []

        opening = prose.count(QUOTE_OPEN_PL)
        closing = prose.count(QUOTE_CLOSE_PL)
        if opening != closing:
            problems.append(
                f"nieparzyste cudzysłowy: otwierających {opening}, zamykających {closing}"
            )

        paired, detail = runner.check_english_quotes(prose)
        if not paired:
            problems.append(detail)

        dashes_ok, dash_detail = runner.check_em_dash_pl(prose, False, False)
        if not dashes_ok:
            problems.append(dash_detail)

        if problems:
            report.error(f"{relative}: " + "; ".join(problems))
        else:
            report.ok(f"{relative}: {opening} par cudzysłowu, myślniki em w normie")


def check_evals(report: Report) -> None:
    print("\nEwaluacje")
    runner = ROOT / "evals" / "run_evals.py"
    if not runner.exists():
        report.error("brak evals/run_evals.py")
        return
    result = subprocess.run(
        [sys.executable, str(runner), "--quiet"],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    for line in (result.stdout or "").splitlines():
        if line.strip():
            print(f"      {line}")
    for line in (result.stderr or "").splitlines():
        if line.strip():
            print(f"      {line}")
    if result.returncode == 0:
        report.ok("run_evals.py zakończony bez niezgodności")
    else:
        report.error(f"run_evals.py zwrócił kod {result.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Walidator pakietu humanizer-pl.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="brak pliku lub pominięta kontrola to błąd (tryb CI)",
    )
    args = parser.parse_args()

    print(f"humanizer-pl - walidacja pakietu w {ROOT}")
    print("tryb: ścisły" if args.strict else "tryb: tolerancyjny (brakujące pliki = POMIN)")

    report = Report(args.strict)
    skill_version = check_skill_frontmatter(report)
    plugin_version = check_plugin_manifest(report)
    changelog_version = check_changelog(report)
    check_versions(
        report,
        {
            "SKILL.md": skill_version,
            "plugin.json": plugin_version,
            "CHANGELOG.md": changelog_version,
        },
    )
    check_pattern_numbering(report)
    check_line_budgets(report)
    check_gitignore(report)
    check_markdown_typography(report)
    check_evals(report)

    print("\nPodsumowanie")
    print(f"  kontroli zdanych: {report.passed}")
    print(f"  pominiętych: {len(report.skips)}")
    print(f"  błędów: {len(report.errors)}")
    if report.errors:
        for message in report.errors:
            print(f"    - {message}")
        return 1
    if report.skips and not args.strict:
        print("  pakiet spójny w zakresie plików, które już istnieją.")
    else:
        print("  pakiet spójny.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
