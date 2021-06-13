from tkinter import *
import numpy as np
from collections import deque
from tkinter import messagebox


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
            "wrong": PhotoImage(file="images/tile_wrong.gif"),
            "1": PhotoImage(file="images/tile_1.gif"),
            "2": PhotoImage(file="images/tile_2.gif"),
            "3": PhotoImage(file="images/tile_3.gif"),
            "4": PhotoImage(file="images/tile_4.gif"),
            "5": PhotoImage(file="images/tile_5.gif"),
            "6": PhotoImage(file="images/tile_6.gif"),
            "7": PhotoImage(file="images/tile_7.gif"),
            "8": PhotoImage(file="images/tile_8.gif")
        }

        self.tiles = dict({})
        self.mines = 0
        self.x = None
        self.y = None
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.buttons = []

        self.nonclicked = 0
        self.clicked = 1
        self.flagged = 2
        self.question = 3
        self.clickedCount = 0
        self.correctFlagCount = 0
        self.flagCount = 0
        self.labels = {
            "mines": Label(self.frame, text="Mines: 0"),
            "flags": Label(self.frame, text="Flags: 0")
        }
        #
        self.start_game()

    # TODO: rozpoczęcie nowej gry
    def start_game(self):
        self.frame.pack()
        self.buttons = []
        self.tiles = dict({})
        self.mines = 0
        self.x = None
        self.y = None
        self.clickedCount = 0
        self.correctFlagCount = 0
        self.flagCount = 0
        self.labels = {
            "mines": Label(self.frame, text="Mines: 0"),
            "flags": Label(self.frame, text="Flags: 0")
        }
        self.labels["mines"].grid(row=self.data.len_ + 1,
                                  column=0, columnspan=int(self.data.width / 2))
        self.labels["flags"].grid(row=self.data.len_ + 1, column=int(self.data.width / 2) - 1,
                                  columnspan=int(self.data.width / 2))

        foobar = np.full((self.data.width, self.data.len_), False)
        # creating list of indices
        idx = []
        for i in range(self.data.mines):
            idx.append([np.random.randint(self.data.width), np.random.randint(self.data.len_)])
        # replace F by T at  indices from idx
        for x in range(0, self.data.width):
            for y in range(0, self.data.len_):
                if [x, y] in idx:
                    foobar[x][y] = True

        for x in range(0, self.data.width):
            for y in range(0, self.data.len_):
                if y == 0:
                    self.tiles[x] = {}
                id = str(x) + "_" + str(y)
                isMine = False

                gfx = self.images["plain"]
                if foobar[x, y]:
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
                tile["button"].bind("<Button-3>", self.onRightClickWrapper(x, y))
                tile["button"].grid(row=x + 1, column=y)  # offset by 1 row for timer
                self.tiles[x][y] = tile

        for a in range(0, self.data.width):
            for b in range(0, self.data.len_):
                mc = 0
                for n in self.getNeighbors(a, b):
                    if n["isMine"]:
                        mc += 1

                self.tiles[a][b]["mines"] = mc

    def onClickWrapper(self, x, y):
        return lambda Button: self.onClick(self.tiles[x][y])

    def onRightClickWrapper(self, x, y):
        return lambda Button: self.onRightClick(self.tiles[x][y])

    def onClick(self, tile):
        if tile["isMine"] == True:
            # end game
            self.gameOver(False)
            return
        # change image
        if tile["mines"] == 0:
            tile["button"].config(image=self.images["click"])
            self.clearSurroundingTiles(tile["id"])
        else:
            tile["button"].config(image=self.images[str(tile["mines"])])

        if tile["state"] == self.clicked:
            tile["state"] = self.clicked
            self.clickedCount += 1
        if self.clickedCount == (self.data.len_ * self.data.width) - self.mines:
            self.gameOver(True)

    def onRightClick(self, tile):
        # if not clicked
        if tile["state"] == self.nonclicked:
            tile["button"].config(image=self.images["flag"])
            tile["state"] = self.flagged
            #tile["button"].unbind("<Button-1>")
            # if a mine
            if tile["isMine"] == True:
                self.correctFlagCount += 1
            self.flagCount += 1
            if self.correctFlagCount == self.mines:
                self.gameOver(True)
            self.refreshLabels()
        # if flagged, unflag
        elif tile["state"] == self.flagged:
            tile["button"].config(image=self.images["question"])
            tile["button"].bind(self.clicked, self.onClickWrapper(tile["coords"]["x"], tile["coords"]["y"]))
            tile["state"] = self.question
            self.refreshLabels()

        elif tile["state"] == self.question:
            tile["button"].config(image=self.images["plain"])
            tile["state"] = self.nonclicked
            tile["button"].bind(self.clicked, self.onClickWrapper(tile["coords"]["x"], tile["coords"]["y"]))
            # if a mine
            if tile["isMine"] == True:
                self.correctFlagCount -= 1
            self.flagCount -= 1
            self.refreshLabels()


    def clearSurroundingTiles(self, id):
        queue = deque([id])
        while len(queue) != 0:
            key = queue.popleft()
            parts = key.split("_")
            x = int(parts[0])
            y = int(parts[1])
        # Dodaje sobie obiekty do sąsiadów
            for tile in self.getNeighbors(x, y):
                self.clearTile(tile, queue)

    def clearTile(self, tile, queue):
        if tile["state"] != self.nonclicked:
            return

        if tile["mines"] == 0:
            tile["button"].config(image=self.images["click"])
            queue.append(tile["id"])
        else:
            tile["button"].config(image=self.images[str(tile["mines"] )])

        tile["state"] = self.clicked
        self.clickedCount += 1

    def restart(self):
        self.start_game()
        self.refreshLabels()

    def refreshLabels(self):
        self.labels["flags"].config(text="Flags: " + str(self.flagCount))
        self.labels["mines"].config(text="Mines: " + str(self.mines))

    def getNeighbors(self, x, y):
        neighbors = []
        coords = [
            {"x": x-1,  "y": y-1},  #top right
            {"x": x-1,  "y": y},    #top middle
            {"x": x-1,  "y": y+1},  #top left
            {"x": x,    "y": y-1},  #left
            {"x": x,    "y": y+1},  #right
            {"x": x+1,  "y": y-1},  #bottom right
            {"x": x+1,  "y": y},    #bottom middle
            {"x": x+1,  "y": y+1},  #bottom left
        ]
        for n in coords:
            try:
                neighbors.append(self.tiles[n["x"]][n["y"]])
            except KeyError:
                pass
        return neighbors

    def gameOver(self, won):
        for x in range(0, self.data.len_):
            for y in range(0, self.data.width):
                if self.tiles[x][y]["isMine"] == False and self.tiles[x][y]["state"] == self.flagged:
                    self.tiles[x][y]["button"].config(image=self.images["wrong"])

                if self.tiles[x][y]["isMine"] == True and self.tiles[x][y]["state"] != self.flagged:
                    self.tiles[x][y]["button"].config(image=self.images["mina"])
        msg = "You Win!" if won else "You Lose!"
        messagebox.showinfo(msg)
        self.tk.update()
        self.frame.destroy()
        self.tk.destroy()
