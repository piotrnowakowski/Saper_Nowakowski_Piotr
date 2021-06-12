from tkinter import *
import random

# TODO: plansza generowana na podstawie pól

# TODO: liczba oznaczonych pól
# TODO: wprowadzenie ile min na planszy


class Main_field():
    def __init__(self, tk, data):
        self.data = data
        # images import
        self.images = {
            "plain": PhotoImage(file="images/tile_plain.gif"),
            "click": PhotoImage(file="images/tile_clicked.gif"),
            "mina": PhotoImage(file="images/tile_mine.gif"),
            "question": PhotoImage(file="images/tile_question.gif"),
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

        self.x = None
        self.y = None
        self.tk = 0
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.buttons = []
        Start_game_button = Button(tk, text="Start Game", command=[self.get_attributes(), self.start_game(tk, width, len_, mines)])
        Start_game_button.pack()

    # TODO: rozpoczęcie nowej gry
    def start_game(self, tk, width, len_, mines):
        window = Toplevel(tk)
        Label(window, text="Window game").pack()
        self.tk = window
        self.frame = Frame(self.tk)
        self.frame.pack()
        # TODO: obsługa wyjątków gdy pole mniejsze od 2x2 lub większe od 15x15


        self.labels = {
            "time": Label(self.frame, text = "00:00:00"),
            "mines": Label(self.frame, text = "Mines: 0"),
            "flags": Label(self.frame, text = "Flags: 0")
        }



        self.labels["time"].grid(row=0, column=0)  # top full width
        self.labels["mines"].grid(row=len_+1, column=0, columnspan=int(width/2))  # bottom left
        self.labels["flags"].grid(row=len_+1, column=int(width/2)-1, columnspan=int(width/2))  # bottom right
        self.tiles = dict({})
        self.mines = 0

        for x in range(0, width):
            for y in range(0, len_):
                if y == 0:
                    self.tiles[x] = {}

                id = str(x) + "_" + str(y)
                isMine = False

                # tile image changeable for debug reasons:
                gfx = self.images["plain"]

                # currently random amount of mines
                if random.uniform(0.0, 1.0) < 0.1:
                    isMine = True
                    self.mines += 1

                tile = {
                    "id": id,
                    "isMine": isMine,
                    "state": 0,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "button": Button(self.frame, image=gfx),
                    "mines": 0
                }

                tile["button"].bind("<Button-1>", self.onClickWrapper(x, y))
                tile["button"].bind("<Button-2>", self.onRightClickWrapper(x, y))
                tile["button"].grid(row=x + 1, column=y)  # offset by 1 row for timer

                self.tiles[x][y] = tile

    def onClickWrapper(self, x, y):
        return lambda Button: self.onClick(self.tiles[x][y])

    def onRightClickWrapper(self, x, y):
        return lambda Button: self.onRightClick(self.tiles[x][y])