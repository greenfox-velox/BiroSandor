from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600, bg= 'yellow')
canvas.pack()


def draw_rectangle_fractal(x, y, size):
    canvas.create_rectangle(x + size, y, x + 2 * size, y + size)
    canvas.create_rectangle(x, y + size, x + size, y + 2 * size)
    canvas.create_rectangle(x + size, y + size, x + 2 * size, y + 2 * size)
    canvas.create_rectangle(x + 2 * size, y + size, x + 3 * size, y + 2 * size)
    canvas.create_rectangle(x + size, y + 2 * size, x + 2 * size, y + 3 * size)

    if size < 3:
        pass
    else:
        draw_rectangle_fractal(x+size, y, size/3)
        draw_rectangle_fractal(x, y + size, size/3)
        draw_rectangle_fractal(x + 2 * size, y + size, size/3)
        draw_rectangle_fractal(x +size, y + 2* size, size / 3)



draw_rectangle_fractal(0, 0, 200)


root.mainloop()
