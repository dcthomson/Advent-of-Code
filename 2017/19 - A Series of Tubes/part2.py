import sys
import string

grid = dict()

with open(sys.argv[1], 'r') as f:
    y = 0
    for line in f:
        line = line.strip("\n")
        x = 0
        for c in line:
            grid[(x, y)] = c
            x += 1
        y += 1

dir = 'd'
x = 0
while grid[(x, 0)] != "|":
    x += 1

letters = ""
coord = (x, 0)
keepgoing = True
steps = 0
while keepgoing:
    if dir == 'd' or dir == 'u':
        if dir == 'u':
            coord = (coord[0], coord[1] - 1)
        if dir == 'd':
            coord = (coord[0], coord[1] + 1)
        if grid[coord] == "+":
            if (coord[0] + 1, coord[1]) in grid and grid[(coord[0] + 1, coord[1])] != " ":
                dir = 'r'
            elif (coord[0] - 1, coord[1]) in grid and grid[(coord[0] - 1, coord[1])] != " ":
                dir = 'l'
    elif dir == 'r' or dir == 'l':
        if dir == 'r':
            coord = (coord[0] + 1, coord[1])
        if dir == 'l':
            coord = (coord[0] - 1, coord[1])
        if grid[coord] == "+":
            if (coord[0], coord[1] + 1) in grid and grid[(coord[0], coord[1] + 1)] != " ":
                dir = 'd'
            elif (coord[0], coord[1] - 1) in grid and grid[(coord[0], coord[1] - 1)] != " ":
                dir = 'u'
    if grid[coord] == "+":
        pass
    elif grid[coord] == "-" or grid[coord] == "|":
        pass
    elif grid[coord] in string.ascii_uppercase:
        letters += grid[coord]
    else:
        keepgoing = False
    steps += 1

print(steps)