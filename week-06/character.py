from tkinter import *

class Character():
    def __init__(self, x, y):
        self.size = 60
        self.x=x
        self.y=y

    def draw(self, canvas):
        canvas.create_image(self.x*self.size,self.y*self.size ,image=self.img, anchor=NW)
