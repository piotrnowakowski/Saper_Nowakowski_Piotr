Saper

(https://pl.wikipedia.org/wiki/Saper (gra komputerowa))

Opis zadania
- główne okno zawiera dwa pola tekstowe do wprowadzania rozmiaw

- Główne okno zawiera dwa pola tekstowe do wprowadzania rozmiaru planszy (n na m
    pol), plansze o wymiarach n na m p6l (np. siatka przycisków), pole tekstowe na
    wprowadzenie liczby min na planszy, liczbe oznaczonych pol, liczbe min na planszy,
    oraz przycisk rozpoczecia nowej gry.
- Wprowadzenie mniejszego rozmiaru planszy niz 2x2 lub większego niz 15x15, liczby
    min mniejszej niz 0 lub wiekszej niz m*n powoduje wyświetlenie komunikatu o
    bledzie. Nie można rozpocząć gry dopóki te parametry nie są poprawne. Walidacja
    danych powinna wykorzystywać mechanizm wyjątków.
- Na początku gry na losowych polach umieszczane jest tyle min ile wskazano w polu
    tekstowym (każde możliwe rozłożenie min jest równie prawdopodobne).
- Po kliknięciu lewym przyciskiem na pole:
    o Jeśli jest tam mina, wyświetlana jest wiadomość o przegranej i gra sie kończy,
    o Jeśli w sąsiedztwie pola są miny, na przycisku wyświetlana jest ich liczba a pole dezaktywuje sie,
    o W przeciwnym razie sąsiednie pola są sprawdzane tak jakby zostały kliknięte a pole dezaktywuje sie.
- Po kliknięciu prawym przyciskiem pole może zostać oznaczone “tu jest mina”, po ponownym kliknięciu oznaczenie
    zmienia sie na “tu może być mina’, a po kolejnym kliknięciu oznaczenie znika.
- Gra kończy sie po kliknięciu wszystkich pól bez min, lub oznaczeniu “tu jest mina”
    wszystkich pol z minami (i żadnych innych).
- Po naciśnięciu kolejno klawiszy x, y, Z, Z, y, pola pod którymi są miny stają się
    ciemniejsze

TESTY
1. Próba rozpoczęcia gry z rozmiarem planszy i min: (1 na 1; 1), (5 na 1; 2)( 4 na 1; 2)(20 na 500; 12)
    (5 na 6; -4), (3 na 3; 10), (1 na 10; 5) - oczekiwane komunikaty o błędzie.
    Wprowadzenie rozmiarów planszy 8 na 8 i liczby min równej 12 na potrzeby kolejnych testów.

2. Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola,

3. Kliknięcie pola, wyświetla się mina, gra się kończy,

4. Klikniecie pola, brak min w sąsiedztwie - oczekiwane automatyczne sprawdzenie sąsiadów aż do
    wyznaczenia obszaru wyznaczonego przez pola sąsiadujące z minami lub krawędzie planszy,

5. Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnaé o 1,

6. Oznaczenie innego pola jako “tu może być mina”,

7. Oznaczenie pola, odznaczenie go, ponowne oznaczenie i ponowne odznaczenie
    - licznik oznaczonych powinien sie odpowiednio aktualizowaé,

8. Wygranie gry przez klikniecie wszystkich pól bez min,

9. Wygranie gry przez oznaczenie wszystkich pól z minami (można skorzystać z kodu xyzzy),

10. Próba oznaczenia sprawdzonego pola - oczekiwane niepowodzenie,

11. Sprawdzenie kilku pól bez min, oznaczenie pól “tu jest mina’, rozpoczęcie nowej gry -
    licznik min powinien sie zaktualizować, a pola zresetować.

12. Wpisanie kodu xyzzy, zresetowanie gry - wszystkie pola powinny odzyskać standardowy kolor.

Link do repozytorium na GitHub
https://github.com/piotrnowakowski/Saper_Nowakowski_Piotr.git