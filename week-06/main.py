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
    hero = Hero(0,0, canvas, a)
    hero.draw_hero_default()
    root.bind('<s>', hero.draw_hero_down)
    root.bind('<w>', hero.draw_hero_up)
    root.bind('<a>', hero.draw_hero_left)
    root.bind('<d>', hero.draw_hero_right)
    boss = Enemy(9,9, canvas)
    skeleton = Enemy(9,0, canvas)
    skeleton2 = Enemy(6,9, canvas)
    skeleton2.draw_skeleton()
    skeleton.draw_skeleton()
    boss.draw_boss()
    root.mainloop()

main()
