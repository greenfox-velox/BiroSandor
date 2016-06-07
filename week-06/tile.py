from tkinter import *

class Tile():
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.create_image(self.y*72, self.x*72, image=self.img, anchor=NW)

class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file='floor.png')

        # def draw(self):
        #     super().draw(self.floor_img)

class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file='wall.png')

    # def draw(self):
    #     super().draw(self.wall_img)
