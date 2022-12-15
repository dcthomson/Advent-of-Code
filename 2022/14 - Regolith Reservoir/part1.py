import sys

grid = {}
maxx = maxy = minx = None
miny = 0

start = (500,0)
grid[start] = "+"

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        coords = line.split(" -> ")
        prevcoord = None

        for c in coords:
            (x,y) = c.split(",")
            x = int(x)
            y = int(y)
            if maxx is None or x > maxx:
                maxx = x
            if maxy is None or y > maxy:
                maxy = y
            if minx is None or x < minx:
                minx = x
            grid[(x,y)] = "#"

            if prevcoord is not None:
                prevx = prevcoord[0]
                prevy = prevcoord[1]
                if x == prevx:
                    if y < prevy:
                        step = 1
                    else:
                        step = -1
                    wallmaker = y
                    for wallmaker in range(y, prevy, step):
                        grid[(x, wallmaker)] = "#"
                elif y == prevy:
                    if x < prevx:
                        step = 1
                    else:
                        step = -1
                    wallmaker = x
                    for wallmaker in range(x, prevx, step):
                        grid[(wallmaker, y)] = "#"

            prevcoord = (x,y)

def printcave(grid):
    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) not in grid:
                print(".", end="")
            else:
                print(grid[(x,y)], end="")
        print()

printcave(grid)

sand = (500,1)
grid[(sand)] = "o"

while sand[1] <= maxy:
    sandx = sand[0]
    sandy = sand[1]
    # check if sand can move
    moved = False
    if (sandx, sandy + 1) not in grid or grid[(sandx, sandy + 1)] == ".":
        grid[sand] = "."
        sand = (sandx, sandy + 1)
        grid[sand] = "o"
        moved = True
    elif (sandx - 1, sandy + 1) not in grid or grid[(sandx - 1, sandy + 1)] == ".":
        grid[sand] = "."
        sand = (sandx - 1, sandy + 1)
        grid[sand] = "o"
        moved = True
    elif (sandx + 1, sandy + 1) not in grid or grid[(sandx + 1, sandy + 1)] == ".":
        grid[sand] = "."
        sand = (sandx + 1, sandy + 1)
        grid[sand] = "o"
        moved = True
    if not moved:
        sand = (500,1)

totalsand = 0

for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        if (x,y) in grid and grid[(x,y)] == "o":
            totalsand += 1

print()
printcave(grid)

print(totalsand)