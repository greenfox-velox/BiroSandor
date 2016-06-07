from tkinter import *
root = Tk()

canvas = Canvas(root, width = 720, height = 720)
canvas.pack()
image_floor = PhotoImage(file='floor.png')
image_wall = PhotoImage(file='wall.png')




def create_floor(x,y):
    floor = canvas.create_image(x, y, image=image_floor, anchor=NW)

def create_wall(x,y):
    wall = canvas.create_image(x, y, image=image_wall, anchor=NW)

def create_field():
    a = [[1,1,1,0,0,1,1,0,0,1],
         [1,0,1,0,0,1,1,0,0,1],
         [1,1,1,1,1,1,1,0,0,1],
         [1,1,1,0,0,1,1,0,0,1],
         [1,0,1,0,0,1,1,1,1,1],
         [1,1,1,0,0,1,1,0,0,1],
         [1,1,1,0,0,1,1,0,0,1],
         [1,0,1,0,0,1,1,0,1,1],
         [1,0,1,1,1,1,1,0,1,1],
         [1,1,1,0,0,1,1,0,0,1]]


    for row_numbers in range(10): #'a' listan beluli listak szama, sorok szama
        for column_numbers in range(10): #ahany eleme van a belso listanak, oszlopok szama
            if a[row_numbers][column_numbers] == 1:
                create_floor(column_numbers*72, row_numbers*72)
            else:
                create_wall(column_numbers*72,row_numbers*72)

create_field()

root.mainloop()
