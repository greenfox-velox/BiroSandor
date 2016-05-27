from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600, bg= 'yellow')
canvas.pack()

# def fractal(x, y, size):
#
#
#     canvas.create_rectangle(x+size/3, y, x+2*(size/3), y+size/3)
#     canvas.create_rectangle(x, y+size/3, x+size/3, y+2*(size/3))
#     canvas.create_rectangle(x+size/3, y+size/3, x+2*(size/3), y+2*(size/3))
#     canvas.create_rectangle(x+2*(size/3), y+size/3, x+size, y+2*(size/3))
#     canvas.create_rectangle(x+size/3, y+2*(size/3), x+2*(size/3), y+size)
#
#     if size < 3:
#         pass
#     else:
#         fractal(x, y, size/3)
#         fractal(x+200, y, size/3)
#         fractal(x+400, y+200, size/3)
#
# fractal(0, 0, 600)


def fractal(x, y, size):
    canvas.create_rectangle(x + size, y, x + 2 * size, y + size)
    canvas.create_rectangle(x, y + size, x + size, y + 2 * size)
    canvas.create_rectangle(x + size, y + size, x + 2 * size, y + 2 * size)
    canvas.create_rectangle(x + 2 * size, y + size, x + 3 * size, y + 2 * size)
    canvas.create_rectangle(x + size, y + 2 * size, x + 2 * size, y + 3 * size)

    if size < 3:
        pass
    else:
        fractal(x+size, y, size/3)
        fractal(x, y + size, size/3)
        fractal(x + 2 * size, y + size, size/3)
        fractal(x +size, y + 2* size, size / 3)



fractal(0, 0, 200)


root.mainloop()
