from tkinter import *


root = Tk()

canvas = Canvas(root, width=300, height=300, bg= 'yellow')
canvas.pack()
width = 300
size = width // 3

#
# for i in range(3):
#     for j in range(3):
#         x = i * size
#         y = j * size
#         canvas.create_rectangle(x, y, x+size, y+size)
#         if (i + j) % 2 == 0:
#             for i in range(3):
#                 for j in range(3):
#                     x = i * size //3
#                     y = j * size // 3
#                     canvas.create_rectangle(x, y, x+size//3, y+size//3)

def fractal():

    canvas.create_rectangle(0, 0, 100, 100)
    canvas.create_rectangle(100, 0, 200, 100)
    canvas.create_rectangle(200, 0, 300, 100)

    canvas.create_rectangle(0, 100, 100, 200)
    canvas.create_rectangle(100, 100, 200, 200)
    canvas.create_rectangle(200, 100, 300, 200)

    canvas.create_rectangle(0, 200, 100, 300)
    canvas.create_rectangle(100, 200, 200, 300)
    canvas.create_rectangle(200, 200, 300, 300)




    canvas.create_rectangle(0, 100, 100/3, 100+100/3)
    canvas.create_rectangle(100/3, 100, 2*100/3, 100+100/3)
    canvas.create_rectangle(2*100/3, 100, 3*100/3, 100+100/3)

    canvas.create_rectangle(0, 100+100/3, 100/3, 100+2*100/3)
    canvas.create_rectangle(100/3, 100+100/3, 2*100/3, 100+2*100/3)
    canvas.create_rectangle(2*100/3, 100+100/3, 100, 100+2*100/3)

    canvas.create_rectangle(0, 100+2*100/3, 100/3, 2*100)
    canvas.create_rectangle(100/3, 100+2*100/3, 2*100/3, 100+100)
    canvas.create_rectangle(2*100/3, 100+2*100/3, 100, 2*100)





fractal()

root.mainloop()
