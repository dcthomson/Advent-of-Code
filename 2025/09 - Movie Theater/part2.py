import sys
import math
import time

grid = {}

last = False
firstcoord = []
xmax = ymax = 0
reds = []

with open(sys.argv[1], "r") as f:
    print("Reading in file...")
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
        reds.append((x,y))
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



def printfloor():
    for y in range(0, ymax + 2):
        for x in range(0, xmax + 2):
            print(grid[(x,y)], end="")
        print()

print("setting blanks...")

for y in range(0, ymax + 2):
    for x in range(0, xmax + 2):
        if (x,y) not in grid:
            grid[(x,y)] = "."

def clearout(coord=(0,0)):
    if coord in grid:
        if grid[coord] == ".":
            grid[coord] = " "
            clearout((coord[0] - 1, coord[1]))
            clearout((coord[0] + 1, coord[1]))
            clearout((coord[0], coord[1] - 1))
            clearout((coord[0], coord[1] + 1))
print("clearing out...")
clearout()

for y in range(0, ymax + 2):
    for x in range(0, xmax + 2):
        if grid[(x,y)] == ".":
            grid[(x,y)] = "G"


print("finding areas...")

maxarea = 0

for r1 in reds:
    for r2 in reds:
        if r1 == r2:
            continue
        else:
            good = True
            if r1[0] > r2[0]:
                x1 = r2[0]
                x2 = r1[0]
            else:
                x1 = r1[0]
                x2 = r2[0]
            if r1[1] > r2[1]:
                y1 = r2[1]
                y2 = r1[1]
            else:
                y1 = r1[1]
                y2 = r2[1]
            for x in range(x1,x2 + 1):
                for y in range(y1, y2 + 1):
                    if grid[(x,y)] == " ":
                        good = False
                        break
                if not good:
                    break
            if good:               
                area = (abs(r1[0] - r2[0]) + 1) * (abs(r1[1] - r2[1]) + 1)
                if area > maxarea:
                    maxarea = area

print(maxarea)
            