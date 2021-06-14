import unittest
from tkinter import *
from GUI import *
from data_check import *


class Minesweeper_tests(unittest.TestCase):

#TODO Próba rozpoczęcia gry z rozmiarem planszy i min: (1 na 1; 1), (5 na 1; 2)( 4 na 1; 2)(20 na 500; 12)
# (5 na 6; -4), (3 na 3; 10), (1 na 10; 5) - oczekiwane komunikaty o błędzie.
# Wprowadzenie rozmiarów planszy 8 na 8 i liczby min równej 12 na potrzeby kolejnych testów.
    def testShouldValidateEntry(self):
        """Testuje czy walidacja poprawnie działa dla podanych wartości planszy i min"""
        tests_ans = [
            [[1, 1, 1], "Board size too small"],
            [[5, 1, 2], "Board size too small"],
            [[4, 1, 2], "Board size too small"],
            [[20, 500, 12], "Board size too big"],
            [[5, 6, -4], "Mines number too small"],
            [[3, 3, 10], "Mines number too big"],
            [[1, 10, 5], "Board size too small"],
            [[8, 8, 12], "OK"]
        ]
        root = Tk()
        data = get_data(root)
        for i in tests_ans:
            response_program = data.validate(i[0][0], i[0][1], i[0][2])
            self.assertEqual(i[1], response_program)

#TODO Kliknięcie pola, wyświetla się mina, gra się kończy,
    def testShouldEndWhenClicked(self):
        """Testuje czy przy kliknięciu gra zamknie się"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 1)
        main_window = Main_field(root, data)
        check = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == True:
                    check = tile
        anserw = main_window.onClick(check)
        self.assertEqual(anserw, "Ended")

# TODO Oznaczenie pola jako “tu jest mina” - licznik oznaczonych powinien wzrosnąć o 1,
    def testShoulCountFlags(self):
        """Testuje czy licznik zaktualizuje się po oflagowaniu"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 1)
        main_window = Main_field(root, data)
        check = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        main_window.onRightClick(check)
        self.assertEqual(1, main_window.flagCount)

        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        self.assertEqual(main_window.flagged, check["state"])

#TODO Oznaczenie innego pola jako “tu może być mina”,
    def testShouldCountQuestion(self):
        """Testuje czy przy dwóch kliknięciach zaktualizuje się status pola i ilość oflagowanych pól"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 1)
        main_window = Main_field(root, data)
        check = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        main_window.onRightClick(check)
        main_window.onRightClick(check)
        # czy ilość flag jest równa 0
        self.assertEqual(0, main_window.flagCount)

        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        self.assertEqual(main_window.question, check["state"])

# TODO Oznaczenie pola, odznaczenie go, oznaczenie i odznaczenie licznik oznaczonych powinien sie  aktualizowac
    def testShouldRefreshFlaggedCount(self):
        """Testuje czy przy dwóch kliknięciach zaktualizuje się status pola i ilość oflagowanych pól"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 1)
        main_window = Main_field(root, data)
        check = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        main_window.onRightClick(check)
        self.assertEqual(1, main_window.flagCount)
        main_window.onRightClick(check)
        # czy ilość flag jest równa 0 bo oznaczony jest pytajnik
        self.assertEqual(0, main_window.flagCount)
        main_window.onRightClick(check)
        self.assertEqual(0, main_window.flagCount)

        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        self.assertEqual(main_window.nonclicked, check["state"])

# TODO Wygranie gry przez klikniecie wszystkich pól bez min,
    def testShouldEndWhenAllClicked(self):
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 2)
        main_window = Main_field(root, data)
        anserw = 0

        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == False and tile["state"] == main_window.nonclicked:
                    anserw = main_window.onClick(tile)
                    if anserw == "Ended":
                        self.assertEqual(anserw, "Ended")



# TODO Wygranie gry przez oznaczenie wszystkich pól z minami
    def testShouldEndWhenAllFlagged(self):
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 2)
        main_window = Main_field(root, data)
        anserw = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == True and tile["state"] != main_window.flagged:
                    anserw = main_window.onRightClick(tile)
                    if anserw == "Ended":
                        self.assertEqual(anserw, "Ended")

# TODO Próba oznaczenia sprawdzonego pola - oczekiwane niepowodzenie,
    def testShouldNotCountFlags(self):
        """Testuje czy licznik oznaczeń nie wzrośnie po kliknięciu na sprawdzone pole"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 1)
        main_window = Main_field(root, data)
        check = 0
        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        if tile["isMine"] == False:
            main_window.onClick(check)
        main_window.onRightClick(check)
        self.assertEqual(0, main_window.flagCount)

        for i in main_window.tiles.values():
            for tile in i.values():
                check = tile
        self.assertEqual(main_window.clicked, check["state"])

# TODO oznaczenie pól “tu jest mina’, rozpoczęcie nowej gry - licznik min powinien sie zaktualizować, a pola zresetować.
    def testShoulZerodFlagCounts(self):
        """Testuje czy po oznaczeniu flag i resecie liczniki i pola zresetują się"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 3)
        main_window = Main_field(root, data)
        main_window.onRightClick(main_window.tiles[1][1])
        main_window.onRightClick(main_window.tiles[2][2])
        self.assertEqual(2, main_window.flagCount)

        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == False:
                    main_window.onClick(tile)
        main_window.reset()
        for i in main_window.tiles.values():
            for tile in i.values():
                self.assertEqual(tile["state"], main_window.nonclicked)
        self.assertEqual(0, main_window.flagCount)

# TODO Wpisanie kodu xyzzy, zresetowanie gry - wszystkie pola powinny odzyskać standardowy kolor.
    def testCheatResetWork(self):
        """Testuje czy po uruchomieniu cheatu i resecie pola wróca na standardowy kolor"""
        root = Tk()
        data = get_data(root)
        data.validate(5, 5, 2)
        main_window = Main_field(root, data)
        main_window.cheat()
        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == True:
                    self.assertEqual(tile["state"], main_window.cheat_tile)
        main_window.reset()
        for i in main_window.tiles.values():
            for tile in i.values():
                if tile["isMine"] == True:
                    self.assertEqual(tile["state"], main_window.nonclicked)
