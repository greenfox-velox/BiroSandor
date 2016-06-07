from tkinter import *
from images import Images

class Gameboard():
    def __init__(self, canvas,a):
        self.canvas = canvas
        self.images=Images()
        self.a = a

    def start(self):
        self.create_field()
        self.create_hero()

    def create_field(self):
        for row_numbers in range(10):
            for column_numbers in range(10):
                if self.a[row_numbers][column_numbers] == 1:
                    self.canvas.create_image(column_numbers*72, row_numbers*72, image=self.images.floor, anchor=NW)
                else:
                    self.canvas.create_image(column_numbers*72,row_numbers*72, image=self.images.wall, anchor=NW)

    def create_hero(self):
        self.canvas.create_image(0,0, image=self.images.hero_down, anchor=NW)

    # def create_monster(self):
    # def create_boss(self):
