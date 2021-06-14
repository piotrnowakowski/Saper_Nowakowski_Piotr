# This is a sample Python script.
from tkinter import *
from GUI import *
from data_check import *
from tkinter import messagebox

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    root = Tk()
    data = get_data(root)
    root.mainloop()
    del root
    root = Tk()
    main_window = Main_field(root, data)
    root.mainloop()
    quit()
main()

# TODO: cheat - kliknięcie x y Z Z y   ściemnienie wszystkich pól gdzie sa bomby


# TODO: TESTY
