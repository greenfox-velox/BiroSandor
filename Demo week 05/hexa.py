from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600, bg='yellow')
canvas.pack()

def draw_hexa(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    canvas.create_polygon(x + size / 2, y, x + (size / 2 + size), y, x + 2 * size, y + h, x + (size / 2 + size), y + 2 * h, x + size / 2, y + 2 * h, x, y + h, fill = 'yellow', outline = 'black')

def draw_hexa_fractal(x, y, size):
    h = (((3 ** 0.5) / 2) * size)
    draw_hexa(x, y, size)

    if size > 5:
        draw_hexa_fractal(x + size / 3, y, size / 3)
        draw_hexa_fractal(x + size, y, size / 3)
        draw_hexa_fractal(x + size / 3, y + h + h / 3, size / 3)
        draw_hexa_fractal(x + size, y + h + h / 3, size / 3)
        draw_hexa_fractal(x, y + 2 * (h / 3), size / 3)
        draw_hexa_fractal(x+ size + size / 3, y + 2 * (h / 3), size / 3)

draw_hexa_fractal(5, 5, 300)
root.mainloop()
