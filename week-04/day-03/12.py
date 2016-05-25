# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=320, height=320)
canvas.pack()
# x = 0
#
#
# for i in range(0, 240, 40):
#     for j in range(8):
#         if box % 2 == 0:
#             blackBox = canvas.create_rectangle(x + y, y, x + 40, y + 40, fill = 'black')
#             x = x + 40
#
#         else:
#             blackBox = canvas.create_rectangle(x + y, y, x + 40, y + 40, fill = 'green')
#             x = x + 40
#
#
#
#


canvas_size = 320
size = canvas_size / 8


for i in range(8):
    for j in range(8):
        x = i * size
        y = j * size
        color = 'white'
        if (i + j) % 2 == 0:
            color = 'black'
        canvas.create_rectangle(x, y, x + size, y + size, fill = color)


root.mainloop()
