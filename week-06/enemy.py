from tkinter import *
from character import *



class Enemy(Character):
    def __init__(self, x,y):
        super().__init__(x,y)

    def boss(self):
        self.img = PhotoImage(file = 'pics/boss.png')

    def skeleton(self):
        self.img = PhotoImage(file = 'pics/skeleton.png')
