# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

def draw_lines(x, y):
    canvas.create_line(x, y, 150, 150)

# for i in range(0, 301, 20):
#     x = 0
#     y = 0
#     canvas.create_line(x, y+i, 150, 150)
#     canvas.create_line(x+i, y, 150, 150)
# for j in range(0, 301, 20):
#     x = 300
#     y = 300
#     canvas.create_line(x, y-j, 150, 150)
#     canvas.create_line(x-j, y, 150, 150)

for i in range(16):
    x=i*20
    y=i*20
    draw_lines(0, y)
    draw_lines(x, 0)
    draw_lines(300, y)
    draw_lines(x, 300)

draw_lines(0, 0)


root.mainloop()
