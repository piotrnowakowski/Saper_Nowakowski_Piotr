from tkinter import *
import tkinter

class get_data():
    def __init__(self, tk):
        global width_var
        width_var = tkinter.StringVar()
        global len_var
        len_var = tkinter.StringVar()
        global mines_var
        mines_var = tkinter.StringVar()

        # TODO: 2 pola tekstowe planszy do wprowadzania rozmiarów i 1 na wprowadzenie min
        entry_box_width = Entry(tk, textvariable=width_var, width=50)
        entry_box_width.pack()
        entry_box_width.insert(0, 0)

        entry_box_len = Entry(tk, textvariable=len_var, width=50)
        entry_box_len.pack()
        entry_box_len.insert(0, 0)

        entry_box_mines = Entry(tk, textvariable=mines_var, width=50)
        entry_box_mines.pack()
        entry_box_mines.insert(0, 0)
        self.width = 0
        self.len_ = 0
        self.mines = 0
        Start_game_button = Button(tk, text="Start Game", command=[self.get_attributes(), tk.destroy]).pack()

    def get_attributes(self):
        try:
            width = int(width_var.get())
            len_ = int(len_var.get())
            mines = int(mines_var.get())
            if mines < 0:
                raise ValueError("Mines number too small")
            if len_ > 15 and width > 15:
                raise ValueError("Board size too big")
            elif len_ < 2 and width < 2:
                raise ValueError("Board size too small")
            if mines > len_ * width:
                raise ValueError("Mines number too big")
            self.width = width
            self.len_ = len_
            self.mines = mines
        except ValueError as er:
            print(er)
        except EXCEPTION as ex:
            print(ex)
