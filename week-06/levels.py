

a = [[1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,0,1,1,0,0,1],
    [1,1,1,1,1,1,1,0,0,1],
    [1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,0,1,1,1,1,1],
    [1,1,1,0,0,1,1,0,0,1],
    [1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,0,1,1,0,1,1],
    [1,0,1,1,1,1,1,0,1,1],
    [1,1,1,0,0,1,1,0,0,0]]


b = [[1,1,1,0,1,1,1,1,1,1],
    [0,0,1,1,1,0,1,0,0,1],
    [0,0,0,0,0,0,1,0,1,1],
    [0,0,1,1,1,1,1,0,1,0],
    [0,0,1,0,0,1,1,1,1,0],
    [1,1,1,0,0,1,1,0,1,0],
    [1,0,0,0,1,1,1,0,1,0],
    [1,1,1,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,1,1,0]]

maps = [b,a]

class Levels():
    def __init__(self):
        self.i = 0
        self.map = maps[self.i]

    def next_level(self):
        self.i += 1
        self.map = maps[self.i]
