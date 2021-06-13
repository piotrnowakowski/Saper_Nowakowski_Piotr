import unittest
from tkinter import *
from GUI import *
from data_check import *


class Minesweeper_tests(unittest.TestCase):

#TODO Próba rozpoczęcia gry z rozmiarem planszy i min: (1 na 1; 1), (5 na 1; 2)( 4 na 1; 2)(20 na 500; 12)
# (5 na 6; -4), (3 na 3; 10), (1 na 10; 5) - oczekiwane komunikaty o błędzie.
# Wprowadzenie rozmiarów planszy 8 na 8 i liczby min równej 12 na potrzeby kolejnych testów.
    def testShouldValidateEntry(self):
        root = Tk()
        data = get_data(root)
        root.mainloop()


#TODO Kliknięcie pola, wyświetla się liczba min w sąsiedztwie pola,

#TODO Kliknięcie pola, wyświetla się mina, gra się kończy,

#TODO Klikniecie pola, brak min w sąsiedztwie - oczekiwane automatyczne sprawdzenie sąsiadów aż do wyznaczenia obszaru wyznaczonego przez pola sąsiadujące z minami lub krawędzie planszy,

#TODO Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnaé o 1,

#TODO Oznaczenie innego pola jako “tu może być mina”,

#TODO Oznaczenie pola, odznaczenie go, ponowne oznaczenie i ponowne odznaczenie licznik oznaczonych powinien sie
# odpowiednio aktualizowac

#TODO Wygranie gry przez klikniecie wszystkich pól bez min,

#TODO Wygranie gry przez oznaczenie wszystkich pól z minami (można skorzystać z kodu xyzzy),

#TODO Próba oznaczenia sprawdzonego pola - oczekiwane niepowodzenie,

#TODO Sprawdzenie kilku pól bez min, oznaczenie pól “tu jest mina’,
# rozpoczęcie nowej gry - licznik min powinien sie zaktualizować, a pola zresetować.

#TODO Wpisanie kodu xyzzy, zresetowanie gry - wszystkie pola powinny odzyskać standardowy kolor.

