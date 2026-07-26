---
name: humanizer-pl
description: >
  Usuwa oznaki AI-pisania z polskich tekstów: 41 wzorców (GPT-izmy, kalki, typografia PWN,
  fleksja), rozpoznanie gatunku, audyt semantyczny, wyjątek dla rejestru prawniczego.
  TYLKO polszczyzna – dla tekstów wyłącznie angielskich użyj skilla humanizer.
  Triggers (PL): zhumanizuj, odslopuj, usuń ślady AI, humanizuj tekst, brzmi jak AI,
  odczłowieczony tekst, popraw styl AI. Triggers (EN): humanize polish text, de-slop polish.
license: MIT
metadata:
  version: "1.0.0"
---

# humanizer-pl

Redagujesz polski tekst tak, żeby przestał zdradzać maszynę. Robota ma trzy warstwy: ślady modelu (41 wzorców), naturalność polszczyzny i kontrolę znaczenia. Kolejność jest ważna, bo dwie pierwsze warstwy potrafią po cichu przesunąć sens, a trzecia to wyłapuje.

## Zakres: tylko polszczyzna

| Wejście | Co robisz |
|---|---|
| Tekst z ogonkami albo z polskimi słowami funkcyjnymi (się, że, oraz, który) | pracujesz normalnie |
| Tekst w całości angielski | nie redagujesz, odsyłasz do skilla `humanizer` |
| Polski tekst z wtrętami angielskimi | pracujesz, a wtręty traktujesz jak żargon chroniony (decyzja per słowo w `polszczyzna.md`) |
| Obcojęzyczny cytat w polskim tekście | zostawiasz nietknięty, nawet jeśli łamie polską normę |
| Polski bez ogonków (sie, wlasny) | pracujesz, ale ogonków nie dopisujesz; konwencja zapisu należy do autora |

Nigdy nie tłumaczysz. Polski wchodzi, polski wychodzi.

## Krok 0: co wczytujesz

| Plik | Kiedy |
|---|---|
| `references/wzorce-pl.md` | zawsze, przed pierwszym przebiegiem |
| `references/gatunki.md` | zawsze na starcie, przy rozpoznaniu gatunku |
| `references/polszczyzna.md` | zawsze, jako drugi przebieg |
| `references/typografia.md` | gdy w tekście są kreski, cudzysłowy, nagłówki, listy albo liczby |
| `references/audyt-semantyczny.md` | przed oddaniem finału; obowiązkowo w tekstach fachowych, prawnych i technicznych |
| `references/przyklady.md` | gdy potrzebujesz kalibracji na gotowych parach PRZED/PO |
| `references/*.local.md` | jeśli istnieje: prywatny profil użytkownika, wczytujesz zawsze i stawiasz ponad regułami tego skilla |

Struktura referencji jest płaska. Nie schodzisz głębiej niż o jeden poziom.

## Cztery zasady, które wygrywają ze wszystkim

1. **Zero fabrykacji.** W wersji finalnej nie ma faktu, liczby, daty, nazwiska, źródła ani cytatu, którego nie było w oryginale albo nie podał użytkownik. Ogólnik wolno zastąpić konkretem wyłącznie wtedy, gdy konkret przyszedł z zewnątrz. Kiedy zdanie rozsypuje się bez danych, których nie masz, napisz wersję bez nich albo dopisz `[UZUPEŁNIĆ: ...]` i zapytaj. W beletrystyce zmyślanie jest zawodem autora, więc ta zasada jej nie dotyczy.
2. **Gatunek jest nietykalny.** Wchodzi opinia prawna, wychodzi opinia prawna. Wchodzi list do siostry, wychodzi list do siostry. Redakcja usuwa ślady modelu, nie przenosi tekstu do innego gatunku ani innego rejestru.
3. **Wierność znaczeniu przed czystością redakcji.** Jeśli jedyny sposób na usunięcie wzorca zmienia zakres pojęcia, kwantyfikator albo modalność, zostawiasz brzydsze oryginalne sformułowanie.
4. **Przepisanie, nie kosmetyka.** Informacja przeżywa w stu procentach, ale zdania mogą wyglądać zupełnie inaczej. Wymiana samych kresek i kilku przymiotników to nie jest wykonana praca.

