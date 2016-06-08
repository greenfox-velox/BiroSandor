from tkinter import *
from gameboard import *
from character import *

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
    hero = Hero(0,0, canvas)
    hero.draw_hero_default()
    root.bind('<Down>', hero.draw_hero_down)
    root.bind('<Up>', hero.draw_hero_up)
    root.bind('<Left>', hero.draw_hero_left)
    root.bind('<Right>', hero.draw_hero_right)


    root.mainloop()

main()
