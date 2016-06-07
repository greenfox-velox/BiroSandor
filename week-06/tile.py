from tkinter import *
root = Tk()
canvas = Canvas(root, width = 720, height = 720)
canvas.pack()


class Tile():
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def draw(self, img):
        canvas.create_image(self.y*72, self.x*72, image=img, anchor=NW)

class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.floor = PhotoImage(file='floor.png')

    def draw(self):
        super().draw(self.floor)

class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.wall = PhotoImage(file='wall.png')
    def draw(self):
        super().draw(self.wall)


class Gameboard():
    def __init__(self,input_field):
        self.input_field = input_field

    def create_field(self):
        self.output = []
        for i in range(len(self.input_field)):
            for j in range(len(self.input_field[i])):
                if self.input_field[i][j] == 1:
                    self.output.append(Floor(i,j))
                else:
                    self.output.append(Wall(i,j))

    def create_board(self):
        for i in self.output:
            i.draw()




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
level1 = Gameboard(a)
level1.create_field()
level1.create_board()

root.mainloop()
