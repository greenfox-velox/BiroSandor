from tkinter import *
from gameboard import *
from character import *
from levels import *

def main():
    root = Tk()
    canvas = Canvas(root, width = 800, height = 600)
    canvas.pack()

    level1 = Gameboard(canvas)
    root.bind('<KeyPress>', level1.keypress)

    root.mainloop()

main()
