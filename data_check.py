from tkinter import *
from tkinter import messagebox
import tkinter
import keyboard

class get_data():
    def __init__(self, tk):
        global width_var
        width_var = tkinter.StringVar()
        global len_var
        len_var = tkinter.StringVar()
        global mines_var
        mines_var = tkinter.StringVar()

        entry_box_width = Entry(tk, textvariable=width_var, width=50)
        entry_box_width.pack()
        entry_box_width.insert(5, "Width")

        entry_box_len = Entry(tk, textvariable=len_var, width=50)
        entry_box_len.pack()
        entry_box_len.insert(5, "Length")

        entry_box_mines = Entry(tk, textvariable=mines_var, width=50)
        entry_box_mines.pack()
        entry_box_mines.insert(5, "Mines")
        self.width = 0
        self.len_ = 0
        self.mines = 0
        self.tk = tk
        Button(tk, text="Start Game", command=lambda: [self.get_attributes()]).pack()

    def get_attributes(self):
        """Sprawdza poprawność wprowadzonych danych, jeśli poprawne zamyka okno wprowadzania i uruchamia okno gry"""
        res = self.validate(len_var.get(), width_var.get(), mines_var.get())
        if res == "OK":
            self.tk.destroy()
        else:
            messagebox.showinfo(message=res)

    def validate(self, len_, width, mines):
        try:
            width = int(width)
            len_ = int(len_)
            mines = int(mines)
            if mines < 0:
                raise ValueError("Mines number too small")
            if len_ * width > 15**2:
                raise ValueError("Board size too big")
            if len_ * width <= 4 or len_ == 1 or width == 1:
                raise ValueError("Board size too small")
            if mines > len_ * width:
                print(mines, len_ * width)
                raise ValueError("Mines number too big")
            self.width = width
            self.len_ = len_
            self.mines = mines
            return "OK"
        except ValueError as er:
            return er.args[0]
        except EXCEPTION as ex:
            return ex.args[0]
