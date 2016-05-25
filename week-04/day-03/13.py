from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()
canvas_size = 300
half = canvas_size // 2

for i in range(0, half + 1, 10):
    canvas.create_line(i, half, half, half-i)
    canvas.create_line(canvas_size - i, half, half, half-i)
    canvas.create_line(i, half, half, half+i)
    canvas.create_line(canvas_size - i, half, half, half+i)

root.mainloop()
