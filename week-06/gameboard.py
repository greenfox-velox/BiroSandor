from tile import *
from character import *
from hero import *
from enemy import *
from levels import *
from random import randint


class Gameboard():
    def __init__(self,canvas):
        self.canvas = canvas
        self.level = Levels()
        self.input_field = self.level.map
        self.hero = Hero(0,0)
        self.boss = Enemy(0,9)
        self.skeletons = [
                Enemy(9,0),
                Enemy(6,9),
                Enemy(4,3)
        ]
        self.create_field()
        self.create_board()
        self.create_hero()
        self.create_boss()
        self.create_skeletons()

    def create_hero(self):
        self.hero.hero_default()
        self.hero.draw(self.canvas)

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

    def keypress(self, event):
        if event.keysym == 's':
            self.hero_move_down()
        if event.keysym == 'w':
            self.hero_move_up()
        if event.keysym == 'a':
            self.hero_move_left()
        if event.keysym == 'd':
            self.hero_move_right()

    def create_hero(self):
        self.hero.hero_default()
        self.hero.draw(self.canvas)

    def is_in_field(self,x,y):
        return x >= 0 and x <= 9 and y >= 0 and y <= 9

    def next_field_is_floor(self,x,y):
        return self.input_field[y][x] == 1

    def hero_move_down(self):
        if self.is_in_field(self.hero.x, self.hero.y+1):
            if self.next_field_is_floor(self.hero.x, self.hero.y+1):
                self.hero.hero_down()
                self.hero.draw(self.canvas)

    def hero_move_up(self):
        if self.is_in_field(self.hero.x, self.hero.y-1):
            if self.next_field_is_floor(self.hero.x, self.hero.y-1):
                self.hero.hero_up()
                self.hero.draw(self.canvas)

    def hero_move_left(self):
        if self.is_in_field(self.hero.x-1, self.hero.y):
            if self.next_field_is_floor(self.hero.x-1, self.hero.y):
                self.hero.hero_left()
                self.hero.draw(self.canvas)

    def hero_move_right(self):
        if self.is_in_field(self.hero.x+1, self.hero.y):
            if self.next_field_is_floor(self.hero.x+1, self.hero.y):
                self.hero.hero_right()
                self.hero.draw(self.canvas)


    def create_boss(self):
        self.boss.boss()
        self.boss.draw(self.canvas)

    def create_skeletons(self):
        for skeleton in self.skeletons:
            skeleton.skeleton()
            skeleton.draw(self.canvas)

    def next_level(self):
        self.level.next_level()
        self.input_field = self.level.map
        self.hero = Hero(0,0)
        self.boss = Enemy(9,9)
        self.skeletons = [Enemy(9,0), Enemy(6,9)]
        self.create_field()
        self.create_board()
        self.create_hero()
        self.create_boss()
        self.create_skeletons()
