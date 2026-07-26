# Mapa atrybucji

Ten plik odpowiada na pytanie „skąd wziął się ten konkretny fragment skilla”. Noty licencyjne w pełnym brzmieniu są w [NOTICE.md](NOTICE.md), a rodowód opisany narracyjnie – w sekcji „Rodowód i zapożyczenia” w [README.md](README.md).

Wiersze poniżej pochodzą z notatek prowadzonych przez autorów poszczególnych plików w trakcie pisania i zostały zestawione z treścią repozytorium po pomiarze zbieżności. Rejestr jest zamknięty dla wersji 1.0.0.

## Skróty źródeł

| Skrót | Repozytorium | Licencja |
|---|---|---|
| blader | [blader/humanizer](https://github.com/blader/humanizer) 2.9.1 | MIT, © 2025 Siqi Chen |
| pielas | [pielas-activy/humanizer-pl](https://github.com/pielas-activy/humanizer-pl) | MIT, © 2026 Igor Pielas |
| paszkiewicz | [paszkiewiczmichal/claude-skills-pl](https://github.com/paszkiewiczmichal/claude-skills-pl) | MIT, © 2026 paszkiewiczmichal |
| 0x00 | [0x00-Crashes/humanizer-pl](https://github.com/0x00-Crashes/humanizer-pl) | brak pliku licencyjnego |
| wikipedia | [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | CC BY-SA 4.0 |
| web | polskie publikacje o GPT-izmach – linki w README | – |

## Formy zapożyczenia

- **cytat** – fragment cudzego tekstu przejęty w brzmieniu albo blisko brzmienia. Wymaga licencji zezwalającej i wiersza w tym pliku. U nas dotyczy wyłącznie list sygnałów i tabel zamienników, czyli słowników fraz.
- **adaptacja** – przepisane własnymi słowami, ale rozpoznawalnie z tego źródła: ten sam podział, ta sama kolejność albo ten sam chwyt techniczny.
- **koncepcja** – przejęty sam pomysł na to, co warto robić. Sformułowania, przykłady i struktura własne.
- **odesłanie bibliograficzne** – cudzą publikację poznaliśmy za pośrednictwem innego projektu. Cytujemy ją samodzielnie, ale wypada powiedzieć, kto na nią naprowadził.

## Metoda weryfikacji

Zbieżność mierzona wspólnymi ciągami ośmiowyrazowymi, po usunięciu adresów URL. Bez tego kroku wspólne zacytowanie tej samej strony Wikipedii daje fałszywe trafienia na każde źródło naraz.

| Źródło | Pliki skilla (`SKILL.md`, `references/`) | Dokumentacja | Charakter trafień |
|---|---|---|---|
| 0x00 | 0 | 4 | tytuł cytowanej publikacji naukowej, przywoływanej też przez tamten projekt |
| blader | 0 | 0 | struktura przejęta, język w całości własny |
| pielas | 8 | 4 | wyłącznie listy sygnałów i tabele zamienników, wszystkie wymienione niżej |
| paszkiewicz | 6 | 3 | jak wyżej |

Trafienia w dokumentacji nie są osobnym zapożyczeniem: to te same cytaty, które wymieniają tabele poniżej, przytoczone jeszcze raz po to, żeby je nazwać. Sformułowanie „od X po Y, gdy X i Y nie są skalą” stoi w wierszu o wzorcu 12, markery zdania wielowarunkowego w wierszu o wyjątku prawniczym, a artefakt rozmowy z asystentem w tabeli wzorca 20 w README. Reprodukcji tekstu licencji MIT w `NOTICE.md` też nie liczymy: to wymóg samej licencji, nie ślad zapożyczenia.

## blader/humanizer – szkielet

| Mechanizm | Plik źródłowy | Forma | Gdzie u nas |
|---|---|---|---|
| Podział wzorców 1–33 na sześć kategorii i ich kolejność | `SKILL.md` | koncepcja | `references/wzorce-pl.md`, kategorie I–VI |
| Pętla szkic → audyt → wersja finalna, z pytaniem audytowym postawionym wprost | `SKILL.md` (Process and Output) | koncepcja | `SKILL.md`, sekcja „Proces” |
| Trzy tryby wywołania: tekst wklejony, plik, tryb osadzony | `SKILL.md` (Invocation Modes) | koncepcja | `SKILL.md`, sekcja „Tryby wywołania” |
| Kalibracja głosu: próbka autora nadpisuje reguły stylistyczne skilla | `SKILL.md` (Voice Calibration) | koncepcja | `SKILL.md`, sekcja „Kalibracja głosu” |
| Sekcje „czego nie flagować” i „oznaki ludzkiego tekstu”, zasada skupisk | `SKILL.md` (Detection Guidance) | koncepcja, pozycje polskie dopisane od zera | `references/wzorce-pl.md` |
| Zasada: przeżywa informacja, nie kształt tekstu | `SKILL.md` pkt 2 | koncepcja | `SKILL.md`, zasada 4 oraz hamulec długości |
| Teza, że tekst pozbawiony głosu zdradza maszynę tak samo jak sztampa | `SKILL.md` (PERSONALITY AND SOUL) | koncepcja, sformułowania i przykłady własne | `SKILL.md`, sekcja „Głos i charakter” |
| Granica: opinia jest głosem, fakt dopisany od siebie jest fabrykacją | `SKILL.md` pkt 3 | koncepcja, spięta u nas z audytem semantycznym | `SKILL.md`, sekcja „Głos i charakter” |
| Układ README: instalacja, użycie, tabela wzorców | `README.md` | adaptacja | `README.md` |

## paszkiewiczmichal/claude-skills-pl – polskie brzmienia i wyjątek prawniczy

| Mechanizm | Plik źródłowy | Forma | Gdzie u nas |
|---|---|---|---|
| Polskie nazwy wzorców 1–33 i pola semantyczne słów na celowniku | `skills/humanizer-pl/SKILL.md` | adaptacja | `references/wzorce-pl.md` |
| Wyjątek prawniczy: pięć reguł zawieszonych i osiem obowiązujących zawsze | tamże, L41–77 | adaptacja, podział przejęty wprost | `SKILL.md`, sekcja wyjątku |
| Markery zdania wielowarunkowego: „z zastrzeżeniem”, „chyba że”, „o ile”, „pod warunkiem że” | tamże, L61 | **cytat** (lista czterech zwrotów) | `SKILL.md`, sekcja wyjątku |
| Tabela wypełniaczy i ich zamienników | tamże, §23 | **cytat** (lista zamienników) | `references/wzorce-pl.md`, wzorzec 23 |
| Artefakty rozmowy z asystentem | tamże, §20 | **cytat** (lista sygnałów) | `references/wzorce-pl.md`, wzorzec 20; przykład w `references/przyklady.md` |
| Tło normatywne kresek: dywiz ortograficzny, półpauza w zakresach, pauza jako znak interpunkcyjny | tamże, §14 | koncepcja, rozwinięta samodzielnie | `references/typografia.md` |
| Tło normatywne cudzysłowów pierwszego i drugiego stopnia | tamże, §19 | koncepcja, rozwinięta samodzielnie | `references/typografia.md` |
| Zastąpienie angielskich złożeń z łącznikiem polskimi anglicyzmami i kalkami | tamże, §26 | koncepcja, przykłady własne | `references/wzorce-pl.md`, wzorzec 26 |
| Uwaga, że formy nieosobowe na -no oraz -to są poprawne | tamże, §13 | koncepcja | `references/wzorce-pl.md`, wzorzec 13 |
| Układ manifestu wtyczki | `.claude-plugin/plugin.json` | adaptacja struktury, własne dane | `.claude-plugin/plugin.json` |

## pielas-activy/humanizer-pl – router, polszczyzna i testy

| Mechanizm | Plik źródłowy | Forma | Gdzie u nas |
|---|---|---|---|
| Rozpoznanie języka po diakrytykach i słowach funkcyjnych, ładowanie tylko potrzebnych referencji, płaska struktura katalogu | `SKILL.md` (krok 0) | koncepcja | `SKILL.md`, sekcje zakresu i kroku 0 |
| Format opisu wzorca jako para sygnał → akcja | `references/patterns-pl.md` | koncepcja | `references/wzorce-pl.md` |
| Polszczyzna jako osobny, drugi przebieg po usunięciu śladów | `references/polszczyzna-pl.md` | koncepcja | `references/polszczyzna.md` |
| Skan kalek prowadzony testem, nie listą: odwrotne tłumaczenie, prostsze polskie słowo, rejestr | tamże, sekcja „Skan kalek” | adaptacja | `references/polszczyzna.md`, sekcja 8; wzorzec 35 |
| Tabela kalek leksykalnych | `references/polszczyzna-pl.md` oraz `SKILL.md:100` | **cytat** (lista; kolejność przestawiona, glosy skrócone) | `references/polszczyzna.md`; wzorzec 26 |
| Parataksa i hipotaksa jako główna poprawka polskiego rytmu | `references/polszczyzna-pl.md`, sekcja 5 | koncepcja, przykłady własne | `references/polszczyzna.md`, sekcja 5; wzorzec 36 |
| Ukryty „nie X, to Y” z czasownikiem osobowym | tamże, sekcja 4 | koncepcja, przykłady własne | `references/polszczyzna.md`, sekcja 4 |
| Wymóg czasownika osobowego, przymiotnik na froncie, urwany dopełniacz | tamże, sekcja 2 | koncepcja, przykłady własne | `references/polszczyzna.md`, sekcja 2 |
| Kalki-przymiotniki rozwijane w zdanie względne | tamże, sekcja 3 | koncepcja, przykłady własne | `references/polszczyzna.md`, sekcja 3 |
| Doklejone negacje jako sygnał | `references/patterns-pl.md`, kat. 3 | **cytat** (lista sygnałów) | `references/wzorce-pl.md`, wzorzec 9 |
| Fałszywe zakresy: sformułowanie „od X po Y”, gdy X i Y nie są skalą | `references/patterns-pl.md:120` | **cytat** | `references/wzorce-pl.md`, wzorzec 12 |
| Głębokość ingerencji: powtórzenie jest śladem, zaczynaj od twierdzenia, ochrona konkretu, sprawdzian na różnicy | `SKILL.md` | adaptacja | `SKILL.md`, sekcja „Głębokość ingerencji” |
| Twarde zasady wyjścia: pierwszy wiersz bez wypełniacza, wyjście nie dłuższe od wejścia, zachowane diakrytyki, brak zmiany języka | `SKILL.md` | koncepcja | `SKILL.md`; asercje `first_line_not_filler`, `length_ratio`, `pl_diacritics` |
| Profil żargonu w pliku `*.local.md`, poza repozytorium, chroniony we wszystkich przebiegach | `SKILL.md` (tryb opcjonalny) | koncepcja | `SKILL.md`, sekcja „Profil lokalny”; `.gitignore` |
| Wniosek z praktyki: kalki przeżywają pierwszy przebieg, bo są poprawne gramatycznie | `SKILL.md` (Learnings) | koncepcja | `references/polszczyzna.md` |
| Testy bez wywołania modelu: zamrożona para wejście–wyjście w JSON-ie, asercje binarne liczone deterministycznie | `evals/run_evals.py`, `evals/evals.json` | adaptacja koncepcji, kod napisany od nowa | `evals/run_evals.py` |
| Mapa `expect` przy przypadku i porównanie wyniku z oczekiwaniem | `evals/run_evals.py` | adaptacja | `evals/run_evals.py`, `run_case` |
| Zapis znaków typograficznych escape'ami, żeby konfiguracja była wolna od glifów | `evals/evals.json` | adaptacja | `evals/evals.json`, sekcja wzorców |
| Zestaw asercji wyjściowych | `evals/evals.json` | adaptacja z poprawkami (niżej) | `evals/evals.json` |

### Co poprawiliśmy względem źródła

Pięć wad zestawu testowego repoB naprawionych w naszej wersji. Wymieniamy je, żeby słowo „adaptacja” nie brzmiało jak przepisanie:

1. **Dopasowanie podciągów zastąpione rdzeniem z granicą wyrazu.** Źródło szukało zwykłego podciągu, więc `dedykowany` nie łapał form odmienionych, a każdy zakazany ciąg trafiał też w środek dłuższego wyrazu.
2. **Obsługa fleksji.** Zamiast osobnych wpisów na każdą formę jeden rdzeń pokrywa cały paradygmat.
3. **Sztywny limit długości zastąpiony stosunkiem.** Wymóg, żeby wyjście nie było dłuższe od wejścia co do znaku, wywracał się na tekstach, w których poprawna redakcja rozwija skrót albo dopisuje brakujący podmiot.
4. **Zakaz półpauzy zastąpiony regułą normatywną.** Źródło zakazywało półpauzy razem z pauzą, co jest błędem: w polszczyźnie półpauza jest poprawna w zakresach liczbowych i jako pauza zdaniowa ze spacjami.
5. **Jeden język zamiast dwóch.** Konfiguracja jest jednojęzyczna, zgodnie z zakresem skilla.

## 0x00-Crashes/humanizer-pl – wyłącznie idee

Repozytorium bez pliku licencyjnego, więc żaden fragment tekstu nie mógł zostać przejęty. Wszystkie pozycje mają formę „koncepcja”, a wynik potwierdza pomiar: zero wspólnych ciągów ośmiowyrazowych w plikach skilla.

| Mechanizm | Plik źródłowy | Co zrobiliśmy inaczej | Gdzie u nas |
|---|---|---|---|
| Rozpoznanie gatunku jako pierwszy, obowiązkowy krok wraz z mapą gatunków | `SKILL.md` L50–95 | tabela napisana od zera, własne nazwy kolumn, dołożony gatunek „pismo urzędowe” i sekcja „Skala swobody” | `references/gatunki.md` |
| Raport rozpoznania gatunku jednym zdaniem na początku odpowiedzi | `SKILL.md` L87–93 | własne brzmienie i własny przykład | `SKILL.md`, sekcja rozpoznania |
| Polskie GPT-izmy porządkowane funkcją w tekście oraz kondensacja jako właściwy sygnał | `SKILL.md` L421–458 | własne listy zwrotów, własny przykład, sygnał opisany jako regularny rozstaw plus zagęszczenie | `references/wzorce-pl.md`, wzorzec 34 |
| Błędy fleksyjne modeli: liczebnik nieokreślony, aspekt, rekcja przyimkowa, odmiana nazw własnych i skrótowców | `SKILL.md` L504–527 | własne przykłady i własne sformułowania reguł | `references/wzorce-pl.md`, wzorzec 38 |
| Audyt semantyczny: procedura, klasy twierdzeń, tabela porównawcza, werdykt, katalog pułapek | `SKILL.md` L554–663 | statusy słowne zamiast emoji, własny przykład, dołożona ósma pułapka i sekcja „czego audyt nie robi” | `references/audyt-semantyczny.md` |
| Zasada: wierność znaczeniu ważniejsza od czystości redakcji | `SKILL.md` L589 | własne brzmienie | `SKILL.md`, zasada 3 |
| Drobne ślady typograficzne: hasztagi wielbłądzie, wielka litera po dwukropku | `SKILL.md` L498–502 | własne brzmienie, dołożone zastrzeżenie o czytnikach ekranu | `references/wzorce-pl.md`, wzorzec 41 |
| Pozycja bibliograficzna: Mazur (2024) | `README.md`, `SKILL.md` | publikację cytujemy samodzielnie | odesłanie bibliograficzne; `README.md`, sekcja źródeł |

## Wikipedia: Signs of AI writing

| Mechanizm | Źródło | Forma | Gdzie u nas |
|---|---|---|---|
| Wyjaśnienie, dlaczego modele produkują uśredniony styl | strona `Wikipedia:Signs_of_AI_writing`, WikiProject AI Cleanup | parafraza własnymi słowami wraz z odnośnikiem | akapit wstępny `references/wzorce-pl.md` |

Żaden fragment tej strony nie został przeniesiony w brzmieniu ani przetłumaczony: akapit napisaliśmy samodzielnie, przejmując obserwację, a nie sposób jej wyrażenia. Zdanie o algorytmach statystycznych, które blader cytuje dosłownie, u nas nie występuje w żadnej postaci. Odnośnik do źródła stoi przy akapicie, zgodnie z wymogiem atrybucji.

## Warstwa inżynieryjna

| Mechanizm | Źródło | Forma | Gdzie u nas |
|---|---|---|---|
| Walidacja frontmattera wyrażeniem regularnym zamiast parsera YAML, bez zależności | blader → `scripts/validate-package.py` | adaptacja: inny zestaw pól | `scripts/validate.py`, `check_skill_frontmatter` |
| Zakaz kluczy nieprzenośnych we frontmatterze | tamże | adaptacja: lista rozszerzona o `version` na poziomie głównym | `scripts/validate.py`, `FORBIDDEN_FRONTMATTER_KEYS` |
| Synchronizacja numeru wersji między manifestami | tamże | adaptacja: źródłem także `CHANGELOG.md`, raport zbiorczy zamiast przerwania na pierwszym rozjeździe | `scripts/validate.py`, `check_versions` |
| Kontrola ciągłości numeracji wzorców | tamże | adaptacja: 41 zamiast 33, źródłem plik referencyjny | `scripts/validate.py`, `check_pattern_numbering` |
| Budżet linii pliku jako twarda bramka | tamże | adaptacja: tabela budżetów per plik zamiast jednego progu | `scripts/validate.py`, `LINE_BUDGETS` |
| Układ manifestu wtyczki i katalogu wtyczek | blader → `.claude-plugin/*.json` | adaptacja struktury, własne dane | `.claude-plugin/*.json` |
| Trójstopniowy workflow CI: walidator, `skills add --list`, `plugin validate` | blader → `.github/workflows/validate.yml` | adaptacja: nazwy kroków po polsku, walidator w trybie ścisłym | `.github/workflows/validate.yml` |

## Praca własna

Bez źródła zewnętrznego, odnotowane dla porządku:

- **Rozstrzygnięcie kolizji słownictwa modelu z terminologią ustawową** w rejestrze prawniczym. Żadne ze źródeł tego problemu nie podnosi; powstało z ustaleń przeglądu wewnętrznego.
- **Podział zakazanych rdzeni na twarde i miękkie**, z limitem gęstości dla tych drugich. Bez tego zakaz odrzucał poprawne teksty fachowe i prawnicze, w których „umowa kompleksowa” albo „personel kluczowy” są terminami, nie ozdobnikami.
- **Kontrola cudzysłowów rozpoznająca polską parę** zamiast prostego zakazu znaków, który odrzucałby poprawny polski cudzysłów zamykający.
- **Dopuszczenie myślnika em w zapisie dialogu** zamiast zakazu bezwarunkowego.
- **Składanie diakrytyków bramkowane stanem wejścia**, potrzebne dla tekstów pisanych bez ogonków.
- **Blok pięciu przypadków regresyjnych** pilnujących mechanizmów, których zestaw dobrych tekstów nie jest w stanie upilnować, wraz z kontrolą wstępną wykrywającą osierocone oczekiwania w rejestrze asercji.
- **Weryfikacja zestawu testowego metodą mutacyjną**: zamiast pytać, czy kontrola działa dziś, psujemy mechanizm w kopii i sprawdzamy, czy zestaw to zauważy. Ta metoda wyciągnęła dwie rzeczy, których przegląd stanu nie pokazał: ślepotę asercji nieobecności na własne uszkodzenie oraz lukę w spójności rejestru. Opis dla kontrybutorów w [CONTRIBUTING.md](CONTRIBUTING.md).
- **Kontrola typografii własnej dokumentacji** w walidatorze, mierząca README, NOTICE, CREDITS i CHANGELOG tą samą miarą, którą skill przykłada do cudzych tekstów.
