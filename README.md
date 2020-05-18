## Jeżeli pip install pySFML wciąż nie działa, poniżej są dwa linki do manualnej instalacji
mirror 1: https://github.com/Sadzka/JS-Labirynt/tree/pySFML
mirror 2: https://drive.google.com/open?id=1uz2vMbQCoCnE2SrFCDxzkH2Kx72qNQcl


# Generator labiryntów
## **Opis zadania**
- Główne okno programu zawiera kontrolki pozwalające na wybór wielkości labiryntu
(liczba pól N na M; para liczb całkowitych nie większych niż 30), wizualizację labiryntu
(na przykład jako siatka kolorowych przycisków) oraz przycisk “generuj”.
- Labirynt składa się z pól będących korytarzem lub ścianą.
- Użytkownik wybiera dwa różne pola będące wejściem i wyjściem. Pola te
traktowane będą jak korytarz. Po naciśnięciu przycisku “generuj” następuje
generowanie losowego labiryntu.
- Dla każdej pary pól będących korytarzem powinna istnieć ścieżka je łącząca
(brak pól odłączonych od reszty labiryntu). Przechodzenie możliwe jest tylko na
pola będące korytarzem które sąsiadują krawędzią z danym polem.
- Wygenerowany labirynt powinien posiadać ścieżkę od wejścia do wyjścia, która
nie będzie linią prostą (poziomą lub pionową) i która powinna być zaznaczona na
wizualizacji.
- Przechowywana jest lista punktów pośrednich ścieżki prowadzącej od wejścia do
wyjścia.
- Po wybraniu dowolnego pola będącego korytarzem, dodawane jest ono na
koniec listy punktów pośrednich. Następnie powinna zostać znaleziona i
zaznaczona najkrótsza ścieżka prowadząca z wejścia do wyjścia przez wszystkie
punkty pośrednie.
- Wybranie pola będącego punktem pośrednim powoduje usunięcie danego punktu
pośredniego.
- Labirynt nie może posiadać żadnego „pokoju‟: obszar 2 na 2 pola korytarza (lub
większy).
- Labirynt nie może posiadać żadnych obszarów 3 na 3 pola ściany (lub większych).
## **Testy**
1. Wygenerowanie labiryntu o wymiarach 10 na 12 pól z wejściem i wyjściem
na przeciwnych krawędziach.
2. Wygenerowanie labiryntu o wymiarach 20 na 10 pól z wejściem i wyjściem
cztery pola od przeciwnych, krótszych krawędzi.
3. Próba wygenerowania labiryntu o wymiarach 10 na 10 z wejściem i wyjściem
w jednym polu - oczekiwana informacja o błędzie.
4. Próba wygenerowania labiryntu o wymiarach 10 na 10 z wejściem i wyjściem koło
siebie - oczekiwana informacja o błędzie, ścieżka jest linią prostą.
5. Próba wygenerowania labiryntu o wymiarach 10 na 10 z wejściem i wyjściem
między którymi jest 1, 2 lub 3 pola odstępu - oczekiwany labirynt bez ścieżki będącej
linią prostą.
6. Próba wygenerowania labiryntu którego przynajmniej jeden z wymiarów wynosi 0
lub jest liczbą ujemną - oczekiwana informacja o błędzie.
7. Próba wygenerowania za dużego labiryntu - oczekiwana informacja o błędzie.
8. Wygenerowanie labiryntu o wymiarach 13 na 17, wejście i wyjście w dowolnych
miejscach, wyszukanie ścieżki przez punkt pośredni wskazany przez prowadzącego.
Wygenerowanie labiryntu o wymiarach 13 na 17, dodanie dwóch punktów pośrednich
wskazanych przez prowadzącego, usunięcie pierwszego, dodanie kolejnego. Oczekiwane
znalezienie właściwej ścieżki.
9. Próba wyszukania ścieżki przez pole będące ścianą - oczekiwane niepowodzenie
przy próbie dodania punktu pośredniego

## Link do Githuba:
https://github.com/Sadzka/JS-Labirynt

Na końcu raportu muszą się znaleźć opisane linki do istotnych fragmentów
kodu (w źródłach na GitHub) który obrazuje wymagane w projekcie
konstrukcje takie jak:
### a. Lambda-wyrażenia
[Lambda 1](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/game.py#L101)

[Lambda 2](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/game.py#L105)

[Lambda 3](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/game.py#L109)

[Lambda 4](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/game.py#L113)

[Lambda 5](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/game.py#L118)

### b. List comprehensions
[List comprehensions 1](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L275)

[List comprehensions 2](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L323)

[List comprehensions 3](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L324)

[List comprehensions 4](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L328)

[List comprehensions 5](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L388)

[List comprehensions 6](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L392)

[List comprehensions 7](https://github.com/Sadzka/JS-Labirynt/blob/a324a405ab57c14d32b685349b420851792f40bf/map.py#L450)


### c. Klasy
[Klasa Window](https://github.com/Sadzka/JS-Labirynt/blob/3d5d8759c022ef0d10abdadac4a42be777185657/window.py#L3)

[Klasa Game](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/game.py#L7)

[Klasa Maze](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L10)

[Klasa Widget](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/widget.py#L9)

[Klasa Text](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/text.py#L6)

[Klasa Image](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/image.py#L5)

[Klasa Button](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/button.py#L10)

[Klasa ErrorShower](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/errorshower.py#L20)

[Klasa GUIManager](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/guimanager.py#L3)

[Klasa EditBox](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/widget.py#L9)


### d. Wyjątki
[Klasa Wyjątku](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/GUI/errorshower.py#L7)

[Rzucanie Wyjątkiem 1](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L260)

[Rzucanie Wyjątkiem 2](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L264)

[Rzucanie Wyjątkiem 3](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L268)

[Rzucanie Wyjątkiem 4](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L317)

[Rzucanie Wyjątkiem 5](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L436)

[Rzucanie Wyjątkiem 6](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L442)

[Łapanie Wyjątku 1](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L439)

[Łapanie Wyjątku 2](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/map.py#L433)

[Łapanie Wyjątku 3](https://github.com/Sadzka/JS-Labirynt/blob/8824c2d7780a3c6396450c871cbbae389ee1c585/main.py#L10)


