import sys
from collections import defaultdict
import time
import functools

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
                if c == "@":
                    robotcoord = (x,y)
                    grid[(x,y)] = "@"
                    x += 1
                    grid[(x,y)] = "."
                elif c == "#":
                    grid[(x,y)] = "#"
                    x += 1
                    grid[(x,y)] = "#"
                elif c == ".":
                    grid[(x,y)] = "."
                    x += 1
                    grid[(x,y)] = "."
                elif c == "O":
                    grid[(x,y)] = "["
                    x += 1
                    grid[(x,y)] = "]"
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

    if d in "><":
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
    else:
        # up or down
        if grid[nextcoord] == ".":
            return [coord]
        elif grid[nextcoord] == "#":
            return [False]
        if grid[nextcoord] == "[":
            retlist = move(grid, nextcoord, d)
            retlist += move(grid, (nextcoord[0] + 1, nextcoord[1]), d)
            if coord not in retlist:
                retlist.append(coord)
        elif grid[nextcoord] == "]":
            retlist = move(grid, nextcoord, d)
            retlist += move(grid, (nextcoord[0] - 1, nextcoord[1]), d)
            if coord not in retlist:
                retlist.append(coord)
        return retlist

def compareup(a, b):

    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1

    return 0

def comparedown(a, b):
        
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        if a[0] < b[0]:
            return 1
        elif a[0] > b[0]:
            return -1
    return 0

for d in directions:
    ret = move(grid, robotcoord, d)
    if isinstance(ret, list):
        if all(ret):
            ret = list(set(ret))
            # sort ret
            if d == "^":
                ret = sorted(ret, key=functools.cmp_to_key(compareup))
            elif d == "v":
                ret = sorted(ret, key=functools.cmp_to_key(comparedown))
            for coord in ret:
                grid[(coord[0], coord[1] + dirs[d][1])] = grid[coord]
                grid[coord] = "."
            grid[robotcoord] = "."
            robotcoord = (robotcoord[0] + dirs[d][0],
                          robotcoord[1] + dirs[d][1])
    elif ret:
        grid[robotcoord] = "."
        robotcoord = (robotcoord[0] + dirs[d][0],
                      robotcoord[1] + dirs[d][1])

total = 0

for coord, c in grid.items():
    if c == "[":
        total += 100 * coord[1] + coord[0]

print(total)