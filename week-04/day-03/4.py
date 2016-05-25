# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def line_drawer(x, y):
    blackLine = canvas.create_line(150, 150, x, y)

line_drawer(50, 100)
line_drawer(100, 150)


root.mainloop()
