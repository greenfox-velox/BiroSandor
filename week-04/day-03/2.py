# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

redLine = canvas.create_line(100, 150, 150, 150, fill = 'red')
blueLine = canvas.create_line(150, 150, 150, 200, fill = 'blue')
yellowLine = canvas.create_line(100, 200, 150, 200, fill = 'yellow')
greenLine = canvas.create_line(100, 200, 100, 150, fill = 'green')

root.mainloop()
