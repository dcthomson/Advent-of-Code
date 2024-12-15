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
        else:
            directions += line

def printgrid(grid):
    for y in range(0, ymax):
        for x in range(0, xmax):
            print(grid[(x,y)], end="")
        print()

def move(grid, coord, d):

    nextcoord = (coord[0] + dirs[d][0], coord[1] + dirs[d][1])

    if grid[nextcoord] == ".":
        grid[nextcoord] = grid[coord]
        return True
    elif grid[nextcoord] == "#":
        return False
    else:
        if move(grid, nextcoord, d):
            grid[nextcoord] = grid[coord]
            return True
        else:
            return False


for d in directions:
    if move(grid, robotcoord, d):
        grid[robotcoord] = "."
        robotcoord = (robotcoord[0] + dirs[d][0],
                      robotcoord[1] + dirs[d][1])
    # print("Move " + d + ":")
    # printgrid(grid)
    # print()

total = 0

for coord, c in grid.items():
    if c == "O":
        total += 100 * coord[1] + coord[0]

print(total)