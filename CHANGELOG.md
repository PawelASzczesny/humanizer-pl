# Rejestr zmian

Tu trafiają zmiany, które mają znaczenie dla osób używających skilla.

Format opiera się na [Prowadź Changelog 1.1.0](https://keepachangelog.com/pl/1.1.0/), a numeracja wersji na [wersjonowaniu semantycznym](https://semver.org/lang/pl/).

## [1.0.0] – 2026-07-26

Pierwsze wydanie.

### Dodane

- Katalog 41 wzorców AI-pisania w polszczyźnie, w siedmiu kategoriach: treść, język i gramatyka, styl i typografia, komunikacja, wypełniacze i asekuracja, retoryka i dramaturgia, polszczyzna. Każdy wzorzec ma listę sygnałów z przypisaną akcją, opis problemu i parę przykładów przed i po.
- Kategoria „polszczyzna” (wzorce 34–41), której nie ma w anglojęzycznych katalogach: polskie GPT-izmy rozpoznawane po zagęszczeniu i regularnym rozstawie, kalki składniowe sprawdzane testem zamiast zamkniętą listą, parataksa w miejsce hipotaksy, zaimkoza i nominalizacja, błędy fleksyjne modeli, monotonny rytm, brak polskiego kontekstu, drobne polskie ślady.
- Wzorzec 40 (brak polskiego kontekstu) rozstrzyga podmianę realiów jednym kryterium: czy ruch zachowuje odniesienie, czy je przelicza. Nazwę instytucji albo etapu edukacji wolno oddać polskim odpowiednikiem wyłącznie w zdaniu mówiącym o roli, kotwicę kalendarzową tylko wtedy, gdy nowe określenie wskazuje ten sam moment, a **kwoty w obcej walucie wypadają zamiast być przeliczane**. Przeliczenie wymagałoby kursu, którego w tekście nie ma, więc byłoby fabrykacją i łamałoby zasadę pierwszą.
- Zakres wyłącznie polski: teksty w całości angielskie skill odsyła do skilla `humanizer`, wtręty angielskie w polskim tekście traktuje jak żargon chroniony, a obcojęzyczne cytaty zostawia nietknięte.
- Rozpoznanie gatunku przed redakcją wraz z mapą gatunków, skalą swobody i listą rzeczy nietykalnych w każdym z nich (`references/gatunki.md`).
- Audyt semantyczny jako osobny przebieg po redakcji: procedura czterokrokowa, katalog ośmiu pułapek i werdykt. Obowiązkowy w tekstach z liczbami, terminami fachowymi i odesłaniami do przepisów (`references/audyt-semantyczny.md`).
- Osobny przebieg polszczyzny po usunięciu śladów modelu: składnia polska zamiast skalkowanej z angielskiego (`references/polszczyzna.md`).
- Wyjątek dla rejestru prawniczego i urzędowego: pięć reguł zawieszonych (strona bierna i formy nieosobowe, powtarzanie terminów zdefiniowanych, zdania wielowarunkowe, słownictwo ustawowe, zakaz dodawania głosu) i osiem obowiązujących zawsze. Terminologia ustawowa ma pierwszeństwo przed listą słownictwa modelu.
- Sekcja o głosie i charakterze: tekst wyprany z osobowości zdradza maszynę tak samo jak sztampa, ale głos to opinie, reakcje i rytm, nigdy nowe fakty.
- Norma typograficzna PWN jako zachowanie domyślne: cudzysłowy „…” i »…«, półpauza ze spacjami jako pauza zdaniowa, dywiz wyłącznie wewnątrz wyrazu, nagłówki bez wersalików w każdym wyrazie, zero emoji. Osobna reguła anty-tell, usuwająca wszystkie kreski, włącza się wyłącznie na wyraźną prośbę (`references/typografia.md`).
- Kalibracja głosu z próbki tekstu użytkownika, nadrzędna wobec reguł stylu, oraz profil lokalny w plikach `references/*.local.md`, wyłączonych z repozytorium.
- Jedenaście par przykładów przed i po, po jednej na gatunek, łącznie z fragmentem umowy, tekstem bez ogonków, tekstem z wtrętami angielskimi i prozą z dialogiem (`references/przyklady.md`).
- Zestaw testowy: 15 przypadków (10 wzorcowych i 5 regresyjnych) oraz 12 asercji, w tym kontrola myślników zgodna z normą, rozpoznawanie polskiej pary cudzysłowów, dwie listy zakazanych rdzeni z limitem gęstości dla terminów fachowych i przypadek kontrolny sprawdzający, że dobry tekst człowieka nie wywołuje alarmu. Uruchamiacz działa na samej bibliotece standardowej, bez sieci i bez zapisów na dysk.
- Walidator pakietu (`scripts/validate.py`): 35 kontroli obejmujących frontmatter skilla, zgodność wersji między `SKILL.md`, manifestem wtyczki i tym plikiem, ciągłość numeracji 41 wzorców, budżety linii oraz typografię własnej dokumentacji mierzoną tą samą miarą co wyjście skilla.
- Pakowanie w dwóch wariantach: instalacja przez skills CLI (`npx skills add`) oraz wtyczka Claude Code z własnym katalogiem wtyczek. Workflow CI uruchamia walidator i obie kontrole pakietu.
- Dokumentacja pochodzenia: [NOTICE.md](NOTICE.md) z notami licencyjnymi źródeł i [CREDITS.md](CREDITS.md) z mapą „mechanizm → źródło → forma zapożyczenia”, wraz z wynikiem pomiaru zbieżności tekstowej.
- [CONTRIBUTING.md](CONTRIBUTING.md) z zasadami edycji, budżetami linii i regułą strażników: każda nowa asercja sprawdzająca nieobecność zjawiska dostaje w tym samym commicie przypadek pilnujący jej mechanizmu, sprawdzony testem mutacyjnym.
- Sekcja znanych ograniczeń w README, spisana z testów przed wydaniem: próg dwóch trafień dla rdzeni miękkich, dosłowne dopasowanie początku wiersza w kontroli wypełniaczy, brak wglądu w audyt w trybie osadzonym oraz dwa wzorce, które celowo wstrzymują się od poprawki.