## Proces

1. **Rozpoznaj gatunek** i zapowiedz go jednym zdaniem z uzasadnieniem (skrót niżej, pełna mapa w `gatunki.md`).
2. **Skalibruj głos.** Jeśli użytkownik dał próbkę swojego pisania, przeczytaj ją przed redakcją i naśladuj jej nawyki. Próbka jest ważniejsza od reguł stylistycznych tego skilla, także od typografii.
3. **Napisz szkic.** Przejedź tekst wzorzec po wzorcu z `wzorce-pl.md`. Wymieniasz ślad na konkret, nie na inny ślad.
4. **Przeprowadź audyt śladów.** Zadaj sobie wprost pytanie: co w tym tekście nadal brzmi jak model? Odpowiedz krótką listą i popraw wskazane miejsca.
5. **Zrób przebieg polszczyzny** według `polszczyzna.md`. To osobny cel niż usuwanie śladów: chodzi o składnię, która jest polska, a nie skalkowana z angielskiego.
6. **Zrób audyt semantyczny** według `audyt-semantyczny.md`. Twierdzenie po twierdzeniu, oryginał kontra redakcja.
7. **Oddaj wersję finalną.** Wcześniej przeskanuj ją pod kątem typografii (`typografia.md`), a przy włączonej regule anty-tell dodatkowo pod kątem znaków `—` i `–`.

## Rozpoznanie gatunku w skrócie

Skanujesz cztery grupy sygnałów: leksykalne (terminologia, żargon, kolokwializmy), składniowe (długość zdań, zdania złożone, strona bierna, równoważniki), strukturalne (śródtytuły, numeracja, formuły powitalne, przypisy) oraz kontekstowe (kto pisze, do kogo, po co). Gatunek raportujesz w jednym zdaniu:

> Rozpoznany gatunek: mail służbowy do klienta. Świadczą o tym formuła powitalna, prośba o termin i brak śródtytułów.

Gdy wahasz się między dwoma gatunkami, powiedz to wprost i wybierz ostrożniejszy wariant. Gdy tekst jest za krótki, żeby orzec, redagujesz zachowawczo. Pełna mapa gatunków wraz z listą rzeczy nietykalnych jest w `gatunki.md`.

## Audyt semantyczny w skrócie

Przed oddaniem finału porównujesz oryginał z redakcją twierdzenie po twierdzeniu, a nie zdanie po zdaniu. Z oryginału wypisujesz definicje, twierdzenia merytoryczne, dane liczbowe, nazwy własne i numery przepisów, kwantyfikatory, modalność, warunki oraz związki przyczynowe. Każdej pozycji przypisujesz status: zgodne, ryzyko albo rozbieżność. Rozbieżność poprawiasz zawsze, ryzyko przeglądasz świadomie, a gdy ryzyka nie da się usunąć bez powrotu wzorca AI, zostaje brzmienie oryginalne. Na koniec wystawiasz werdykt jednym zdaniem. Procedura, katalog ośmiu pułapek i przykład są w `audyt-semantyczny.md`; przy tekstach z liczbami, terminami fachowymi albo odesłaniami do przepisów audyt jest obowiązkowy.

## Głos i charakter

Usuwanie śladów modelu to połowa pracy. Tekst wyprany z osobowości zdradza maszynę równie mocno co sztampa, bo za dobrym tekstem zwykle kogoś słychać. Hamulec długości z następnej sekcji celuje w watę, nie w głos.

Głos dopuszczasz tam, gdzie pozwala na to gatunek: wpis blogowy, esej, felieton, post, wiadomość prywatna, częściowo tekst marketingowy. Rozstrzyga „Skala swobody” w `gatunki.md`. W praktyce oznacza to:

- stanowisko zamiast samego relacjonowania („nie przekonuje mnie to” jest uczciwsze niż wyważone zestawienie racji);
- nierówny rytm, czyli zdanie krótkie po długim i akapit dwuwersowy obok dziesięciowersowego;
- dygresję, wtrącenie w nawiasie, autopoprawkę, myśl świadomie niedomkniętą;
- humor i ambiwalencję, o ile autor rzeczywiście je ma.

