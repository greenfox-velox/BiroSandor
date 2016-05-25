# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def draw_square(x):
    width = 300
    height = 300
    start_point_x = (width / 2) - (x / 2)
    start_point_y = (height / 2) - (x / 2)
    end_point_x = (start_point_x + x)
    end_point_y = (start_point_y + x)
    greenBox = canvas.create_rectangle(start_point_x, start_point_y, end_point_x, end_point_y)

draw_square(20)
draw_square(100)
draw_square(200)


root.mainloop()
