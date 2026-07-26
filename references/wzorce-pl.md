# Wzorce AI w polskim tekście

Czterdzieści jeden wzorców w siedmiu kategoriach. Kategorie od pierwszej do szóstej opisują ślady wspólne dla polszczyzny i angielszczyzny, ale w polskich sformułowaniach. Kategoria siódma jest wyłącznie polska i to ona odróżnia ten skill od przetłumaczonej listy angielskiej.

Format każdego wzorca: **Sygnały** w postaci par tell → akcja, **Problem** w jednym albo dwóch zdaniach, potem krótka para PRZED/PO.

Wszystkie te wzorce mają jedną przyczynę. Model dobiera kolejne słowo tak, żeby pasowało do możliwie największej liczby sytuacji, w jakich mogłoby paść. Wybór najbezpieczniejszy statystycznie jest z definicji uśredniony, więc tekst wychodzi gładki, symetryczny i pozbawiony ryzyka. Lista poniżej to katalog objawów tego jednego mechanizmu. Obserwacje, od których zaczęła się ta rodzina list, gromadzi społeczność Wikipedii pod hasłem [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

Jak z tego korzystać:

- **Skupisko, nie pojedyncze trafienie.** Jeden imiesłów, jedna półpauza i jedno „ponadto” nie znaczą nic. Ślad zaczyna się tam, gdzie wzorce nakładają się na siebie w jednym akapicie.
- **Wymieniasz ślad na treść, nie na inny ślad.** Wycięcie „kluczowego” i wstawienie „istotnego” to praca pozorna.
- **Wersja PO nigdy nie wnosi faktów, których nie było w PRZED.** Przykłady w tym pliku trzymają tę zasadę, żebyś miał ją przed oczami także w praktyce.
- **Przykłady są zmyślone i celowo bezimienne.** Nie traktuj ich jako danych o świecie.

Przykłady w blokach cytatu łamią polską normę typograficzną świadomie: pokazują usterkę, którą masz wyłapać.

---

## I. Treść (1–6)

### 1. Pompowanie znaczenia, dziedzictwa i „szerszych trendów”

**Sygnały:** stanowi świadectwo, stanowi dowód → wytnij zdanie; odgrywa kluczową rolę → napisz, co ta rzecz robi; wpisuje się w szerszy trend, na przestrzeni lat → wytnij; kamień milowy, punkt zwrotny, przełom → podaj fakt bez etykiety; odcisnął piętno, na trwałe zapisał się, symbolizuje → wytnij.

**Problem:** Model dokłada do faktu drugie zdanie o jego doniosłości. Ta warstwa nie ma pokrycia w źródle i po jej usunięciu nie ubywa żadnej informacji.

> **PRZED:** Zakład uruchomiono w 1994 roku, co stanowiło punkt zwrotny w rozwoju branży i wpisywało się w szerszy trend modernizacji regionu.
>
> **PO:** Zakład uruchomiono w 1994 roku.

### 2. Nadmierne eksponowanie rozpoznawalności i mediów

**Sygnały:** był szeroko opisywany, zyskał uznanie, prestiżowe tytuły, ogólnopolskie media → zostaw jedno wystąpienie, ale z treścią; prowadzi aktywny profil, tysiące obserwujących → wytnij, chyba że liczba coś tłumaczy; niezależne źródła potwierdzają → nazwij źródło albo skreśl.

**Problem:** Zamiast powiedzieć, co ktoś zrobił, model wylicza, gdzie o tym wspomniano. Lista mediów bez treści wypowiedzi nie informuje o niczym.

> **PRZED:** Jej analizy cytowały prestiżowe tytuły w kraju i za granicą, w tym branżowy kwartalnik, w którym tłumaczyła mechanizm dopłat. Prowadzi też aktywny profil w mediach społecznościowych.
>
> **PO:** W branżowym kwartalniku tłumaczyła mechanizm dopłat.

### 3. Płytkie dopowiedzenia imiesłowowe i ogony „co podkreśla…”

**Sygnały:** podkreślając, odzwierciedlając, przyczyniając się do, ukazując, obejmując, wzmacniając → wytnij doczepkę; ogony „co czyni go”, „co przekłada się na”, „tym samym zwiększając” → wytnij albo rozbij na zdanie z czasownikiem osobowym.

**Problem:** Imiesłów przysłówkowy doklejony na końcu zdania udaje wniosek, a zwykle powtarza to, co już padło. Jest to polski odpowiednik angielskiej końcówki -ing.

> **PRZED:** Kurs trwa osiem tygodni, odzwierciedlając potrzeby uczestników i przyczyniając się do wzrostu ich kompetencji.
>
> **PO:** Kurs trwa osiem tygodni.

### 4. Ton promocyjno-reklamowy

**Sygnały:** malowniczy, urokliwy, tętniący życiem, perła regionu, w sercu miasta, zapierający dech, kultowy, niezapomniany → nazwij rzecz wprost; szczyci się, słynie z, może pochwalić się → napisz, co ta rzecz ma; bogaty w przenośni (bogata oferta, bogate dziedzictwo) → wymień zawartość albo wytnij.

**Problem:** Model wpada w rejestr folderu turystycznego, zwłaszcza przy miejscach, kulturze i produktach. Zdanie robi się entuzjastyczne i puste jednocześnie.

> **PRZED:** Malowniczo położona w sercu regionu miejscowość tętni życiem i szczyci się bogatym dziedzictwem.
>
> **PO:** Miejscowość leży w środkowej części regionu.

### 5. Mgliste atrybucje i słowa-wytrychy

**Sygnały:** eksperci twierdzą, analitycy wskazują, obserwatorzy zauważają → podaj nazwisko albo instytucję; według doniesień, jak pokazują badania, liczne źródła podają → wskaż konkretne badanie albo wytnij twierdzenie; powszechnie uważa się, jak wiadomo → wytnij.

**Problem:** Model podpiera twierdzenie autorytetem, którego nie potrafi wskazać. Przypis do nikogo nie jest przypisem, tylko dekoracją.

> **PRZED:** Eksperci są zgodni, że nowa metoda znacząco skraca czas obsługi.
>
> **PO:** (Bez źródła to zdanie nie ma pokrycia. Wytnij je albo podaj badanie, na które się powołujesz.)

### 6. Schematyczne sekcje „Wyzwania i perspektywy”

**Sygnały:** nagłówek „Wyzwania i perspektywy”, „Podsumowanie i wnioski” doklejony bez potrzeby → usuń sekcję; „Pomimo licznych wyzwań”, „Mimo tych trudności” → zostaw konkretny problem, wytnij ramę; „przyszłość rysuje się obiecująco” → wytnij.

**Problem:** Model domyka temat gotowym szkieletem: najpierw wylicza abstrakcyjne trudności, potem je unieważnia optymistycznym zdaniem. Żadna z tych warstw nie niesie informacji.

> **PRZED:** Mimo wyzwań typowych dla branży spółka konsekwentnie się rozwija, a przyszłość rysuje się obiecująco.
>
> **PO:** (Zdanie nie zawiera żadnej informacji. Wytnij je albo wpisz konkretne trudności, jeśli tekst źródłowy je podaje.)

---

## II. Język i gramatyka (7–13)

### 7. Słownictwo modelu

**Sygnały:** kluczowy, istotny, znaczący, fundamentalny → wytnij przymiotnik albo napisz, dlaczego coś waży; innowacyjny, przełomowy, rewolucyjny → napisz, co jest nowe; kompleksowy, holistyczny, wszechstronny → wymień zakres; dedykowany → przeznaczony do, dla, osobny; fascynujący, imponujący, niezwykle, wyjątkowo → wytnij; zaawansowany, niezawodny, synergia → wytnij albo nazwij mechanizm.

**Problem:** Te słowa są w tekstach po 2023 roku wielokrotnie częstsze niż wcześniej i chodzą stadami. Test jest prosty: usuń wyraz i sprawdź, czy zdanie coś straciło. Jeśli nie, była to wata.

> **PRZED:** Nasze kompleksowe i innowacyjne narzędzie odgrywa kluczową rolę w dynamicznie zmieniającym się środowisku finansowym.
>
> **PO:** Nasze narzędzie prowadzi obieg faktur w firmie.

### 8. Unikanie „jest”, „są”, „to”

**Sygnały:** stanowi → jest, to; pełni funkcję, odgrywa rolę → służy do, robi; charakteryzuje się → ma; jawi się jako, prezentuje się jako → wygląda na, jest; może poszczycić się → ma.

**Problem:** Model omija najprostsze orzeczenie, jakby było zbyt ubogie. W polszczyźnie najbardziej razi „stanowi”, które wciska się wszędzie tam, gdzie wystarczyłoby „to”.

> **PRZED:** Sala stanowi przestrzeń warsztatową i charakteryzuje się powierzchnią stu metrów.
>
> **PO:** Sala warsztatowa ma sto metrów.

### 9. „To nie X, to Y”, paralelizmy przeczące i doklejone negacje

**Sygnały:** „To nie X, to Y”, „Nie chodzi o X, chodzi o Y” → zacznij od twierdzenia; „Nie tylko X, ale również Y” → zwykłe „X i Y”; seria „Bez X. Bez Y. Bez Z.” → jedno zdanie z treścią; ogonki „bez zgadywania”, „zero kombinowania” → wpisz w pełne zdanie.

**Problem:** Kontrast przez zaprzeczenie brzmi mocno raz. Powtórzony trzy razy zamienia się w rytm bez treści, bo każda taka para mówi najpierw, czego nie ma.

> **PRZED:** To nie jest kolejny kurs. To zmiana sposobu myślenia. Bez teorii. Bez lania wody.
>
> **PO:** Ten kurs uczy praktyki zamiast teorii.

### 10. Reguła trzech

**Sygnały:** trzy przymiotniki w rzędzie → zostaw najmocniejszy; trzy przykłady tam, gdzie realnie są dwa → wymień dwa; szkielet całego tekstu „wstęp, trzy punkty, podsumowanie” → przebuduj układ pod treść.

**Problem:** Trójka brzmi kompletnie, więc model dosypuje trzeci element, nawet gdy nie ma go z czego wziąć. Trzeci człon zwykle powtarza drugi innymi słowami.

> **PRZED:** Szkolenie jest praktyczne, skuteczne i przyjemne.
>
> **PO:** Szkolenie jest praktyczne.

### 11. Wariacja synonimiczna

**Sygnały:** ta sama osoba lub rzecz nazwana w kolejnych zdaniach inaczej (bohater → protagonista → postać centralna) → wróć do jednej nazwy; łańcuch „firma → przedsiębiorstwo → podmiot → organizacja” → wybierz jedno słowo i trzymaj się go.

**Problem:** Model unika powtórzeń, bo ma je wpisane w karę za powtarzanie. Polszczyzna jest bogata synonimicznie, więc efekt wychodzi jaskrawo. Uwaga: w tekstach prawnych, technicznych i naukowych powtórzenie terminu jest wymogiem, nie usterką.

> **PRZED:** Bohaterka mierzy się z trudnościami. Główna postać pokonuje przeszkody. Protagonistka wraca do domu.
>
> **PO:** Bohaterka mierzy się z trudnościami, pokonuje je i wraca do domu.

### 12. Fałszywe zakresy

**Sygnały:** „od X po Y”, gdy X i Y nie leżą na jednej skali → wymień elementy; „począwszy od…, a skończywszy na…” → wymień elementy; „zarówno…, jak i…” jako ozdoba → wytnij konstrukcję.

**Problem:** Konstrukcja zakresowa sugeruje skalę i kompletność. Kiedy skali nie ma, zdanie obiecuje przegląd, a daje dwa przypadkowe hasła.

> **PRZED:** Kurs obejmuje wszystko, od podstaw obsługi arkusza po zmianę kultury pracy w firmie.
>
> **PO:** Kurs uczy obsługi arkusza i omawia jej wpływ na pracę zespołu.

### 13. Strona bierna i bezosobowość ukrywająca sprawcę

**Sygnały:** „jest rozpatrywany”, „zostaje wdrożony” → nazwij sprawcę, ale tylko jeśli oryginał go podaje; „nie jest wymagane”, „zaleca się” w instrukcji dla użytkownika → tryb osobowy albo rozkazujący; zdania bez podmiotu w opisie działania produktu → wpisz podmiot.

**Problem:** Bierna forma nie jest błędem. Błędem jest chowanie w niej wykonawcy tam, gdzie czytelnik potrzebuje wiedzieć, kto co robi. Sprawcy nigdy nie dopisujesz z głowy: gdy oryginał go nie wskazuje, zostawiasz stronę bierną i pytasz autora. **W rejestrze prawniczym i urzędowym tego wzorca nie egzekwujesz**: formy na -no oraz -to są tam poprawne i naturalne.

> **PRZED:** Zgłoszenie jest weryfikowane przez zespół wsparcia w terminie dwóch dni roboczych.
>
> **PO:** Zespół wsparcia weryfikuje zgłoszenie w terminie dwóch dni roboczych.

---

## III. Styl i typografia (14–19)

### 14. Myślnik, półpauza, dywiz

**Sygnały:** długi myślnik bez spacji w angielskim rytmie (`słowo—słowo`) → przecinek, dwukropek albo nowe zdanie; kreska w funkcji przecinka w co drugim zdaniu → przywróć zwykłą interpunkcję; dywiz użyty jako pauza (`tekst - tekst`) w piśmie formalnym → półpauza ze spacjami albo przebudowa.

**Problem:** Pauza i półpauza są w polszczyźnie poprawne, więc nie tępisz ich odruchowo. Sygnałem jest angielski wzór użycia: kreska zamiast każdego innego znaku i brak spacji wokół niej. Pełna norma oraz opcjonalna reguła anty-tell są w `typografia.md`.

> **PRZED:** Termin promują instytucje—nie sami zainteresowani—a mimo to funkcjonuje w dokumentach.
>
> **PO:** Termin promują instytucje, nie sami zainteresowani, a mimo to funkcjonuje w dokumentach.

### 15. Nadużycie pogrubień

**Sygnały:** pogrubione pojedyncze wyrazy w środku zdania → usuń wyróżnienie; pogrubienie każdej nazwy własnej i każdego skrótu → usuń; kilka wyróżnień w jednym akapicie → zostaw najwyżej jedno albo żadnego.

**Problem:** Wyróżnienie działa, gdy jest rzadkie. Model pogrubia mechanicznie, więc czytelnik widzi las tłustego druku i przestaje wiedzieć, co jest ważne.

> **PRZED:** Łączy **cele roczne**, **wskaźniki efektywności** oraz narzędzia wizualne, takie jak **mapa procesu**.
>
> **PO:** Łączy cele roczne, wskaźniki efektywności oraz narzędzia wizualne, na przykład mapę procesu.

### 16. Listy z pogrubionym nagłówkiem śródwierszowym

**Sygnały:** każdy punkt zaczyna się od pogrubionego hasła i dwukropka → zamień listę na akapit albo zostaw same treści punktów; punkt powtarza swój nagłówek w pierwszych słowach → usuń powtórzenie.

**Problem:** Ten układ wygląda na uporządkowany, ale zwykle w każdym punkcie jest jedno zdanie, które parafrazuje własny nagłówek. Po scaleniu w akapit widać, jak mało tam treści.

> **PRZED:**
> - **Wydajność:** Wydajność wzrosła dzięki nowym algorytmom.
> - **Bezpieczeństwo:** Bezpieczeństwo wzmocniono szyfrowaniem.
>
> **PO:** Aktualizacja przyspiesza działanie dzięki nowym algorytmom i dodaje szyfrowanie.

### 17. Wielkie litery w nagłówkach

**Sygnały:** nagłówek z każdym znaczącym wyrazem wielką literą → zostaw wielką literę na początku i w nazwach własnych; podpisy tabel i rysunków w tym samym stylu → popraw tak samo.

**Problem:** Zapis z wielkiej litery w każdym wyrazie to konwencja angielska. W polszczyźnie jest po prostu błędem ortograficznym i jednym z najłatwiejszych do wychwycenia śladów tłumaczenia szablonu.

> **PRZED:** `## Nowe Zasady Rozliczania Delegacji Służbowych`
>
> **PO:** `## Nowe zasady rozliczania delegacji służbowych`

### 18. Emoji

**Sygnały:** emoji przed nagłówkiem albo punktem listy → usuń; emoji jako znacznik statusu w tekście biznesowym → zastąp słowem; kilka różnych emoji w jednym akapicie → usuń wszystkie.

**Problem:** Model dekoruje strukturę emotkami niezależnie od tematu i rejestru. W dokumencie, mailu do klienta czy artykule wygląda to jak szablon prezentacji, nie jak tekst autora.

> **PRZED:** 🚀 **Wdrożenie:** start w trzecim kwartale. ✅ **Następny krok:** spotkanie kontrolne.
>
> **PO:** Wdrożenie ruszy w trzecim kwartale. Następny krok to spotkanie kontrolne.

### 19. Cudzysłowy

**Sygnały:** cudzysłów angielski `“tekst”` albo prosty `"tekst"` w polskiej prozie → zamień na `„tekst”`; dwa znaki otwierające `„tekst“` → popraw zamknięcie; cytat w cytacie w tym samym cudzysłowie → drugi stopień w »…«.

**Problem:** Polski cudzysłów pierwszego stopnia to „…” (otwierający przy dolnej linii, zamykający u góry). Angielskie „kręcone” znaki są tu obcym importem, a prosty cudzysłów maszynowy oznacza w typografii cale i sekundy. W blokach kodu prosty znak zostaje bez zmian.

> **PRZED:** Napisała “magazyn potwierdzi to jutro”, choć nikt jeszcze o to nie pytał.
>
> **PO:** Napisała „magazyn potwierdzi to jutro”, choć nikt jeszcze o to nie pytał.

---

## IV. Komunikacja (20–22)

### 20. Artefakty rozmowy z asystentem

**Sygnały:** „Mam nadzieję, że to pomoże”, „Daj znać, jeśli” → usuń; „Oto…”, „Poniżej znajdziesz…” → zacznij od treści; „Czy chcesz, żebym…?”, „Mam rozwinąć?” → usuń; „Oczywiście!”, „Jasne!” → usuń.

**Problem:** Ramka rozmowy z asystentem zostaje wklejona razem z treścią. To najbardziej jednoznaczny ślad ze wszystkich, bo nie da się go wytłumaczyć stylem autora.

> **PRZED:** Oto przegląd zasad rozliczania delegacji. Mam nadzieję, że to pomoże! Daj znać, jeśli mam rozwinąć któryś punkt.
>
> **PO:** Delegację rozlicza się na podstawie polecenia wyjazdu i dowodów kosztów.

### 21. Zastrzeżenia o dacie wiedzy i spekulacyjne łatanie luk

**Sygnały:** „według mojej ostatniej aktualizacji”, „na dzień dzisiejszy dostępne dane” → usuń; „choć informacje są ograniczone” → napisz wprost, czego nie wiadomo, albo wytnij zdanie; „prawdopodobnie dorastał”, „przypuszcza się, że” → wytnij; „ceni prywatność”, „stroni od rozgłosu” → wytnij.

**Problem:** Dwa powiązane ślady. Pierwszy to zostawione w tekście zastrzeżenie o dacie wiedzy. Drugi to akapit o braku źródeł, po którym model dopisuje prawdopodobnie brzmiące wypełnienie. Brak informacji zapisuje się jednym zdaniem albo pomija.

> **PRZED:** Informacje o początkach firmy nie są szeroko dostępne, co sugeruje, że założyciele cenili prywatność. Prawdopodobnie działali wtedy lokalnie.
>
> **PO:** Początki firmy nie są udokumentowane w dostępnych źródłach.

### 22. Ton służalczy

**Sygnały:** „Świetne pytanie!”, „Doskonała uwaga!” → usuń; „Masz całkowitą rację” → usuń albo zamień na rzeczową odpowiedź; „Z przyjemnością wyjaśnię” → przejdź do wyjaśnienia; „pozostaję do pełnej dyspozycji”, „dołożymy wszelkich starań” → napisz, co konkretnie zrobisz.

**Problem:** Nadmiar uprzejmości bez treści czyta się jak wazelina i osłabia to, co po nim następuje. W mailu handlowym zjada miejsce, w którym powinno stać zobowiązanie.

> **PRZED:** Świetne pytanie! Masz całkowitą rację, że temat jest złożony. Pozostajemy do pełnej dyspozycji.
>
> **PO:** Temat jest złożony. Odpowiedź przyślemy do piątku.

---

## V. Wypełniacze i asekuracja (23–26)

### 23. Wypełniacze i wielosłowie

**Sygnały:** „w celu osiągnięcia” → „aby”; „z uwagi na fakt, że” → „ponieważ”; „w chwili obecnej” → „teraz”; „w przypadku, gdyby” → „jeśli”; „posiada możliwość” → „może”; „warto zauważyć, że”, „należy podkreślić, że” → usuń i przejdź do rzeczy; pleonazmy („okres czasu”, „cofać się do tyłu”, „w miesiącu maju”) → zostaw jeden człon.

**Problem:** Konstrukcje wielowyrazowe wypierają czasowniki i zżerają miejsce bez dodawania treści. Model po nie sięga, bo brzmią oficjalnie, a oficjalność mylona bywa z precyzją.

> **PRZED:** W chwili obecnej, z uwagi na fakt, że system posiada możliwość automatycznego przetwarzania, warto zauważyć, że dane spływają szybciej.
>
> **PO:** System przetwarza dane automatycznie, więc spływają szybciej.

### 24. Nadmierna asekuracja

**Sygnały:** „wydaje się, że można przypuszczać” → zostaw jedno zastrzeżenie; „potencjalnie mogłoby” → „może”; „poniekąd”, „w pewnym sensie”, „niejako” → usuń; „prawdopodobnie w większości przypadków” → wybierz jedną miarę niepewności.

**Problem:** Model nawarstwia zabezpieczenia, aż zdanie przestaje cokolwiek twierdzić. Jedno rzetelne zastrzeżenie jest informacją, trzy zabezpieczenia z rzędu są unikiem. Uwaga: w tekście naukowym modalność bywa treścią, więc jej nie ścinasz bez sprawdzenia w audycie semantycznym.

> **PRZED:** Można by potencjalnie argumentować, że zmiana mogłaby poniekąd wpłynąć na wyniki.
>
> **PO:** Zmiana może wpłynąć na wyniki.

### 25. Ogólnikowe pozytywne zakończenia

**Sygnały:** „przyszłość rysuje się w jasnych barwach” → wytnij; „to krok w dobrą stronę” → wytnij; „przed nami ekscytujące czasy” → wytnij; „warto o tym pamiętać” jako ostatnie zdanie → wytnij.

**Problem:** Model nie potrafi skończyć na fakcie, więc dokleja pożegnanie w tonie podniosłym. Tekst kończy się najlepiej na ostatniej konkretnej informacji.

> **PRZED:** Przyszłość rysuje się w jasnych barwach, a przed firmą ekscytujące czasy. To krok w dobrą stronę.
>
> **PO:** (Wytnij akapit. Zakończ na ostatnim konkrecie z tekstu.)

### 26. Anglicyzmy i kalki leksykalne

**Sygnały:** dedykowany → przeznaczony do, dla, osobny; adresować problem → zająć się, odpowiedzieć na; dostarczać wartość → przynosić korzyść, dawać efekt; w oparciu o → na podstawie; na koniec dnia → ostatecznie, w praktyce; szyty na miarę → dopasowany; wartość dodana → korzyść; być na tej samej stronie → rozumieć się tak samo.

**Problem:** Model wnosi angielskie zwroty z materiału, na którym się uczył. Zdanie jest gramatycznie poprawne, ale brzmi jak przekład. Kalki składniowe i metoda ich wykrywania są osobno we wzorcu 35. Angielskie złożenia z łącznikiem (typu „data-driven”) przybierają po polsku postać sztucznych przymiotników; rozwijasz je według `polszczyzna.md` §3.

> **PRZED:** Nasz dedykowany zespół zaadresuje ten temat i dostarczy wartość w oparciu o dane.
>
> **PO:** Zajmie się tym osobny zespół i pokaże korzyści policzone na podstawie danych.

---

## VI. Retoryka i dramaturgia (27–33)

### 27. Tropy autorytetu

**Sygnały:** „prawdziwe pytanie brzmi” → „pytanie brzmi”; „w gruncie rzeczy”, „tak naprawdę”, „w istocie” → usuń; „u podstaw leży”, „sedno sprawy” → powiedz wprost, o co chodzi; „głębszy problem polega na” → nazwij problem.

**Problem:** Te zwroty zapowiadają przejście na wyższy poziom analizy, a zdanie po nich powtarza zwykłą myśl z dodatkową ceremonią. Po ich usunięciu treść zostaje bez zmian.

> **PRZED:** Prawdziwe pytanie brzmi, czy zespół się dostosuje. W gruncie rzeczy tak naprawdę liczy się gotowość organizacji.
>
> **PO:** Pytanie brzmi, czy zespół się dostosuje. Zależy to od gotowości organizacji.

### 28. Zapowiedzi i drogowskazy

**Sygnały:** „przyjrzyjmy się bliżej”, „zanurzmy się” → wytnij i przejdź do rzeczy; „w tym artykule omówimy” → wytnij; „rozłóżmy to na czynniki pierwsze” → wytnij; „oto, co musisz wiedzieć” → wytnij; „w kolejnym akapicie wyjaśnię” → wyjaśnij.

**Problem:** Model zapowiada czynność zamiast ją wykonać. Meta-komentarz spowalnia lekturę i nadaje tekstowi ton skryptu z poradnika wideo.

> **PRZED:** Przyjrzyjmy się bliżej temu, jak działa buforowanie. Oto, co musisz wiedzieć.
>
> **PO:** Buforowanie działa na dwóch poziomach: w przeglądarce i po stronie serwera.

### 29. Nagłówki-atrapy

**Sygnały:** nagłówek, po którym pierwsze zdanie powtarza nagłówek innymi słowami → usuń to zdanie; „Zacznijmy od podstaw” jako pierwsze zdanie sekcji → usuń; ogólnik w roli rozbiegu („Szybkość ma znaczenie”) → usuń.

**Problem:** Model traktuje pierwsze zdanie sekcji jak rozgrzewkę retoryczną. Czytelnik dostaje najpierw tytuł, potem parafrazę tytułu, a treść zaczyna się dopiero w trzeciej linijce.

> **PRZED:**
> `## Wydajność`
>
> Szybkość ma znaczenie.
>
> Gdy strona ładuje się wolno, użytkownik ucieka.
>
> **PO:**
> `## Wydajność`
>
> Gdy strona ładuje się wolno, użytkownik ucieka.

### 30. Pisanie „od zmiany” zamiast od stanu

**Sygnały:** „ta funkcja została dodana, aby zastąpić” → opisz, co funkcja robi; „w nowej wersji poprawiono” w dokumentacji, która nie jest listą zmian → opisz stan; „wcześniej działało to inaczej” → wytnij, chyba że dokument jest przewodnikiem migracji.

**Problem:** Dokumentacja napisana jako relacja ze zmiany wymaga od czytelnika wiedzy o poprzedniej wersji. Opis stanu obecnego jest zrozumiały dla każdego, kto trafia tu pierwszy raz.

> **PRZED:** Ten moduł dodano po to, aby zastąpić wcześniejsze rozwiązanie, które przeliczało wszystkie pozycje po kolei.
>
> **PO:** Moduł wyszukuje pozycje po identyfikatorze, bez przeliczania całej listy.

### 31. Sztuczne puenty i staccato

**Sygnały:** seria krótkich zdań oznajmujących budujących napięcie → scal w jedno albo dwa zdania z treścią; każde zdanie kończące się jak cytat na plakat → obniż rejestr; urwane równoważniki jeden po drugim → dopisz czasowniki.

**Problem:** Pojedyncze krótkie zdanie podkreśla myśl. Cztery z rzędu produkują dramat bez zawartości, bo każde z nich mówi mniej niż poprzednie.

> **PRZED:** Potem przyszła zmiana. Bez ostrzeżenia. Bez planu awaryjnego. Nic już nie było takie samo.
>
> **PO:** Zmiana przyszła bez ostrzeżenia i bez planu awaryjnego, więc wcześniejsze ustalenia przestały obowiązywać.

### 32. Aforyzmy z formułki

**Sygnały:** „X to nowa Y” → powiedz, co X naprawdę robi; „X to język Y”, „X to waluta Y” → zastąp konkretem; „DNA marki”, „święty Graal branży” → wytnij; „X to nie narzędzie, lecz lustro” → wytnij i napisz twierdzenie wprost.

**Problem:** Model przerabia zwykłe stwierdzenie na sentencję, która brzmi mądrze i niczego nie precyzuje. Zdanie nadaje się do zacytowania i do niczego więcej.

> **PRZED:** Symetria to język zaufania, a wydajność staje się pułapką, gdy zapomina się o ludziach.
>
> **PO:** Symetryczne układy wydają się użytkownikom bardziej przewidywalne. Optymalizacja procesu bywa prowadzona bez sprawdzenia, jak ludzie z niego korzystają.

### 33. Retoryczne otwarcia pseudoszczere

**Sygnały:** „Szczerze?”, „Powiem wprost”, „Umówmy się” jako samodzielny wtręt → wytnij; „Prawda jest taka, że” → wytnij; jednowyrazowe pytanie i odpowiedź po nim („Warto? Zależy.”) → jedno zdanie oznajmujące.

**Problem:** Model udaje odsłonięcie kart, żeby zbudować bliskość przed zwykłym twierdzeniem. Sygnałem jest teatralna pauza, nie samo słowo: „szczerze” w środku zdania jest normalne.

> **PRZED:** Czy to się opłaca? Powiem wprost: zależy, ile razy w miesiącu tego użyjesz.
>
> **PO:** Opłacalność zależy od tego, ile razy w miesiącu tego użyjesz.

---

## VII. Polszczyzna (34–41)

### 34. Polskie GPT-izmy według funkcji w tekście

**Sygnały:** otwarcia („W dzisiejszym dynamicznym świecie”, „W dobie cyfryzacji”, „Nie ulega wątpliwości, że”) → zacznij od konkretu; łączniki („Co więcej”, „Ponadto”, „Co istotne”, „W tym kontekście”) → usuń albo zamień na zwykłe „poza tym”; domknięcia akapitu („Dzięki temu”, „Tym samym”, „W rezultacie”) → usuń, jeśli akapit i tak jest domknięty; zakończenia („Podsumowując”, „Reasumując”, „Z powyższego wynika”) → usuń albo napisz wniosek wprost.

**Problem:** Każdy z tych zwrotów jest osobno niewinny, bo należy do normalnej polszczyzny. Sygnałem jest ich zagęszczenie, czyli kilka na stronę, i regularne rozmieszczenie: otwarcie akapitu, łącznik w środku, domknięcie na końcu. Model nigdy nie zostawia myśli otwartej, więc doszywa klamrę do każdej.

> **PRZED:** W dzisiejszym dynamicznym świecie liczy się czas reakcji. Co więcej, klienci oczekują szybkiej odpowiedzi. Tym samym rośnie znaczenie automatyzacji. Podsumowując, warto o tym pamiętać.
>
> **PO:** Klienci oczekują szybkiej odpowiedzi, więc rośnie znaczenie automatyzacji.

### 35. Kalki składniowe jako test, nie jako lista

**Sygnały:** podejrzaną frazę sprawdzasz trzema pytaniami → (1) czy dosłowne tłumaczenie na angielski daje naturalną angielską frazę („na ten moment” → „at this point”); (2) czy istnieje zwyklejsze polskie słowo (finalnie → ostatecznie, implementować → wdrożyć, w międzyczasie → tymczasem); (3) czy rejestr pasuje do tekstu, czy brzmi jak slajd z korporacji.

**Problem:** Kalki przechodzą przez redakcję, bo są gramatycznie poprawne. Żadna lista ich nie zamknie, więc pracujesz testem, a nie słownikiem. Guard: kalką nie jest świadomy żargon zawodowy autora, nazwa własna ani zapożyczenie bez polskiego odpowiednika. Pełna procedura jest w `polszczyzna.md`.

> **PRZED:** Na ten moment nie adresujemy tego tematu, ale finalnie chcemy dostarczyć rozwiązanie dedykowane dla tej grupy.
>
> **PO:** Na razie się tym nie zajmujemy, ale ostatecznie chcemy przygotować osobne rozwiązanie dla tej grupy.

### 36. Parataksa zamiast hipotaksy

**Sygnały:** trzy krótkie zdania obok siebie, logicznie powiązane → scal spójnikiem („bo”, „więc”, „choć”, „który”); zdanie bez czasownika osobowego („Od pierwszego dnia z konsultantem obok.”) → scal z sąsiadem; równa długość wszystkich zdań w akapicie → zróżnicuj.

**Problem:** Model sieka polszczyznę na krótkie zdania, bo taki rytm ma angielski oryginał jego wzorców. Polski częściej buduje zdanie złożone i przez to brzmi płynniej. Nie scalaj wszystkiego: jedno krótkie zdanie dla podkreślenia myśli zostaje. Scalając, nie dokładaj spójnika przyczynowego („bo”, „więc”, „dlatego”), jeśli przyczyny nie było w oryginale: to pułapka 6 z `audyt-semantyczny.md`.

> **PRZED:** Wdrożenie trwało trzy miesiące. Prowadził je zespół z dwóch działów. Nikt nie przewidział opóźnień w dostawach.
>
> **PO:** Wdrożenie, które prowadził zespół z dwóch działów, trwało trzy miesiące, a opóźnień w dostawach nikt nie przewidział.

### 37. Zaimkoza i nominalizacja

**Sygnały:** nagromadzenie „tego”, „to”, „te”, „który” w jednym zdaniu → usuń zbędne zaimki, polszczyzna ich nie wymaga; rzeczowniki odczasownikowe („zapewnienie zgodności”, „zidentyfikowanie potrzeb”, „dokonanie analizy”) → wróć do formy osobowej („zapewnić”, „rozpoznać”, „przeanalizować”); „dokonać przeglądu” → „przejrzeć”.

**Problem:** Model kalkuje angielski szyk, w którym zaimek jest obowiązkowy, i angielskie rzeczowniki odsłowne. Polszczyzna opuszcza zaimek, gdy podmiot wynika z odmiany, i woli czasownik od jego rzeczownikowej wersji.

> **PRZED:** Celem tego projektu jest zapewnienie tego, aby dokonanie analizy tych danych było możliwe.
>
> **PO:** Projekt ma umożliwić analizę danych.

### 38. Błędy fleksyjne modeli

**Sygnały:** orzeczenie przy liczebniku nieokreślonym („wielu klientów zgłosili”) → forma nijaka pojedyncza („wielu klientów zgłosiło”); pomylony aspekt („przeprowadzić szkolenia co miesiąc”) → aspekt niedokonany („przeprowadzać”); rekcja kalkowana („poprzez wykorzystanie narzędzia”) → „dzięki narzędziu”, „za pomocą narzędzia”; nieodmieniane nazwy własne i skrótowce („użytkownicy Excel”, „zgodnie z RODO w wersji”) → odmieniaj („użytkownicy Excela”, „w ZUS-ie”).

**Problem:** Polska fleksja jest znacznie bogatsza od angielskiej, więc model myli się tam statystycznie najczęściej. Te potknięcia bywają jedynym twardym śladem w tekście, który poza tym brzmi poprawnie.

> **PRZED:** Wielu uczestników zgłosili uwagi poprzez formularz, co pozwoliło przeprowadzić cykliczne przeglądy.
>
> **PO:** Wielu uczestników zgłosiło uwagi w formularzu, co pozwoliło przeprowadzać cykliczne przeglądy.

### 39. Monotonny rytm i podejrzana czystość

**Sygnały:** wszystkie zdania w akapicie mają zbliżoną długość → skróć jedno, wydłuż drugie; każdy akapit ma tyle samo zdań → połam układ; tekst bez jednej dygresji, wtrącenia i autopoprawki → dopuść nierówność, jeśli gatunek na to pozwala.

**Problem:** Ludzki tekst faluje: zdanie krótkie po długim, myśl urwana i dokończona później. Model utrzymuje równy, średni rytm, bo taka jest jego statystyka. Uwaga: sam równy rytm nie jest dowodem, redakcja zawodowa też wygładza tekst.

> **PRZED:** Zespół przygotował raport. Analiza objęła trzy obszary. Wyniki przedstawiono zarządowi. Decyzję podjęto w piątek.
>
> **PO:** Zespół przygotował raport z trzech obszarów i przedstawił go zarządowi. Decyzja zapadła w piątek.

### 40. Brak polskiego kontekstu

**Sygnały:** instytucje i urzędy z obcego porządku (IRS, Internal Revenue Service) → polska nazwa o tym samym odniesieniu; etapy edukacji i stopnie z obcego systemu (high school, college) → polski odpowiednik; kwoty w obcej walucie oraz miary spoza polskiego układu (mile, funty, stopnie Fahrenheita) → usuń wielkość i poproś autora o dane, **nigdy nie przeliczaj**; święta i inne kotwice kalendarzowe (Święto Dziękczynienia, Dzień Pamięci) → określenie czasu wskazujące ten sam moment.

**Problem:** Model uczył się głównie po angielsku, więc domyślne realia ma amerykańskie i wstawia je nawet w tekst zakotwiczony w polskich przepisach. Każda podmiana realiów korzysta z wiedzy spoza tekstu, więc rozstrzyga jedno pytanie: czy ruch **zachowuje odniesienie, czy je przelicza**. Zachowanie odniesienia jest redakcją, przeliczenie jest fabrykacją.

Trzy klasy ruchu:

1. **Podmiana nazwy, gdy zdanie mówi o roli.** „IRS” → „urząd skarbowy”, „high school” → „szkoła średnia”. Zachowujesz **rolę w porządku, którego tekst faktycznie dotyczy**, a nie tożsamość podmiotu: amerykański urząd federalny i polski organ podatkowy to dwie różne instytucje, a high school i szkoła średnia obejmują inne roczniki i inny ustrój szkolny. Dlatego ruch jest dozwolony tylko wtedy, gdy zdanie mówi o roli („zeznanie składasz w urzędzie skarbowym”), a zakazany, gdy stawia twierdzenie o konkretnej instytucji („IRS opublikował wytyczne”); wtedy zostawiasz nazwę albo wycinasz zdanie. Sprawdzian jest ten sam co w klasie 3: czy po podmianie zdanie nadal jest prawdziwe.
2. **Usunięcie wielkości, która wymagałaby przeliczenia.** Kursu ani przelicznika nie masz z tekstu, więc każda liczba, którą byś wstawił, byłaby zmyślona. Wielkość wypada, a zdanie zostaje bez niej. Jeżeli ma wrócić, prosisz autora o wartość w złotych albo w polskich jednostkach ze źródła, którym dysponuje; kwota w złotych wchodzi wyłącznie wtedy, gdy podał ją autor.
3. **Podmiana kotwicy kalendarzowej, ale tylko przy zachowanym odniesieniu.** „Tuż po Święcie Dziękczynienia” → „pod koniec listopada”, bo to święto wypada zawsze między 22 a 28 listopada, więc zdanie jest prawdziwe dokładnie wtedy, gdy było prawdziwe wcześniej. Gdy nie umiesz wskazać tego samego momentu, kotwicę wycinasz zamiast zgadywać.

Guard: nie ruszasz realiów w tekście, który zagranicę faktycznie opisuje. Rozstrzyga to, o czym tekst jest, a nie sama obecność obcej nazwy.

> **PRZED:** Sezon zaczyna się tuż po Święcie Dziękczynienia, przeciętna rodzina wydaje wtedy kilkaset dolarów, a uczniowie high school dorabiają przy pakowaniu.
>
> **PO:** Sezon zaczyna się pod koniec listopada, przeciętna rodzina ponosi wtedy wydatki, a uczniowie szkół średnich dorabiają przy pakowaniu. (Wypadła sama kwota, bo przeliczenia nie ma z czego zrobić; twierdzenie o wydatkach zostaje. Jeśli kwota ma wrócić, poproś autora o wartość w złotych.)

### 41. Drobne polskie ślady

**Sygnały:** hasztagi w zapisie wielbłądzim (#TworzenieTreściSEO) → zapis małymi literami, chyba że autor stosuje wielbłąda świadomie ze względu na czytniki ekranu; wielka litera po dwukropku w środku zdania → mała, jeśli nie zaczyna się pełne zdanie; niekonsekwentna interpunkcja punktów listy (raz kropka, raz nic) → jedna konwencja w całym tekście; kropka przed cudzysłowem zamykającym → w polszczyźnie kropka stoi po cudzysłowie.

**Problem:** To usterki drobne, ale zbierają się w komplet i razem wskazują na szablon przeniesiony z angielskiego. Pojedynczo nic nie znaczą, dlatego liczysz je łącznie z wzorcami 14 i 17. Szczegóły w `typografia.md`.

> **PRZED:** Zapytał: Czy zdążymy? #PlanowanieProjektu, a potem dodał: „nie ma pośpiechu.”
>
> **PO:** Zapytał: czy zdążymy? #planowanieprojektu, a potem dodał: „nie ma pośpiechu”.

---

## Czego NIE flagować

Dobry autor bez najmniejszego udziału modelu potrafi trafić w kilka z powyższych wzorców. Zanim zaczniesz przepisywać, upewnij się, że nie niszczysz dobrego tekstu. Żadna z poniższych cech nie dowodzi niczego sama:

- **Poprawna polska typografia.** Cudzysłów „…” i półpauza ze spacjami to norma, nie ślad. Podejrzany jest dopiero zapis angielski.
- **Formalny rejestr i formuły grzecznościowe.** „Szanowni Państwo”, „z wyrazami szacunku”, „w załączeniu przesyłam” to konwencja korespondencji.
- **Słownictwo prawnicze, urzędowe i fachowe.** „Niniejszym”, „zważywszy”, „należyta staranność”, „amortyzacja” nie są watą. Terminu nie zamieniasz na synonim.
- **Pojedynczy imiesłów, pojedynczy łącznik, pojedyncza kreska.** Ślad zaczyna się przy nawarstwieniu.
- **Bezbłędny język.** Tekst po redakcji zawodowej też nie ma literówek.
- **Sucha, rzeczowa proza.** Model zostawia konkretne ślady. Sama oschłość to po prostu suchy styl.
- **Brak przypisów.** Większość tekstów w sieci jest bez źródeł.
- **Mieszanie rejestru potocznego z fachowym.** Tak pisze wiele osób z branż technicznych.
- **Jedno krótkie zdanie dla emfazy.** Ślad to seria.
- **Cudza fraza w cytacie, tytule albo nazwie własnej.** Nie redagujesz słów, o których tekst mówi, zamiast ich używać.

Szukaj skupisk. Jeden imiesłów nie znaczy nic; imiesłów plus reguła trzech plus „w dzisiejszym dynamicznym świecie” plus sekcja „Podsumowując” to już przyznanie się.

## Oznaki ludzkiego tekstu

Gdy widzisz poniższe, redaguj oszczędnie. Nadmierna ingerencja zabija właśnie to, co czyni tekst wiarygodnym:

- **Konkret trudny do zmyślenia.** Nazwa ulicy, dziwny cytat, kwota z groszami, godzina spotkania.
- **Ambiwalencja i niedokończony spór z samym sobą.** „Chyba dobrze wyszło, ale coś mi tu zgrzyta i nie umiem powiedzieć co.”
- **Polskie realia.** Nazwy urzędów, lokalne zwyczaje, kwoty w złotych, odwołania do przepisów obowiązujących w kraju.
- **Idiom użyty celnie**, a nie kalka przetłumaczona z angielskiego.
- **Odniesienia osadzone w czasie.** Slang, żart wewnętrzny, nawiązanie do wydarzenia z konkretnego roku.
- **Zróżnicowany rytm zdań** i akapity o nierównej długości.
- **Dygresja, wtrącenie w nawiasie, autopoprawka.** „(Chciałem napisać »prawie«, ale to naprawdę było pewne.)”
- **Drobne potknięcia i kolokwializmy**, które autor mógłby obronić, gdyby go zapytać.
- **Świadomy żargon zawodowy**, powracający w tekście jako stały motyw.
