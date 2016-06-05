from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600, bg='yellow')
canvas.pack()

def draw_triangle(x, y, size):
    h = ((3**0.5)/2)
    canvas.create_polygon(x, y, x + size, y,
                        x + size / 2, y + h * size,
                            fill = 'yellow', outline = 'black')

def draw_triangle_fractal(x, y, size):
    draw_triangle(x, y, size)

    if size > 5:
        h = (((3 ** 0.5) / 2) * size)
        draw_triangle_fractal(x, y, size / 2)
        draw_triangle_fractal(x + size / 2, y, size / 2)
        draw_triangle_fractal(x + size / 4, y + h / 2, size / 2)


draw_triangle_fractal(0, 0, 600)
root.mainloop()
