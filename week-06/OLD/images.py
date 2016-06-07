from tkinter import *

class Images():
    def __init__(self):
        self.floor = PhotoImage(file='floor.png')
        self.wall = PhotoImage(file='wall.png')
        self.hero_down = PhotoImage(file='hero-down.png')
        self.hero_up = PhotoImage(file='hero-up.png')
        self.hero_left = PhotoImage(file='hero-left.png')
        self.hero_right = PhotoImage(file='hero-right.png')
