#from logging.config import _RootLoggerConfiguration
import sys
import time
import os

sys.setrecursionlimit(10**6)

grid = dict()

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = int(c)
            x += 1
        maxx = x
        y += 1
    maxy = y

def printshortest(shortest):
    
    os.system('cls')

    longest = 0

    for k in shortest:
        stepslen = len(str(shortest[k]))
        if stepslen > longest:
            longest = stepslen

    for y in range(0, maxy):
        for x in range(0, maxx):
            if (x,y) not in shortest:
                for i in range(0, longest):
                    print("_", end="")
            else:
                stepsstr = str(shortest[(x,y)])
                for i in range(0, longest - len(stepsstr)):
                    print("_", end="")
                print(stepsstr, end="")
            print(" ", end="")
        print()

# Let's try keeping the shortest path for every coord saved in an object
#class Coord:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#        self.path = list()
#        self.shortest = None
shortesttotal = None
shortest = dict()
count = 0

def go(grid, coord, steps=0):
    global shortest
    global shortesttotal
    global count
    count += 1

    printshortest(shortest)

    if coord not in grid:
        # we've gone out of the boundries of the grid
        return

    steps += grid[coord]
    if coord not in shortest:
        shortest[coord] = steps
    else:
        if steps < shortest[coord]:
            shortest[coord] = steps
        else:
            # been here in less steps
            return
#    print(coord)
#    if shortest is not None and steps > shortest:
#        # we're already higher than the shortest path
#        return
#    print(count)
    if coord == (maxx - 1, maxy - 1):
#        print(shortest[coord])
        # found end
        if shortesttotal is None or steps < shortest[coord]:
            shortesttotal = steps
            print(steps)
    else:
#        print(coord, steps)
#        print(shortest)
        # let's go to the smallest first
        for i in range(1, 10):
            for c in ((coord[0], coord[1] + 1),
                      (coord[0] + 1, coord[1]),
                      (coord[0], coord[1] - 1),
                      (coord[0] - 1, coord[1])):
                try:
                    if grid[c] == i:
                        go(grid, c, steps)
                except:
                    pass

go(grid, (0,0))

print(shortest[(maxx - 1, maxy - 1)] - grid[(0,0)])