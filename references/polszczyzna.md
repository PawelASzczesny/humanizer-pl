# Polszczyzna: drugi przebieg

Ten przebieg robisz **po** usunięciu śladów modelu, na gotowym tekście. Ma inny cel niż pierwszy: tam chodziło o to, żeby tekst przestał brzmieć jak wygenerowany, tutaj o to, żeby brzmiał jak napisany po polsku, a nie przetłumaczony z angielskiego. Ślady z pierwszego przebiegu widać gołym okiem. To, co poprawiasz teraz, jest gramatycznie poprawne i właśnie dlatego prześlizguje się przez zwykłe czytanie.

Zasada nadrzędna: sens, fakty i głos autora zostają. Czyścisz leniwe kalki i nienaturalny szyk, nie żargon i nie osobiste dziwactwa.

Osiem ruchów. Ostatni jest osobnym skanem i robisz go na końcu.

## 1. Anglicyzmy: tłumacz leniwe, zostaw żargon

Decyzja zapada przy każdym słowie osobno.

| Zostaw | Przetłumacz |
|---|---|
| żargon zawodowy autora, niezależnie od branży (medycyna, prawo, finanse, gastronomia, sport) | feedback → informacja zwrotna, uwagi |
| nazwy własne, marki, nazwy produktów i systemów | deadline → termin |
| terminy bez dobrego polskiego odpowiednika | insight → wniosek, spostrzeżenie |
| słowo, które wraca w tekście jako świadomy motyw | output (ogólnie) → wynik, efekt |
| terminy zdefiniowane w normie, umowie albo przepisie | supply → podaż |

Uważaj na pseudopolszczyznę, czyli spolszczony angielski udający tłumaczenie. „Kuracja” w znaczeniu doboru treści brzmi gorzej niż oryginał; polskie słowo to selekcja albo wybór. Gdy nie wiesz, czy masz do czynienia z żargonem autora, sprawdź, czy termin wraca w tekście świadomie. Jeśli wraca, zostaw.

Terminy z pliku `*.local.md` są chronione bezwarunkowo i nie podlegają tej decyzji.

## 2. Każde zdanie ma czasownik osobowy

Polski slop kalkuje angielski szyk i zostawia zdania bez orzeczenia albo z orzecznikiem wypchniętym na początek.

- Przymiotnik na froncie: „Najcenniejsza w sieci jest Twoja sytuacja.” → „W sieci najcenniejsza jest twoja sytuacja.”
- Równoważnik bez czasownika: „Świetny pomysł. I zupełnie niewykonalny.” → „Pomysł jest świetny, ale zupełnie niewykonalny.”
- Urwany dopełniacz: „Od pierwszego dnia z konsultantem obok.” → scal z poprzednim zdaniem (patrz ruch 5).

Wyjątek: jeden świadomy równoważnik dla emfazy zostaje („No i tyle.”). Ślad to seria, nie pojedynczy przypadek. Lista wypunktowana bez orzeczeń jest normalną listą, nie usterką.

## 3. Rozwiń kalki-przymiotniki

W angielszczyźnie znaczenie chowa się w przymiotniku. Polszczyzna rozkłada je na zdanie podrzędne albo wyrażenie z przyimkiem.

- „kompetencje przyszłościowe” → „kompetencje przydatne w przyszłości”
- „treści generowane AI” → „treści generowane przez AI”
- „podejście danocentryczne” → „podejście oparte na danych”

Reguła: rzeczownik plus sztuczny przymiotnik ukuty z angielskiego rozwijasz w konstrukcję z „który”, „przez”, „do” albo „z”.

## 4. Ukryty „nie X, to Y”

Ten sam paralelizm przeczący co we wzorcu 9, ale z czasownikiem, więc łatwo go przeoczyć. Schemat brzmi „Nie robię X, robię Y”.

- „Nie liczymy godzin, liczymy wynik.” → „Liczymy wynik, nie godziny.”
- „To nie jest szkolenie z narzędzi, to szkolenie z decyzji.” → „To szkolenie dotyczy decyzji, nie narzędzi.”

Najgorsza odmiana to dwa urywane zdania obok siebie. Problemem jest wtedy nie sam kontrast, lecz jego posiekana forma; leczy ją scalenie w zdanie złożone. Jedno wystąpienie na tekst może zostać.

## 5. Parataksa → hipotaksa

Najsilniejszy polski ślad, którego pierwszy przebieg nie łapie. Model sieka treść na krótkie, osobne zdania, bo tak wyglądają jego angielskie wzorce. Polszczyzna znacznie częściej buduje zdanie złożone.

- „Wdrożenie trwało trzy miesiące. Prowadził je zespół z dwóch działów.” → „Wdrożenie, które prowadził zespół z dwóch działów, trwało trzy miesiące.”
- „Zmieniliśmy dostawcę. Poprzedni spóźniał się z dostawami.” → „Zmieniliśmy dostawcę, który spóźniał się z dostawami.”

Szukaj sąsiadów, których łączy „bo”, „więc”, „ale”, „choć”, „który”, i połącz je tym spójnikiem. Spójnika przyczynowego nie dokładasz na siłę: jeżeli w oryginale były trzy niezależne zdania, scalenie ma je połączyć, a nie orzec, że jedno wynika z drugiego (pułapka 6 w `audyt-semantyczny.md`). Nie scalaj wszystkiego w jedno olbrzymie zdanie: jedno krótkie zdanie dla podkreślenia myśli jest dobre, a w dokumentacji technicznej krótkie kroki są wręcz wymagane.

