# humanizer-pl

Skill agentowy, który usuwa oznaki pisania przez AI z polskich tekstów. Nie jest tłumaczeniem angielskich reguł, tylko katalogiem zjawisk widocznych dopiero w polszczyźnie: kalek składniowych, GPT-izmów rozpoznawanych po zagęszczeniu, błędów fleksyjnych modeli językowych i typografii według normy PWN. Runtime to zwykły plik Markdown, więc skill działa w każdym środowisku, które rozumie instrukcje w formie skilla.

## English summary

`humanizer-pl` removes AI writing tells from Polish text. It is a Polish-first catalogue rather than a translation: on top of the 33 patterns blader/humanizer collected for English (following Wikipedia's "Signs of AI writing"), it adds eight that exist only in Polish, such as syntactic calques from English, inflection errors typical of language models, PWN typography, and missing local context, plus a suspended-rules mode for legal and official register, where passive voice and repeated defined terms are correct rather than sloppy. If your text is entirely in English, use the original [humanizer](https://github.com/blader/humanizer) skill instead; this one refuses and says so. The runtime artifact is plain Markdown, so any harness that supports skill-style instructions can run it.

## Czym to jest

Skill przepisuje tekst tak, żeby przestał brzmieć jak wygenerowany. Pracuje w siedmiu krokach: rozpoznaje gatunek, kalibruje głos, pisze szkic, robi audyt śladów, przechodzi osobny przebieg polszczyzny, sprawdza znaczenie i dopiero wtedy oddaje wersję finalną.

Cztery zasady wygrywają ze wszystkim innym:

1. **Zero fabrykacji.** W wersji finalnej nie ma faktu, liczby, daty ani nazwiska, którego nie było w oryginale.
2. **Gatunek jest nietykalny.** Wchodzi opinia prawna, wychodzi opinia prawna.
3. **Wierność znaczeniu przed czystością redakcji.** Gdy usunięcie wzorca przesuwa zakres pojęcia albo modalność, zostaje brzydsze zdanie oryginalne.
4. **Przepisanie, nie kosmetyka.** Informacja przeżywa w całości, zdania nie muszą.

Od tłumaczenia angielskiego humanizera różni się trzema rzeczami:

- **Kategoria polszczyzny (wzorce 34–41).** Osiem zjawisk, których w angielskim katalogu nie ma, bo w angielskim nie istnieją: kalki składniowe, siekanie zdań złożonych na proste, zaimkoza i nominalizacja, błędy zgodności przy liczebnikach, brak polskiego kontekstu realiów.
- **Norma typograficzna PWN.** Cudzysłowy „…”, półpauza ze spacjami jako pauza zdaniowa, dywiz wyłącznie wewnątrz wyrazu. Angielski myślnik em bez spacji jest w polskim tekście sygnałem sam w sobie. Norma obowiązuje domyślnie, a osobna reguła anty-tell włącza się tylko na wyraźną prośbę.
- **Wyjątek prawniczy.** W umowie, piśmie procesowym czy regulaminie strona bierna, formy nieosobowe i powtarzanie terminów zdefiniowanych są poprawne. Skill zawiesza w tym rejestrze pięć reguł, a osiem – typografię, cudzysłowy, emoji, artefakty czatu i resztę – egzekwuje tak samo. Terminy ustawowe zostają nietknięte nawet wtedy, gdy pokrywają się z listą słownictwa modelu.

## Instalacja

### Skills CLI

Instalacja globalna, dostępna w każdym projekcie:

```bash
npx skills add PawelASzczesny/humanizer-pl --global
```

Bez `--global` instalacja jest lokalna dla projektu i można ją zacommitować razem z repozytorium. Po instalacji zacznij nową sesję albo przeładuj skille.

### Wtyczka Claude Code

```
/plugin marketplace add PawelASzczesny/humanizer-pl
/plugin install humanizer-pl@humanizer-pl
```

### Ręcznie

Runtime to `SKILL.md` wraz z katalogiem `references/`, więc wystarczy umieścić repozytorium tam, gdzie twoje narzędzie szuka skilli:

```bash
git clone https://github.com/PawelASzczesny/humanizer-pl ~/.claude/skills/humanizer-pl
```

## Użycie

Wywołaj skill tak, jak twoje narzędzie udostępnia skille – slashem albo zwykłą prośbą.

**Tekst wklejony (tryb domyślny).** Dostajesz komplet: rozpoznany gatunek z uzasadnieniem, szkic, listę tego, co nadal brzmi jak model, wersję finalną i podsumowanie zmian. Przy tekstach z liczbami, terminami fachowymi albo odesłaniami do przepisów dochodzi werdykt audytu semantycznego.

```
/humanizer-pl

[wklej tutaj swój tekst]
```

**Plik.** Skill czyta plik, przechodzi całą pętlę wewnętrznie i zapisuje samą wersję finalną. Redaguje wyłącznie prozę: bloki kodu, frontmatter, dane i adresy odnośników zostają nietknięte.

```
Zhumanizuj tekst w notes/post-na-linkedin.md
```

**Tryb osadzony.** Inny agent albo skill używa humanizera jako jednego kroku większego zadania. Pętla idzie w środku, na wyjściu jest sam tekst, bez raportu i komentarza.

**Kalibracja głosu.** Podaj próbkę własnego pisania, a skill dopasuje rytm zdań, słownictwo i przyzwyczajenia do twoich, zamiast produkować generyczną „czystą” polszczyznę. Próbka wygrywa z regułami stylu, łącznie z typografią: jeśli piszesz zdaniami na pół akapitu i lubisz myślniki, skill ich nie potnie.

```
/humanizer-pl

Próbka mojego pisania do dopasowania głosu:
[dwa lub trzy akapity twojego tekstu]

A teraz zhumanizuj to:
[tekst do przepisania]
```

**Reguła anty-tell.** Na wyraźną prośbę („bez żadnych myślników”, „ma wyglądać jak pisane ręcznie”) skill usuwa z wersji finalnej pauzę i półpauzę, zastępując je kropką, przecinkiem, dwukropkiem, nawiasem albo przebudową zdania. Domyślnie tego nie robi, bo w tekstach do druku daje typografię gorszą od normy.

**Profil lokalny.** Plik `references/jargon-profile.local.md` należy do ciebie i nie trafia do repozytorium – wzorzec `references/*.local.md` jest w `.gitignore`. Trzymasz w nim żargon zawodowy, nazwy własne i wewnętrzne skróty firmy, których skill nie ma prawa tłumaczyć ani poprawiać w żadnym przebiegu.

## 41 wzorców

Wzorce działają jak wagi, nie jak bramki. Pojedyncze wystąpienie nie przesądza o niczym – dopiero zagęszczenie sygnałów w akapicie znaczy, że tekst wymaga redakcji. Pełne opisy z parami PRZED i PO są w `references/wzorce-pl.md`.

### I. Treść (1–6)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 1 | Pompowanie znaczenia i „szerszych trendów” | drugie zdanie o doniosłości faktu: `punkt zwrotny`, `wpisuje się w szerszy trend` |
| 2 | Eksponowanie rozpoznawalności i mediów | lista tytułów prasowych zamiast treści wypowiedzi |
| 3 | Płytkie dopowiedzenia imiesłowowe | doczepki `podkreślając`, `co przekłada się na` |
| 4 | Ton promocyjno-reklamowy | rejestr folderu turystycznego zamiast opisu |
| 5 | Mgliste atrybucje i słowa-wytrychy | `eksperci twierdzą` bez nazwiska i źródła |
| 6 | Schematyczne „Wyzwania i perspektywy” | sekcja domykająca temat bez nowej treści |

### II. Język i gramatyka (7–13)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 7 | Słownictwo modelu | rdzenie w rodzaju `przełomowy`, `kompleksowy`, `wielowymiarowy` |
| 8 | Unikanie „jest”, „są”, „to” | `stanowi`, `służy jako`, `jawi się jako` |
| 9 | „To nie X, to Y” i doklejone negacje | paralelizm przeczący, ogony `bez zgadywania` |
| 10 | Reguła trzech | wyliczenia zawsze trzyelementowe, niezależnie od treści |
| 11 | Wariacja synonimiczna | `bohater`, `protagonista`, `postać centralna` o jednej osobie |
| 12 | Fałszywe zakresy | `od startupów po korporacje`, gdy to nie jest skala |
| 13 | Strona bierna ukrywająca sprawcę | zdanie nie mówi, kto działa (poza rejestrem urzędowym) |

### III. Styl i typografia (14–19)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 14 | Myślnik, półpauza, dywiz | myślnik em bez spacji w rytmie angielskim |
| 15 | Nadużycie pogrubień | pogrubione hasła w każdym akapicie |
| 16 | Listy z pogrubionym nagłówkiem śródwierszowym | `**Wydajność:** wydajność wzrosła` |
| 17 | Wielkie litery w nagłówkach | Title Case przeniesiony z angielskiego |
| 18 | Emoji | ozdobniki w nagłówkach i punktach listy |
| 19 | Cudzysłowy | proste albo angielskie zamiast „…” i »…« |

### IV. Komunikacja (20–22)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 20 | Artefakty rozmowy z asystentem | `mam nadzieję, że to pomoże`, `daj znać, jeśli` |
| 21 | Zastrzeżenia o dacie wiedzy | `moja wiedza sięga`, spekulacyjne łatanie luk |
| 22 | Ton służalczy | `świetne pytanie!`, `masz absolutną rację` |

### V. Wypełniacze i asekuracja (23–26)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 23 | Wypełniacze i wielosłowie | `w celu osiągnięcia`, `z uwagi na fakt, że` |
| 24 | Nadmierna asekuracja | piętrowe `wydaje się, że można przypuszczać` |
| 25 | Ogólnikowe pozytywne zakończenia | `przyszłość rysuje się obiecująco` |
| 26 | Anglicyzmy i kalki leksykalne | `dedykowany`, `adresować problem`, `dostarczać wartość` |

### VI. Retoryka i dramaturgia (27–33)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 27 | Tropy autorytetu | `prawdziwe pytanie brzmi`, `sedno sprawy` |
| 28 | Zapowiedzi i drogowskazy | `przyjrzyjmy się`, `w tym artykule omówimy` |
| 29 | Nagłówki-atrapy | nagłówek, a pod nim zdanie powtarzające nagłówek |
| 30 | Pisanie „od zmiany” zamiast od stanu | opis tego, co się zmieniło, zamiast tego, jak jest |
| 31 | Sztuczne puenty i staccato | `Zero ryzyka. Zero stresu. Zero kompromisów.` |
| 32 | Aforyzmy z formułki | `X to nowa Y`, `X to język Z` |
| 33 | Retoryczne otwarcia pseudoszczere | `szczerze?`, `powiedzmy sobie wprost` |

### VII. Polszczyzna (34–41)

| # | Wzorzec | Na czym poznasz |
|---|---|---|
| 34 | Polskie GPT-izmy według funkcji | otwarcia, łączniki i domknięcia w regularnym rozstawie, po kilka na stronę |
| 35 | Kalki składniowe jako test, nie lista | zdanie tłumaczy się na angielski gładziej, niż brzmi po polsku |
| 36 | Parataksa zamiast hipotaksy | ciąg zdań prostych tam, gdzie polszczyzna łączy je spójnikiem |
| 37 | Zaimkoza i nominalizacja | nadmiar `tego` i `to`, `zapewnienie` zamiast formy osobowej |
| 38 | Błędy fleksyjne modeli | zgodność przy liczebnikach, rekcja, odmiana skrótowców |
| 39 | Monotonny rytm i podejrzana czystość | równa długość zdań, zero literówek, zero niedokończeń |
| 40 | Brak polskiego kontekstu | instytucje, etapy edukacji, waluty i święta z obcego porządku w tekście o polskich realiach |
| 41 | Drobne polskie ślady | hasztagi wielbłądzie, wielka litera po dwukropku |

Wzorzec 40 ma węższy zakres, niż sugeruje nazwa. Rozstrzyga jedno pytanie: czy podmiana zachowuje odniesienie, czy je przelicza. Nazwę urzędu wolno oddać polskim odpowiednikiem, ale tylko gdy zdanie mówi o roli, a nie o konkretnej instytucji. Kwoty w obcej walucie **wypadają zamiast być przeliczane** – kursu nie ma w tekście, więc każda liczba wstawiona w to miejsce byłaby zmyślona.

## Co jest w repozytorium

| Plik | Zawartość |
|---|---|
| `SKILL.md` | runtime: zakres, cztery zasady, proces, wyjątek prawniczy, tryby wywołania |
| `references/wzorce-pl.md` | 41 wzorców: sygnały, opis problemu, para PRZED i PO |
| `references/polszczyzna.md` | drugi przebieg: składnia polska zamiast skalkowanej |
| `references/typografia.md` | norma PWN dla kresek, cudzysłowów, liczb i nagłówków |
| `references/gatunki.md` | mapa gatunków, skala swobody, rzeczy nietykalne |
| `references/audyt-semantyczny.md` | procedura kontroli znaczenia i osiem pułapek redakcji |
| `references/przyklady.md` | jedenaście par PRZED i PO, po jednej na gatunek |
| `evals/` | zestaw testowy: 15 przypadków, 12 asercji, uruchamiacz na samej bibliotece standardowej |
| `scripts/validate.py` | walidator pakietu: frontmatter, wersje, numeracja wzorców, budżety linii, typografia dokumentacji |
| `CONTRIBUTING.md` | zasady edycji, budżety linii, reguła strażników asercji |

## Rodowód i zapożyczenia

Ten skill nie powstał w próżni i nie udaje, że powstał.

Punktem wyjścia jest [blader/humanizer](https://github.com/blader/humanizer) (MIT) – katalog 33 wzorców i przebieg pracy szkic → audyt → wersja finalna. Sam blader opiera się na wikipedycznym przewodniku [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), który prowadzi grupa redakcyjna [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) – to tam zebrano obserwacje z tysięcy przypadków tekstu generowanego i to stamtąd pochodzi sama idea katalogowania oznak.

Przed `humanizer-pl` powstały trzy polskie podejścia do tego samego problemu. Każde dało coś, czego nie było w pozostałych:

- [0x00-Crashes/humanizer-pl](https://github.com/0x00-Crashes/humanizer-pl) – rozpoznanie gatunku przed redakcją, audyt semantyczny jako osobny przebieg po redakcji i pomysł, żeby katalogować błędy fleksyjne modeli. Repozytorium nie ma pliku licencyjnego, więc zapożyczyliśmy wyłącznie koncepcje: każdy mechanizm napisaliśmy od zera własnym językiem, a wynik sprawdziliśmy maszynowo, szukając wspólnych ciągów ośmiowyrazowych. W plikach samego skilla, czyli w `SKILL.md` i w katalogu `references/`, nie ma ani jednego takiego ciągu. W dokumentacji pokrywają się rzeczy z natury wspólne: nazwy własne i tytuł publikacji naukowej, którą oba projekty przywołują w bibliografii.
- [pielas-activy/humanizer-pl](https://github.com/pielas-activy/humanizer-pl) (MIT, © 2026 Igor Pielas) – rozpoznanie języka jako krok zerowy, polszczyzna jako osobny przebieg, reguła głębokości ingerencji, profil żargonu użytkownika i pomysł na testy bez wywołania modelu.
- [paszkiewiczmichal/claude-skills-pl](https://github.com/paszkiewiczmichal/claude-skills-pl) (MIT, © 2026 paszkiewiczmichal) – polskie nazwy wzorców, tło normatywne typografii i wyjątek dla rejestru prawniczego. Autor jest radcą prawnym, więc lista reguł zawieszonych w tekstach prawnych pochodzi z praktyki, nie z domysłu.

Formy zapożyczenia są cztery: **cytat** (fragment przejęty w brzmieniu), **adaptacja** (przepisane, ale rozpoznawalnie z tego źródła), **koncepcja** (sam pomysł, sformułowania własne) oraz **odesłanie bibliograficzne**. Który mechanizm skąd pochodzi i w której formie – tabele w [CREDITS.md](CREDITS.md). Noty licencyjne wszystkich źródeł w pełnym brzmieniu – [NOTICE.md](NOTICE.md).

## Polskie źródła

### Norma

Rozstrzygnięcia typograficzne i poprawnościowe opierają się na ustaleniach [Rady Języka Polskiego](https://rjp.pan.pl/) oraz na wydawnictwach poprawnościowych PWN: rodzaje kresek i ich funkcje, cudzysłowy pierwszego i drugiego stopnia, pozycja kropki wobec cudzysłowu zamykającego, zapis liczb, dat i skrótowców.

### Artykuły

Publikacje, z których pochodzą obserwacje o polskich GPT-izmach. Fakty i spostrzeżenia przejęliśmy, sformułowania są własne.

- [Jak rozpoznać tekst z AI? Kompletny przewodnik po »GPT-izmach«](https://dbest-content.com/jak-rozpoznac-tekst-z-ai-kompletny-przewodnik-po-gpt-izmach/) – DBest Content
- [Jak rozpoznać tekst napisany przez AI? Praktyczny przewodnik](https://pracownieorange.pl/inspiration/jak-rozpoznac-tekst-napisany-przez-ai-praktyczny-przewodnik/) – Pracownie Orange, Fundacja Orange
- [To pisało AI – 15 sposobów, jak rozpoznać tekst z Chata GPT](https://katsin.pl/jak-rozpoznac-tekst-z-chatagpt/) – katsin.pl
- [Jak sprawdzić i rozpoznać tekst napisany przez AI?](https://www.senuto.com/pl/blog/jak-sprawdzic-czy-tekst-zostal-napisany-przez-ai/) – Senuto

### Narzędzia

- [Detektor AI po polsku](https://krupinskiai.pl/apps/ai-detektor) – Krupinski AI. Reguły wykonywane lokalnie w przeglądarce, bez wysyłania tekstu na serwer.
- [Humanizer tekstu AI po polsku](https://krupinskiai.pl/apps/humanizer) – Krupinski AI. Bliski krewny tego skilla, tyle że jako aplikacja webowa z regułami zaszytymi na sztywno.

### Lektura uzupełniająca

- Mazur, R. (2024), „O poprawności językowej tekstów generowanych przez SI na przykładzie ChatuGPT”, *LingVaria* 19(1/37), s. 119–138, DOI 10.12797/LV.19.2024.37.08 – [pełny tekst](https://journals.akademicka.pl/lv/article/view/5756), open access. Opracowanie językoznawcze o błędach gramatycznych modeli, przydatne jako podparcie dla kategorii fleksyjnej. Dotyczy błędów, nie manier stylistycznych, więc katalogu wzorców z niego nie budowaliśmy.

## Ograniczenia

**Tylko polszczyzna.** Tekst w całości angielski skill odrzuca i odsyła do [humanizer](https://github.com/blader/humanizer). Wtręty angielskie w polskim tekście traktuje jak żargon chroniony i ich nie tłumaczy.

**Wagi, nie bramki.** Pojedynczy sygnał nie jest wyrokiem. Człowiek też napisze `kluczowy` albo użyje reguły trzech – i będzie miał rację. Skill reaguje na zagęszczenie i na współwystępowanie, a od fałszywych alarmów ma osobną sekcję z listą rzeczy, których flagować nie wolno.

**To nie jest detektor.** Skill nie orzeka, czy tekst napisała maszyna, tylko poprawia tekst, który tak brzmi. Automatyczne detektory mają w polszczyźnie na tyle duży margines błędu, że nie warto na nich opierać decyzji o niczyjej pracy.

**Redakcja zmienia tekst.** Głębokość ingerencji jest celowo duża – to przepisanie, nie kosmetyka. Informacja ma przeżyć w całości, ale zdania nie. W trybie domyślnym dostajesz podsumowanie zmian, a przy tekstach z liczbami i terminami także werdykt audytu semantycznego; jeśli zależy ci na dosłownym brzmieniu, przejrzyj je przed publikacją.

## Znane ograniczenia

Rzeczy wykryte podczas testów przed wydaniem. Żadna nie blokuje pracy skilla, ale lepiej o nich wiedzieć, niż odkryć je samodzielnie.

**Kontrolę wypełniaczy omija znak spoza listy dekoracji.** Asercja `first_line_not_filler` obcina z początku wiersza dekoracje składni markdown – białe znaki, myślniki, znaki listy, cyfry, znaki cytatu i podobne – a dopiero potem porównuje resztę z listą otwarć. Znak spoza tej listy przesuwa więc porównanie i wypełniacz przechodzi: sprawdzone dla cudzysłowu otwierającego, nawiasu i emoji. Przy emoji dziura zamyka się sama, bo łapie je osobna asercja, przy cudzysłowie i nawiasie już nie. Sam skill takie otwarcie usuwa – to ograniczenie warstwy testowej, nie redakcji.

**Miękkie rdzenie mają próg dwóch trafień.** `banned_stems_soft` przepuszcza do dwóch wystąpień niezależnie od długości tekstu. W krótkim tekście oznacza to gęstość kilkukrotnie przekraczającą limit bez jednego sygnału. Próg jest świadomy i spójny z regułą kondensacji z wzorca 34: sygnałem jest zagęszczenie, nie pojedyncze użycie, a rdzenie miękkie to wyrazy mające legalne zastosowanie fachowe i ustawowe.

**Tryb osadzony zdejmuje wgląd w audyt.** Na wyjściu jest sam tekst, więc nie zobaczysz tabeli audytu semantycznego ani decyzji o scaleniu dwóch twierdzeń w jedno. Scalenia bywają trafne, ale zawsze są decyzją. W tekstach, w których taka decyzja jest kosztowna – prawnych, medycznych, finansowych – używaj trybu domyślnego i przejrzyj tabelę.

**Dwa wzorce celowo wstrzymują się od poprawki.** Wzorzec 13 zostawia stronę bierną nietkniętą, gdy oryginał nie wskazuje sprawcy: dopisanie wykonawcy z głowy byłoby fabrykacją, więc skill woli zapytać autora. Wzorzec 40 nie rusza obcych realiów w tekście, który zagranicę faktycznie opisuje, ani nazwy instytucji w zdaniu, które stawia twierdzenie o tej konkretnej instytucji. Skutek jest taki, że część zdań wyglądających na kandydatów do redakcji zostanie bez zmian – to wybór na rzecz wierności, nie przeoczenie.

**Automatyczne sprawdzanie wyjścia wymaga wycięcia wersji finalnej.** W trybie domyślnym odpowiedź zawiera także wejście z usterkami: cytaty w raporcie audytu, przykłady tego, co brzmiało jak model. Jeżeli podłączysz zestaw asercji do potoku i puścisz na całej odpowiedzi, zapali się na cudzych słowach – emoji, słownictwie modelu i artefaktach czatu, które skill właśnie wyciął. Kontrola musi najpierw wyodrębnić sekcję z wersją finalną.

## Licencja

MIT, © 2026 Paweł Szczęsny. Patrz [LICENSE](LICENSE), [NOTICE.md](NOTICE.md) i [CREDITS.md](CREDITS.md).
