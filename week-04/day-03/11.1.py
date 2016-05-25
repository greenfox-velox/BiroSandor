from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()



def draw_square(x, y, size):
    for i in range(1, 20):

        purpleBox = canvas.create_rectangle(x*i, y*i, x+(size*i), y+(size*i), fill = 'purple')

draw_square(10, 10, 10)




root.mainloop()
