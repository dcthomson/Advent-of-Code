import sys
import math

with open(sys.argv[1], "r") as f:

    grid = {}

    last = False
    firstcoord = []
    xmax = ymax = 0

    for line in f:
        line = line.strip()
        x,y = [int(i) for i in line.split(",")]
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
        if not firstcoord:
            firstcoord = (x,y)
        grid[(x,y)] = "R"
        if last:
            lastx = last[0]
            lasty = last[1]
            if lastx == x:
                if lasty > y:
                    for i in range(y + 1, lasty):
                        grid[(x,i)] = "G"
                elif lasty < y:
                    for i in range(lasty + 1, y):
                        grid[(x,i)] = "G"
            elif lasty == y:
                if lastx > x:
                    for i in range(x + 1, lastx):
                        grid[(i,y)] = "G"
                elif lastx < x:
                    for i in range(lastx + 1, x):
                        grid[(i,y)] = "G"
        last = (x,y)
    
    x = firstcoord[0]
    y = firstcoord[1]
    if last:
        lastx = last[0]
        lasty = last[1]
        if lastx == x:
            if lasty > y:
                for i in range(y + 1, lasty):
                    grid[(x,i)] = "G"
            elif lasty < y:
                for i in range(lasty + 1, y):
                    grid[(x,i)] = "G"
        elif lasty == y:
            if lastx > x:
                for i in range(x + 1, lastx):
                    grid[(i,y)] = "G"
            elif lastx < x:
                for i in range(lastx + 1, x):
                    grid[(i,y)] = "G"
                

    for y in range(0, ymax + 2):
        for x in range(0, xmax + 2):
            if (x,y) not in grid:
                grid[(x,y)] = "."