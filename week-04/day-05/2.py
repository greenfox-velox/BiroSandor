from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=300)

canvas.pack()

def draw_hexa(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    canvas.create_polygon(x + size / 2, y, x + (size / 2 + size), y, x + 2 * size, y + h, x + (size / 2 + size), y + 2 * h, x + size / 2, y + 2 * h, x, y + h, fill = 'white', outline = 'black')


def draw_fractal(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    draw_hexa(x, y, size)

    if size > 5:
        draw_fractal(x + size / 3, y, size / 3)
        draw_fractal(x + size, y, size / 3)
        draw_fractal(x + size / 3, y + h + h / 3, size / 3)
        draw_fractal(x + size, y + h + h / 3, size / 3)
        draw_fractal(x, y + 2 * (h / 3), size / 3)
        draw_fractal(x+ size + size / 3, y + 2 * (h / 3), size / 3)

draw_fractal(5, 5, 150)


root.mainloop()
