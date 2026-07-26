# Jak współtworzyć

Skill jest plikiem tekstowym, więc próg wejścia jest niski, a ryzyko cichej regresji wysokie: zmiana jednego zdania w regule potrafi przestawić zachowanie w tekstach, o których nikt nie pomyślał. Stąd kilka zasad.

## Dwie bramki przed wysłaniem zmiany

```bash
python3 scripts/validate.py --strict
python3 evals/run_evals.py
```

Walidator sprawdza frontmatter skilla, zgodność numeru wersji między `SKILL.md`, manifestem wtyczki i `CHANGELOG.md`, ciągłość numeracji wzorców, budżety linii, obecność wpisu na profile lokalne w `.gitignore` oraz typografię własnej dokumentacji. Zestaw testowy sprawdza zamrożone pary wejście–wyjście. Obie komendy muszą kończyć się kodem zero. To samo uruchamia CI, więc lepiej dowiedzieć się lokalnie.

## Budżety linii

Każdy plik referencyjny ma twardy limit: `SKILL.md` 250 wierszy, `wzorce-pl.md` 550, `przyklady.md` 300, `polszczyzna.md` 200, `audyt-semantyczny.md` 150, `typografia.md` 140, `gatunki.md` 120. Limit nie jest kaprysem: całość ląduje w kontekście modelu przy każdym wywołaniu, a plik, który spuchł, wypycha z uwagi to, co ważne. Chcesz dopisać akapit, a budżet jest wyczerpany? Poszukaj, co skreślić.

## Dogfooding

Dokumentacja tego projektu podlega tej samej normie, którą skill narzuca cudzym tekstom, a walidator to sprawdza. W praktyce: cudzysłowy „…” domykane właściwym znakiem, półpauza ze spacjami zamiast myślnika em, zero emoji, nagłówki bez wersalików w każdym wyrazie. Eksponat łamiący normę jest dozwolony wyłącznie w bloku kodu albo w cytacie blokowym – kontrola maskuje te dwa konteksty, więc przykład usterki postawiony w zwykłym akapicie zapali się jako usterka.

## Strażnicy asercji

Najważniejsza reguła w tym repozytorium i jedyna, która wyszła z pomyłki popełnionej w trakcie budowy.

**Problem.** Asercja pilnująca nieobecności zjawiska – brak emoji, brak angielskiego cudzysłowu, brak myślnika em – nie może zostać sprawdzona przez poprawne wyjście, bo poprawne wyjście z definicji tego zjawiska nie zawiera. Można więc usunąć całą asercję z rejestru albo zepsuć jej mechanizm, a zestaw nadal świeci na zielono. Testy milczą dokładnie wtedy, gdy powinny krzyczeć.

**Reguła.** Dodajesz asercję sprawdzającą nieobecność? Dodaj do niej strażnika w tym samym commicie i sprawdź go mutacją: usuń asercję z rejestru albo zepsuj mechanizm w kopii i upewnij się, że zestaw pada. Jeżeli nie pada, strażnika nie ma, choćby przypadek wyglądał na powiązany.

### Trzy przypadki, w kolejności preferencji

**1. Przypadek na progu tolerancji.** Wyjście jest poprawne i siedzi dokładnie na granicy, którą próg przepuszcza. Tak działa `regresja_prog_tolerancji_gestosci`: ma w wyjściu dwa miękkie rdzenie, czyli tyle, ile przepuszcza próg. Zestaw przechodzi, a zniesienie progu wypycha gęstość ponad limit i przypadek pada. Zaleta jest taka, że do zestawu nie wchodzi ani jeden przykład wadliwej redakcji, więc nikt, kto uczy się z zestawu, nie zobaczy złego wzorca.

**2. Przypadek z `expect: false`.** Konieczny tam, gdzie mechanizm nie ma progu, tylko wykrywa obecność. Wyjście jest celowo wadliwe, a mapa `expect` deklaruje, że wskazana asercja ma paść. Koszt: w zestawie ląduje przykład, którego nie wolno naśladować. Dlatego takie przypadki oznaczamy prefiksem `regresja_`, polem `kind` i notą przy zestawie.

**3. Mechanizm, którego nie da się upilnować.** Zdarza się. Wtedy zamiast udawać pokrycie, opisz w komentarzu przy asercji, dlaczego strażnik jest niemożliwy, i dołóż dowód: wynik mutacji pokazujący, że żaden dostępny kształt przypadku nie wykrywa uszkodzenia. Udokumentowana luka jest uczciwa, luka zamaskowana przypadkiem, który niczego nie pilnuje, jest gorsza niż jej brak.

### Pułapka samego testu mutacyjnego

Łatka nałożona na kod, która nie trafi – bo w międzyczasie zmieniono nazwę zmiennej albo funkcji – daje fałszywą lukę i wygląda identycznie jak prawdziwa. To się w tym projekcie zdarzyło: zgłoszono niepokrytą gałąź, która była pokryta, bo łatka celowała w nieistniejącą już nazwę. Każda łatka musi więc weryfikować, że faktycznie coś podmieniła, i zgłaszać brak trafienia jako błąd metody, a nie jako lukę pokrycia.

## Zestaw wzorcowy jest zamrożony

Pary wejście–wyjście w `evals/evals.json` powstały w osobnej fazie i zostały zamrożone. Otwiera się je wyłącznie z powodu klasy bloker: udowodniona wada mechanizmu, błąd normatywny w regule albo fałszywy alarm na poprawnym tekście. Wygodna zmiana przypadku, żeby przepuścił nową regułę, jest dokładnie tym, przed czym zestaw ma chronić – jeżeli reguła i przypadek się kłócą, najpierw rozstrzygnij, które z nich ma rację.

## Atrybucja

Ten projekt korzysta z pracy czterech innych repozytoriów i pilnuje, żeby to było widać. Bierzesz skądś sformułowanie, listę albo strukturę? Dopisz wiersz do [CREDITS.md](CREDITS.md) w tym samym commicie: mechanizm, plik źródłowy, forma zapożyczenia, miejsce u nas. Jeżeli źródło ma licencję, jego nota trafia do [NOTICE.md](NOTICE.md) w pełnym brzmieniu. Jeżeli nie ma licencji, wolno przejąć wyłącznie pomysł i trzeba go napisać od zera – sprawdzanym kryterium jest brak wspólnych ciągów ośmiowyrazowych.
