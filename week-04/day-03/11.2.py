from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

x = 10
y = 10
size = 10

def draw_square(x, y, size):

    while size < 50:
        purpleBox = canvas.create_rectangle(x, y, x+size, y+size, fill = 'purple')
        x = x + size
        y = y + size
        size = size + 10

draw_square(10, 10, 10)




root.mainloop()
