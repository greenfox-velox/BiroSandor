# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def draw_square(size):
    width = 300
    height = 300
    start_point_x = (width / 2) - (size / 2)
    start_point_y = (height / 2) - (size / 2)
    end_point_x = (start_point_x + size)
    end_point_y = (start_point_y + size)
    greenBox = canvas.create_rectangle(start_point_x, start_point_y, end_point_x, end_point_y)



for size in range(1, 201, 10):
    draw_square(size)


root.mainloop()
