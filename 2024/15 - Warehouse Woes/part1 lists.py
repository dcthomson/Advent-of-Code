import sys
from collections import defaultdict

grid = {}

x = y = xmax = ymax = 0
directions = ""

dirs = {"^":(0,-1),
        ">":(1,0),
        "v":(0,1),
        "<":(-1,0)}

robotcoord = False

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if line.startswith("#"):
            x = 0
            for c in line:
                grid[(x,y)] = c
                if c == "@":
                    robotcoord = (x,y)
                x += 1
            xmax = x
            y += 1
            ymax = y

        elif line != "":
            directions = line

def printgrid(grid):
    for y in range(0, ymax):
        for x in range(0, xmax):
            print(grid[(x,y)], end="")
        print()

printgrid(grid)

for d in directions:
    coord = robotcoord
    while grid[coord] not in ".#":
        coord = (coord[0] + dirs[d][0], coord[1] + dirs[d][1])
    if grid[coord] == ".":
        while grid[coord] != "@":
            robotcoord = coord
            bcoord = (coord[0] + (dirs[d][0] * -1), coord[1] + (dirs[d][1] * -1))
            grid[coord] = grid[bcoord]
            coord = bcoord
        grid[coord] = "."
    printgrid(grid)
    print()       