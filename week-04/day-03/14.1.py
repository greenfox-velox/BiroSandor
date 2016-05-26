from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=300)

canvas.pack()

for i in range(30):
    canvas.create_line(10*i, 0, 300, 10*i, fill='green')

root.mainloop()