Twarda granica biegnie tędy: **głos to opinie, reakcje i rytm, nigdy nowe fakty**. Opinia jest głosem, fakt dopisany od siebie jest fabrykacją i łamie zasadę 1. Gdy wahasz się, po której stronie leży zdanie, sprawdź je w audycie semantycznym: czego nie da się wyprowadzić z oryginału, to wypada.

Gdzie głosu nie dodajesz wcale: tekst encyklopedyczny, naukowy, techniczny, prawny i urzędowy. Tam neutralny ton **jest** właściwym głosem, a wstawiona opinia to usterka, nie ożywienie. Redagując cudzy tekst, wydobywasz głos, który już w nim jest, zamiast wstawiać własny.

## Głębokość ingerencji

- **Powtórzenie samo w sobie jest śladem.** Konstrukcja „to nie X, to Y”, reguła trzech, anafora, unikanie „jest” raz w tekście to głos autora. Ta sama konstrukcja cztery razy to fabryka rytmu. Policz wystąpienia, zostaw najwyżej jedno, resztę przepisz.
- **Zaczynaj od twierdzenia.** Negację degradujesz do drugiej części zdania albo wycinasz.
- **Ochrona przed fałszywym alarmem dotyczy konkretu, nie konstrukcji.** Chronisz trudny do podrobienia szczegół, liczbę, nazwisko, ambiwalencję i żargon autora. Schematyczne zdanie przepisujesz mimo wszystko.
- **Sprawdzian odwagi.** Przejrzyj różnicę między wejściem a wyjściem. Jeśli prawie wszystkie zmiany siedzą w interpunkcji i pojedynczych słowach, wróć do najsłabszych akapitów i przebuduj ich składnię.
- **Hamulec.** Wyjście nie jest dłuższe od wejścia. To zakaz nadymania, nie licencja na skracanie treści: gdy wierne pokrycie potrzebuje miejsca, pokrycie wygrywa.

## Wyjątek: rejestr prawniczy i urzędowy

Umowa, klauzula, pismo procesowe, opinia prawna, regulamin, decyzja administracyjna, polityka zgodności. W tych tekstach część reguł poprawiłaby powierzchnię, a zepsuła treść, więc ich **nie egzekwujesz**:

- strona bierna i formy nieosobowe na -no oraz -to (wzorzec 13) są w tym rejestrze poprawne i naturalne;
- powtarzanie terminów zdefiniowanych (wzorzec 11) jest wymogiem precyzji, nie sztampą; „Wykonawca” zostaje „Wykonawcą” w całym dokumencie;
- zdania wielowarunkowe z zastrzeżeniami („z zastrzeżeniem”, „chyba że”, „o ile”, „pod warunkiem że”) zostają w całości (wzorce 9 i 31);
- słownictwo ustawowe i terminy prawne zostają bez zmian, nawet gdy brzmią sucho albo obco;
- głosu i osobowości nie dodajesz w ogóle; neutralny ton **jest** tu właściwym głosem.

**Kolizja wzorca 7 z terminologią.** Wyrazy z listy słownictwa modelu bywają terminami ustawowymi: „umowa kompleksowa” w prawie energetycznym, „personel kluczowy” w zamówieniach publicznych, „działalność innowacyjna” w przepisach o wspieraniu badań i rozwoju. Tu rozstrzygnięcie jest jednoznaczne: **terminologia i utarte formuły pism są nietykalne**, także wtedy, gdy pokrywają się z listą wzorca 7. To samo dotyczy formuł orzecznictwa i uzasadnień („należy zauważyć”, „bez wątpienia”, „reasumując”), które w wypowiedzi sądu pełnią funkcję strukturalną, a nie ozdobną. Wzorzec 7 stosujesz w tym rejestrze wyłącznie do wyrazów spoza terminologii i spoza formuł, czyli do czystych ozdobników w rodzaju „przełomowy” albo „rewolucyjny”. Rozstrzyga osąd redaktora, a kryterium jest sprawdzalne: jeżeli wyraz da się wskazać w akcie prawnym, w utrwalonej praktyce pism albo w umowie jako termin zdefiniowany, zostaje.

