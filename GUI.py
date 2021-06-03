from tkinter import *


# TODO: plansza generowana na podstawie pól

# TODO: liczba oznaczonych pól

# TODO: wprowadzenie ile min na planszy

# TODO: rozpoczęcie nowej gry
class Main_field():
    def __init__(self, tk):
        # images import
        self.images = {
            "plain": PhotoImage(file="images/tile_plain.gif"),
            "click": PhotoImage(file="images/tile_clicked.gif"),
            "mina": PhotoImage(file="images/tile_mine.gif"),
            "question":PhotoImage(file="images/tile_question.gif"),
            "flag": PhotoImage(file="images/tile_flag.gif"),
            "1": PhotoImage(file="images/tile_1.gif"),
            "2": PhotoImage(file="images/tile_2.gif"),
            "3": PhotoImage(file="images/tile_3.gif"),
            "4": PhotoImage(file="images/tile_4.gif"),
            "5": PhotoImage(file="images/tile_5.gif"),
            "6": PhotoImage(file="images/tile_6.gif"),
            "7": PhotoImage(file="images/tile_7.gif"),
            "8": PhotoImage(file="images/tile_8.gif")
        }
        # TODO: 2 pola tekstowe planszy do wprowadzania rozmiarów i 1 na wprowadzenie min
        # TODO: obsługa wyjątków gdy pole mniejsze od 2x2 lub większe od 15x15
        root = Tk()
        entry_box_width = Entry(root, width=50)
        entry_box_width.pack()
        entry_box_len = Entry(root, width=50)
        entry_box_len.pack()
        entry_box_mines = Entry(root, width=50)
        entry_box_mines.pack()
        self.x = None
        self.y = None
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        Start_game_button = Button(root, text="Start Game", function=self.start_game(entry_box_width, entry_box_len, entry_box_mines))

        root.mainloop()

    def start_game(self, entry_width, entry_len, entry_mines):
        # set up labels/UI
        try:
            width = int(entry_width.get())
            len = int(entry_len.get())
            mines = int(entry_mines.get())
            if mines < 0:
                raise ValueError("Too small")
            if len > 15 and width >15:
                raise ValueError("Too big")
            elif len < 2 and width < 2:
                raise ValueError("Too small")
            if mines > len*width:
                raise ValueError("Too big")

        except ValueError as er:
            print(er)
        except EXCEPTION as ex:
            print(ex)





        self.labels = {
            "time": Label(self.frame, text = "00:00:00"),
            "mines": Label(self.frame, text = "Mines: 0"),
            "flags": Label(self.frame, text = "Flags: 0")
        }
        self.labels["time"].grid(row = 0, column = 0) # top full width
        self.labels["mines"].grid(row = SIZE_X+1, column = 0, columnspan = int(SIZE_Y/2)) # bottom left
        self.labels["flags"].grid(row = SIZE_X+1, column = int(SIZE_Y/2)-1, columnspan = int(SIZE_Y/2)) # bottom right