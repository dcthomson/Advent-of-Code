import sys

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

newgrid = dict()

def printgrid(grid, maxx, maxy):
    for y in range(0, maxy):
        for x in range(0, maxx):
            print(grid[(x,y)], " ", end="")
        print()

steps = 0
blinks = 0

for i in range(0, 100):
    # add 1 to every cell
    for y in range(0, maxy):
        for x in range(0, maxx):
            grid[(x,y)] += 1
    # find greater than 10 and set to B for Blinked
    gtninefound = True
    while gtninefound:
        gtninefound = False
        for y in range(0, maxx):
            for x in range(0, maxy):
                if grid[(x,y)] != 'B' and grid[(x,y)] > 9:
                    gtninefound = True
                    for y2 in range(-1, 2):
                        y2 = y + y2
                        for x2 in range(-1, 2):
                            x2 = x + x2
                            if (x2, y2) in grid:
                                if grid[(x2, y2)] != 'B':
                                    if x2 != x or y2 != y:
                                        grid[(x2, y2)] += 1
                    grid[(x,y)] = 'B'
                    blinks += 1
    steps += 1
    # change B's to 0
    for y in range(0, maxx):
        for x in range(0, maxy):
            if grid[(x,y)] == 'B':
                grid[(x,y)] = 0

print(blinks)