# Audyt semantyczny

Najważniejszy krok całej redakcji. Każda zmiana, która przesuwa znaczenie pojęcia, twierdzenia, liczby, kwantyfikatora albo modalności, jest błędem, choćby tekst brzmiał po niej lepiej. Ładniejsze zdanie mówiące coś innego niż oryginał to nie redakcja, tylko cicha zmiana treści.

Audyt robisz po drugim przebiegu, przed oddaniem wersji finalnej.

**Obowiązkowo** przy tekstach naukowych, prawnych, urzędowych, technicznych, medycznych i finansowych oraz wszędzie tam, gdzie w tekście są liczby, terminy fachowe, warunki albo odesłania do przepisów. **Skrócona forma** (sam krok 1 i szybkie porównanie) wystarczy przy wiadomości prywatnej, poście i krótkim tekście bez danych.

## Krok 1: wypisz twierdzenia z oryginału

Czytasz oryginał zdanie po zdaniu i wypisujesz wszystko, co należy do ośmiu klas poniżej:

1. **Definicję**: „X to…”, „przez X rozumiemy…”, „X oznacza…”.
2. **Twierdzenie merytoryczne**: zależność między zjawiskami, przypisanie cechy, wskazanie skutku.
3. **Daną liczbową**: kwotę, procent, datę, próg, parametr, liczebność próby.
4. **Nazwę własną, skrótowiec, numer przepisu albo normy, cytat.**
5. **Kwantyfikator**: wszystkie, większość, część, niektóre, żaden, co najmniej.
6. **Modalność**: musi, powinien, może, prawdopodobnie, rzekomo, zwykle.
7. **Warunek, zastrzeżenie albo wyjątek**: „o ile”, „chyba że”, „z zastrzeżeniem”, „poza przypadkiem, gdy”.
8. **Związek przyczynowy albo logiczny**: ponieważ, dlatego, w konsekwencji, mimo to, a zatem.

Twierdzenia numerujesz. To one, a nie zdania, są jednostką porównania.

## Krok 2: zestaw oryginał z redakcją

Dla każdego twierdzenia jeden wiersz tabeli:

| # | Oryginał | Po redakcji | Status |
|---|---|---|---|
| 1 | fragment źródłowy | odpowiadający fragment redakcji | zgodne / ryzyko / rozbieżność |

- **zgodne**: sens, modalność, kwantyfikator i terminologia bez zmian.
- **ryzyko**: przeformułowanie albo synonim, który może przesunąć niuans. Przy terminach fachowych, prawnych i normalizacyjnych status jest zawsze co najmniej „ryzyko”.
- **rozbieżność**: znaczenie się zmieniło; wymaga poprawki, bez wyjątków.

## Krok 3: popraw

Każdą rozbieżność usuwasz. Każde ryzyko przeglądasz jeszcze raz i decydujesz świadomie. Jeżeli nie da się usunąć ryzyka bez wprowadzenia z powrotem wzorca AI, zostawiasz sformułowanie oryginalne. Wierność znaczeniu wygrywa z czystością redakcji za każdym razem.

## Krok 4: wystaw werdykt

Jedna z trzech form, zawsze na końcu odpowiedzi:

> **Audyt semantyczny: zgodny.** Wszystkie twierdzenia zachowane.

> **Audyt semantyczny: zgodny z zastrzeżeniami.** Pozycje 3 i 7: przeformułowanie akceptowalne, bo [powód].

> **Audyt semantyczny: niezgodny.** Pozycje 2 i 5 wymagały poprawki, poprawione w wersji finalnej.

Werdykt „niezgodny” bez poprawki nie istnieje. Albo poprawiasz, albo wracasz do brzmienia oryginału.

## Osiem pułapek

1. **Synonim przesuwa zakres pojęcia.** Termin zdefiniowany w normie, przepisie albo literaturze przedmiotu jest nazwą, nie opisem cechy. Zamiana „audytu” na „kontrolę” albo „wdrożenia” na „realizację” wygląda jak poprawa stylu, a bywa zmianą znaczenia.
2. **Uproszczenie połyka warunek.** „Podmioty objęte nadzorem, poza tymi poniżej progu, mają obowiązek…” nie skraca się do „podmioty mają obowiązek”.
3. **Pominięty wyjątek.** Najczęstszy błąd redakcji dążącej do zwięzłości. Wyjątek zwykle stoi na końcu zdania i pada pierwszy.
4. **Podmieniony kwantyfikator.** „Wiele instytucji” to nie „większość instytucji”, a „może wystąpić” to nie „występuje”.
5. **Przesunięta modalność.** „Może” (uprawnienie), „powinien” (zalecenie) i „musi” (obowiązek) są trzema różnymi treściami. Tak samo „sugeruje”, „wskazuje” i „dowodzi”.
6. **Sklejone twierdzenia.** Połączenie dwóch niezależnych zdań spójnikiem „więc” albo „ponieważ” tworzy związek przyczynowy, którego w oryginale nie było.
7. **Rozdzielone twierdzenie.** Rozbicie jednego zdania na dwa potrafi zmienić wagę członów i kolejność logiczną wywodu.
8. **Przesunięty zakres.** Czasowy („od 2025 roku” to nie „w 2025 roku”), przestrzenny, podmiotowy („w sektorze finansowym” obejmuje więcej niż „w bankowości”) albo odpowiedzialnościowy, gdy zmiana strony biernej na czynną przypisuje działanie komuś, kogo w oryginale nie wskazano.

## Krótki przykład

**Oryginał:**

> Zgodnie z regulaminem uczestnik może odstąpić od umowy w ciągu czternastu dni od dostarczenia towaru, z wyjątkiem towarów przygotowanych na indywidualne zamówienie.

**Redakcja (kandydat):**

> Uczestnik ma czternaście dni na odstąpienie od umowy.

**Tabela:**

| # | Oryginał | Po redakcji | Status |
|---|---|---|---|
| 1 | „może odstąpić” | „ma czternaście dni” | ryzyko: uprawnienie zamienione na opis terminu |
| 2 | „od dostarczenia towaru” | brak | rozbieżność: zniknął moment, od którego biegnie termin |
| 3 | „z wyjątkiem towarów na indywidualne zamówienie” | brak | rozbieżność: pominięty wyjątek |

**Werdykt:** niezgodny w pozycjach 2 i 3. Wersja finalna:

> Uczestnik może odstąpić od umowy w ciągu czternastu dni od dostarczenia towaru. Wyjątkiem są towary przygotowane na indywidualne zamówienie.

Zdanie zostało rozbite na dwa, ale nie ubyło ani warunku, ani wyjątku, ani uprawnienia.

## Czego audyt nie robi

- Nie sprawdza, czy oryginał mówi prawdę. Sprawdza, czy redakcja mówi to samo.
- Nie uzupełnia luk w oryginale. Brak danych zostaje brakiem danych.
- Nie ocenia stylu. Zdanie brzydkie, ale wierne, przechodzi audyt.
- Nie zastępuje audytu śladów AI. To dwa różne przebiegi z różnymi pytaniami.