## 6. Szyk i akcent zdaniowy

Polski ma szyk swobodny i wykorzystuje go do rozłożenia akcentu: informacja nowa idzie zwykle na koniec zdania. Model trzyma się sztywnego układu podmiot, orzeczenie, dopełnienie i przez to gubi ten akcent.

- Poprzednie zdanie pyta „kto to zrobił?”: „Dział finansowy przygotował ten raport.” → „Ten raport przygotował dział finansowy.”
- Poprzednie zdanie pyta „kiedy?”: „W marcu ruszyła nowa wersja.” → „Nowa wersja ruszyła w marcu.”

Nie przestawiaj szyku odruchowo. Zmieniasz go tylko wtedy, gdy zdanie odpowiada na pytanie postawione wcześniej, a odpowiedź stoi w środku zamiast na końcu.

## 7. Zaimki: „swój” i nadmiar „twojego”

Dwie kalki, które w polszczyźnie brzmią obco, a w angielszczyźnie są normą.

- Zaimek dzierżawczy zamiast zwrotnego: „Autor przedstawił jego wnioski” (czyje?) → „Autor przedstawił swoje wnioski”.
- Nadmiar drugiej osoby przeniesiony z „your”: „Twój zespół, Twoje procesy i Twoje dane” → „zespół, procesy i dane” albo jedno „twój” na akapit.
- Zaimek tam, gdzie wystarczy odmiana: „On powiedział, że on przyjdzie” → „Powiedział, że przyjdzie”.

Wielką literę w „Twój” zostawiasz tylko w bezpośrednim zwrocie do adresata (list, mail). W tekście marketingowym to konwencja autora, nie usterka.

## 8. Skan kalek: test, nie lista

Robisz go osobno, na samym końcu, jednym przejściem przez tekst. Kalki są poprawne gramatycznie, więc przy zwykłym czytaniu oko się po nich prześlizguje. Żadna lista ich nie zamknie, dlatego pracujesz testem.

Trzy pytania do każdej podejrzanej frazy:

1. **Odwrotne tłumaczenie.** Przełóż frazę dosłownie na angielski. Kalkę poznasz po tym, że przekład daje zgrabny, częsty zwrot angielski: „na ten moment” wraca jako „at this point”, a „nie robi sensu” jako „does not make sense”.
2. **Prostsze polskie słowo.** Obcy rdzeń (finalnie, definitywnie, implementować, adresować, dedykowany) niemal zawsze da się oddać zwyklejszym polskim wyrazem. Jeśli nic przy tym nie tracisz, wybierz polski.
3. **Rejestr.** Czy to brzmi jak slajd z prezentacji, czy jak zdanie wypowiedziane przez człowieka? Korpomowę bez potrzeby upraszczasz.

Lista poniżej jest ziarnem do kalibracji ucha, nie zbiorem zamkniętym:

| Kalka | Po polsku |
|---|---|
| dedykowany | osobny, przeznaczony dla |
| adresować problem | zająć się czymś |
| w oparciu o, bazować na | na podstawie |
| kluczowy interesariusz | decydent, główny uczestnik |
| na dzień dzisiejszy | dziś |
| na ten moment, w tym momencie | teraz, na razie |
| w międzyczasie | tymczasem |
| finalnie | ostatecznie, w końcu |
| definitywnie | na pewno |
| posiadać (gdy wystarczy „mieć”) | mieć |
| robić sens | mieć sens |
| generalnie, tak naprawdę (jako wypełniacz) | ogólnie albo usuń |

Guard: kalką nie jest świadomy żargon zawodowy, nazwa własna ani zapożyczenie bez zgrabnego polskiego odpowiednika. W razie wątpliwości zostaw słowo w spokoju. Fałszywe tłumaczenie żargonu psuje tekst mocniej niż kalka, bo zmienia znaczenie.

## Jak uruchomić ten przebieg

Najlepiej jako osobne czytanie, a w trybie wielu agentów jako osobnego recenzenta polszczyzny, który dostaje gotowy tekst i zgłasza sześć rzeczy:

1. anglicyzmy do przetłumaczenia (z podziałem na leniwe i chronione),
2. zdania bez czasownika osobowego oraz przymiotnik wypchnięty na front,
3. kalki-przymiotniki do rozwinięcia,
4. ukryte „nie X, to Y”,
5. serie urywanych zdań do scalenia,
6. kalki wykryte testem odwrotnego tłumaczenia.

Recenzent zgłasza, nie przepisuje samodzielnie. Poprawki wprowadza ten sam model, który prowadzi całą redakcję, bo tylko on ma przed oczami oryginał i wynik audytu semantycznego.

## Czego w tym przebiegu nie ruszasz

- Terminów z profilu lokalnego i żargonu, który wraca w tekście jako świadomy motyw.
- Cytatów, tytułów i nazw własnych, także wtedy, gdy zawierają kalkę.
- Terminologii prawnej, normalizacyjnej i technicznej. Zamiana „audytu” na „kontrolę” wygląda jak poprawa polszczyzny, a jest zmianą znaczenia.
- Tekstu w innym języku wplecionego w polski.
- Konwencji zapisu autora, w tym pisania bez ogonków, jeśli konsekwentnie tak pisze.
