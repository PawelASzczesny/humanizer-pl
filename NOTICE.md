# Noty licencyjne źródeł

Ten plik zbiera noty licencyjne projektów, z których `humanizer-pl` przejął fragmenty tekstu, strukturę albo pomysły. Licencja MIT wymaga, żeby nota o prawach autorskich i treść zezwolenia wędrowały dalej razem z oprogramowaniem, więc reprodukujemy je tutaj w pełnym brzmieniu – mapa „który mechanizm skąd pochodzi” jest w [CREDITS.md](CREDITS.md).

Sam `humanizer-pl` jest wydany na licencji MIT, copyright © 2026 Paweł Szczęsny – patrz [LICENSE](LICENSE).

---

## blader/humanizer

- Repozytorium: https://github.com/blader/humanizer
- Wersja przejrzana: 2.9.1 (commit `523374d`, 2026-07-21)
- Licencja: MIT
- Zakres wykorzystania: szkielet katalogu wzorców (33 pozycje w oryginale) z podziałem na kategorie, przebieg pracy szkic → audyt → wersja finalna, trzy tryby wywołania, kalibracja głosu z próbki autora, zasada zerowej fabrykacji oraz układ pakietu, czyli manifest wtyczki, walidator i workflow CI. Wszystko w formie koncepcji i adaptacji: pomiar zbieżności tekstowej daje zero wspólnych ciągów ośmiowyrazowych. Szczegóły w [CREDITS.md](CREDITS.md).

```text
MIT License

Copyright (c) 2025 Siqi Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## pielas-activy/humanizer-pl

- Repozytorium: https://github.com/pielas-activy/humanizer-pl
- Wersja przejrzana: commit `446d0d4` (2026-06-15)
- Licencja: MIT, copyright © 2026 Igor Pielas
- Zakres wykorzystania: rozpoznanie języka jako krok zerowy, polszczyzna jako osobny przebieg po usunięciu śladów, reguła głębokości ingerencji, profil żargonu użytkownika oraz pomysł na testy bez wywołania modelu. Cytowane w brzmieniu: tabela kalek leksykalnych i dwie listy sygnałów (doklejone negacje, fałszywe zakresy). Szczegóły w [CREDITS.md](CREDITS.md).

Plik `LICENSE` tego projektu zawiera – poza kanonicznym tekstem MIT – dodatkowy akapit opisujący relację do projektu `blader/humanizer`. Reprodukujemy całość dosłownie, bez skrótów:

```text
MIT License

Copyright (c) 2026 Igor Pielas

This project is a fork of and builds on "humanizer" by blader
(https://github.com/blader/humanizer), which is also MIT licensed. The English
patterns in references/patterns-en.md are reproduced 1:1 from blader/humanizer.
All Polish-language layers (patterns-pl.md, polszczyzna-pl.md), the Bielik
integration, the evals harness and the documentation are additions.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Uwaga dla osób czytających ten plik jako wzór: w `humanizer-pl` atrybucja celowo nie trafiła do `LICENSE`, tylko tutaj. Dopisek w środku tekstu licencji zaburza automatyczne rozpoznawanie licencji przez GitHub i utrudnia maszynową analizę zgodności – nota o pochodzeniu należy do `NOTICE.md`, a nie do `LICENSE`.

---

## paszkiewiczmichal/claude-skills-pl

- Repozytorium: https://github.com/paszkiewiczmichal/claude-skills-pl
- Wersja przejrzana: commit `83ce91c` (2026-06-14)
- Licencja: MIT, copyright © 2026 paszkiewiczmichal (Michał Paszkiewicz, radca prawny)
- Zakres wykorzystania: polskie nazwy wzorców w kategoriach I–VI, tło normatywne typografii (myślnik, półpauza, dywiz, cudzysłowy obu stopni), wyjątek dla rejestru prawniczego wraz z podziałem na reguły zawieszone i obowiązujące oraz układ manifestu wtyczki. Cytowane w brzmieniu: markery zdania wielowarunkowego, tabela wypełniaczy z zamiennikami i lista artefaktów rozmowy z asystentem. Szczegóły w [CREDITS.md](CREDITS.md).

```text
MIT License

Copyright (c) 2026 paszkiewiczmichal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 0x00-Crashes/humanizer-pl

- Repozytorium: https://github.com/0x00-Crashes/humanizer-pl
- Wersja przejrzana: commit `b0851fa` (2026-05-18)
- Licencja: brak pliku licencyjnego w repozytorium (stan na 2026-07-25)

Z tego projektu zapożyczyliśmy wyłącznie koncepcje: rozpoznanie gatunku tekstu przed redakcją, audyt semantyczny jako osobny przebieg po redakcji oraz pomysł na katalog błędów fleksyjnych typowych dla modeli językowych w polszczyźnie. Ponieważ repozytorium nie ma licencji, mechanizmy napisaliśmy od zera własnym językiem, a wynik sprawdziliśmy maszynowo, szukając wspólnych ciągów ośmiowyrazowych. W plikach samego skilla, czyli w `SKILL.md` i w katalogu `references/`, nie ma ani jednego takiego ciągu. W tej dokumentacji pokrywają się rzeczy z natury wspólne: nazwy własne oraz tytuł publikacji naukowej, którą oba projekty przywołują w bibliografii. Nie ma tu więc noty licencyjnej do reprodukcji, jest za to wdzięczność i wskazanie inspiracji.

Test maszynowy nie rozstrzyga jednak wszystkiego. Jeśli autor tego projektu uzna, że którykolwiek fragment `humanizer-pl` przypomina jego pracę bardziej, niż powinien – prosimy o zgłoszenie w issue. Poprawimy albo usuniemy.

---

## Wikipedia: Signs of AI writing

Pierwotnym katalogiem oznak pisania AI, na którym opiera się `blader/humanizer`, jest wikipedyczny przewodnik [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Prowadzi go grupa redakcyjna [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup), a całość udostępniono na licencji CC BY-SA 4.0. `humanizer-pl` przejmuje stamtąd obserwacje i klasyfikację zjawisk, nie tekst – wszystkie opisy wzorców są napisane po polsku od zera. Jedyne miejsce, w którym idzie za tą stroną wprost, to akapit wstępny `references/wzorce-pl.md`, wyjaśniający, skąd bierze się uśredniony styl modeli. Napisaliśmy go samodzielnie, nie tłumacząc ani nie przenosząc żadnego zdania ze strony źródłowej – przejęta została obserwacja, nie sposób jej wyrażenia. Odnośnik do źródła stoi przy akapicie.
