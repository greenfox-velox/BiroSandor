from tkinter import *

class Character():
    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x=x
        self.y=y

    def draw(self, img):
        self.canvas.create_image(self.x*72,self.y*72,image=img, anchor=NW)

class Hero(Character):
    def __init__(self, x,y, canvas):
        super().__init__(0,0, canvas)

    def draw_hero_default(self):
        self.img = PhotoImage(file = 'hero-down.png')
        super().draw(self.img)

    def draw_hero_down(self, event):
        self.img = PhotoImage(file = 'hero-down.png')
        if self.y + 1 <= 9:
            self.y += 1
        super().draw(self.img)

    def draw_hero_up(self, event):
        self.img = PhotoImage(file = 'hero-up.png')
        if self.y -1 >= 0:
            self.y -= 1
        super().draw(self.img)

    def draw_hero_left(self, event):
        self.img = PhotoImage(file = 'hero-left.png')
        if self.x -1 >= 0:
            self.x -= 1
        super().draw(self.img)

    def draw_hero_right(self, event):
        self.img = PhotoImage(file = 'hero-right.png')
        if self.x +1 <= 9:
            self.x += 1
        super().draw(self.img)

# class Boss():
#     def __init__(self, x,y, canvas):
#         self.canvas = canvas
#         self.x=x
#         self.y=y
#
#     def draw_boss(self):
#         self.img = PhotoImage(file = 'boss.png')
#         self.canvas.create_image(self.x,self.y,image=self.img, anchor=NW)
