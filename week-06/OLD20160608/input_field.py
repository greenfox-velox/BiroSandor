from tile import *

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

output = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 1:
            output.append(Floor(i,j))
        else:
            output.append(Wall(i,j))