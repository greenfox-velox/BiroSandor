# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

canvas_width = 300
canvas_height = 300
rectangle_size = 10

start_point_x = (canvas_width / 2) - (rectangle_size / 2)
start_point_y = start_point_
end_point_x = start_point_x + rectangle_size
end_point_y = end_point_x

greenBox = canvas.create_rectangle(start_point_x, start_point_y, end_point_x, end_point_y,  fill = 'green')



root.mainloop()
