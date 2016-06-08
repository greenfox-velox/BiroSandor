from tile import *


class Gameboard():
    def __init__(self,canvas, input_field):
        self.canvas = canvas
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
            i.draw(self.canvas)

    # def create_hero(self):
    #     Herodown.draw_character()

    
