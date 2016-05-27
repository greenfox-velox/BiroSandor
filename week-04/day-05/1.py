from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=300)

canvas.pack()

def draw_triangle(x, y, size):
    h = ((3**0.5)/2)
    canvas.create_polygon(x, y, x + size, y, x + size / 2, h * size, fill = 'white', outline = 'black')


def draw_fractal(x, y, size):
    draw_triangle(x, y, size)

    if size > 5:
        h = (((3 ** 0.5) / 2) * size)
        draw_fractal(x, y, size/2)
        draw_fractal(x + size / 2, y, size / 2)
        draw_fractal(x + size / 4, y + h /2, size / 2)


draw_fractal(0, 0, 300)

root.mainloop()
