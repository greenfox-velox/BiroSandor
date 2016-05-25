# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

greenBox = canvas.create_rectangle(0, 0, 200, 100, fill = 'green')
yellowBox = canvas.create_rectangle(200, 0, 300, 100, fill = 'yellow')
redBox = canvas.create_rectangle(0, 100, 200, 300, fill = 'red')
blueBox = canvas.create_rectangle(200, 100, 300, 300, fill = 'blue')



root.mainloop()
