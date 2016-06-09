from tkinter import *
from character import *

class Hero(Character):
    def __init__(self, x,y):
        super().__init__(0,0)
        # self.health
        # self.defend
        # self.strike

    def hero_default(self):
        self.img = PhotoImage(file = 'pics/hero-down.png')

    def hero_down(self):
        self.img = PhotoImage(file = 'pics/hero-down.png')
        self.y += 1

    def hero_up(self):
        self.img = PhotoImage(file = 'pics/hero-up.png')
        self.y -= 1

    def hero_left(self):
        self.img = PhotoImage(file = 'pics/hero-left.png')
        self.x -= 1

    def hero_right(self):
        self.img = PhotoImage(file = 'pics/hero-right.png')
        self.x += 1