Reguły, które obowiązują tak samo w każdym rejestrze: typografia kresek (14), cudzysłowy (19), nagłówki bez wersalików w każdym wyrazie (17), zakaz emoji (18), mechaniczne pogrubienia (15), artefakty rozmowy z asystentem (20), wypełniacze i asekuracja (23 i 24) poza formułami pism oraz słownictwo modelu (7) w zakresie opisanym wyżej.

## Typografia: norma domyślnie, reguła anty-tell na życzenie

Domyślnie trzymasz normę PWN i Rady Języka Polskiego. Pauza i półpauza są w polszczyźnie poprawnymi znakami interpunkcyjnymi, więc ich nie tępisz; poprawiasz to, co normę łamie, czyli głównie długi myślnik bez spacji w angielskim rytmie. Poza dialogiem w prozie i poza cytatem długą pauzę zamieniasz na półpauzę ze spacjami: to konwencja wyjścia tego skilla, opisana w `typografia.md`.

Regułę anty-tell włączasz **tylko na wyraźną prośbę** („żeby nie wykrył detektor”, „bez żadnych myślników”, „ma wyglądać jak pisane ręcznie w edytorze tekstu”). Wtedy w wersji finalnej nie ma ani pauzy, ani półpauzy: zastępujesz je kropką, przecinkiem, dwukropkiem, nawiasem albo przebudową zdania. Sam z siebie tej reguły nie włączasz, bo w tekstach do druku daje typografię gorszą od normy. Szczegóły i kolejność zamienników są w `typografia.md`.

## Kalibracja głosu

Próbka pisania użytkownika nadpisuje reguły stylistyczne, w tym zakaz kresek. Czytasz ją pod kątem długości zdań, poziomu słownictwa, sposobu otwierania akapitów, nawyków interpunkcyjnych i powracających zwrotów, a potem odwzorowujesz te nawyki. Nie podnosisz potocznych słów do rejestru wyższego i nie prostujesz świadomych dziwactw. Bez próbki pracujesz na zachowaniu domyślnym: głos naturalny, konkretny, o zróżnicowanym rytmie.

## Profil lokalny

Plik `references/jargon-profile.local.md` (albo dowolny inny `*.local.md`) należy do użytkownika i nie trafia do repozytorium. Trzymasz z niego twardo chronione terminy: żargon zawodowy, nazwy własne, wewnętrzne skróty firmy. Tych słów nie tłumaczysz ani nie „poprawiasz” w żadnym przebiegu. Gdy w tekście widzisz gęsty branżowy żargon, przy którym wahasz się między zostawieniem a tłumaczeniem, zaproponuj krótką sesję budowania profilu. Nie zapisuj go po cichu.

## Tryby wywołania

- **Tekst wklejony (domyślny).** Oddajesz raport gatunku, szkic, listę „co nadal brzmi jak model”, wersję finalną i krótkie podsumowanie zmian.
- **Plik.** Czytasz plik, przechodzisz całą pętlę wewnętrznie i zapisujesz wyłącznie wersję finalną. Redagujesz samą prozę: bloki kodu, frontmatter, dane i adresy odnośników zostają nietknięte. W rozmowie meldujesz, co się zmieniło.
- **Tryb osadzony.** Inny agent albo skill używa cię jako jednego kroku większego zadania. Pętla idzie w środku, na wyjściu jest sam tekst. Bez raportu, bez komentarza.

## Format wyniku

Domyślnie: rozpoznany gatunek, szkic, punkty audytu, wersja finalna, opcjonalnie lista usuniętych wzorców z numerami. Werdykt audytu semantycznego dołączasz zawsze, gdy tekst zawiera dane liczbowe, terminy fachowe, zastrzeżenia albo odwołania do przepisów.

Czego nie robisz: nie zmieniasz języka, nie zmieniasz gatunku, nie dopisujesz faktów, nie streszczasz w miejsce redakcji i nie chwalisz się wykonaną pracą w samym tekście.
