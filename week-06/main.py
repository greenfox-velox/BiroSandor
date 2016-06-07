from tkinter import *
from gameboard import *

def main():
    root = Tk()
    canvas = Canvas(root, width = 720, height = 720)
    canvas.pack()

    a = [[1,1,1,0,0,1,1,0,0,1],
        [1,0,1,0,0,1,1,0,0,1],
        [1,1,1,1,1,1,1,0,0,1],
        [1,1,1,0,0,1,1,0,0,1],
        [1,0,1,0,0,1,1,1,1,1],
        [1,1,1,0,0,1,1,0,0,1],
        [1,1,1,0,0,1,1,0,0,1],
        [1,0,1,0,0,1,1,0,1,1],
        [1,0,1,1,1,1,1,0,1,1],
        [1,1,1,0,0,1,1,0,0,1]]
    level1 = Gameboard(canvas, a)
    level1.create_field()
    level1.create_board()


    root.mainloop()

main()
