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
    msg = "Play again?"
    res = messagebox.askyesno("Game Over", message=msg)
    del root, data, main_window
    if res:
        main()
    else:
        quit()
main()


# TODO: losowe rozmieszczenie min

# TODO: kliknięcie w dane pole

# TODO: kliknięcie w bombę

# TODO: kliknięcie w puste pole
# TODO: znikanie tam gdzie nie ma obok bomb
# TODO: wyświetlanie liczby bomb przy polach wolnych na miejscach brzegowych

# TODO: oznaczenie miny
# TODO: drugie kliknięcie zmiana z tu jest na tu może
# TODO: trzecie kliknięcie znika oznaczenie

# TODO: zakończenie gry : oznaczenie wszystkich bomb, kliknięcie wszystkich pustych pól bez miny

# TODO: cheat - kliknięcie x y Z Z y   ściemnienie wszystkich pól gdzie sa bomby


# TODO: TESTY
