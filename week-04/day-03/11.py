# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def random_color():
   r = lambda: random.randint(0,255)
   return ('#%02X%02X%02X' % (r(),r(),r()))


def draw_square(size, color):
    width = 300
    height = 300
    start_point_x = (width / 2) - (size / 2)
    start_point_y = (height / 2) - (size / 2)
    end_point_x = (start_point_x + size)
    end_point_y = (start_point_y + size)
    greenBox = canvas.create_rectangle(start_point_x, start_point_y, end_point_x, end_point_y, fill = color)





for size in range(201, 1, -10):
    draw_square(size, random_color())


root.mainloop()
