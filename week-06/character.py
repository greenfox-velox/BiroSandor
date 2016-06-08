from tkinter import *

class Character():
    def __init__(self, x, y, canvas,a):
        self.size = 72
        self.a = a
        self.canvas = canvas
        self.x=x
        self.y=y

    def draw(self, img):
        self.canvas.create_image(self.x*self.size,self.y*self.size,image=img, anchor=NW)

class Hero(Character):
    def __init__(self, x,y, canvas, a):
        super().__init__(0,0, canvas, a)

    def draw_hero_default(self):
        self.img = PhotoImage(file = 'hero-down.png')
        super().draw(self.img)

    def draw_hero_down(self, event):
        self.img = PhotoImage(file = 'hero-down.png')
        if self.y + 1 <= 9:
            if self.a[self.y + 1][self.x] == 1:
                self.y += 1
        super().draw(self.img)

    def draw_hero_up(self, event):
        self.img = PhotoImage(file = 'hero-up.png')
        if self.y -1 >= 0:
            if self.a[self.y - 1][self.x] == 1:
                self.y -= 1
        super().draw(self.img)

    def draw_hero_left(self, event):
        self.img = PhotoImage(file = 'hero-left.png')
        if self.x -1 >= 0:
            if self.a[self.y][self.x - 1] == 1:
                self.x -= 1
        super().draw(self.img)

    def draw_hero_right(self, event):
        self.img = PhotoImage(file = 'hero-right.png')
        if self.x +1 <= 9:
            if self.a[self.y][self.x+1] == 1:
                self.x += 1
        super().draw(self.img)

class Enemy():
    def __init__(self, x,y, canvas):
        self.size = 72
        self.canvas = canvas
        self.x=x
        self.y=y

    def draw_boss(self):
        self.img = PhotoImage(file = 'boss.png')
        self.canvas.create_image(self.x*self.size,self.y*self.size,image=self.img, anchor=NW)

    def draw_skeleton(self):
        self.img = PhotoImage(file = 'skeleton.png')
        self.canvas.create_image(self.x*self.size,self.y*self.size,image=self.img, anchor=NW)
