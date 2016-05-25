# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def line_drawer(x, y):
    blackLine = canvas.create_line(x, y, x + 50, y)

line_drawer(50, 100)
line_drawer(100, 150)
line_drawer(150, 200)



root.mainloop()
