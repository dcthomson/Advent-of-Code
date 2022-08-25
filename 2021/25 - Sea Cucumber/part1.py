import sys

floor = dict()
xmax = 0
ymax = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in line.rstrip():
            floor[(x, y)] = c
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y
        y += 1

def printfloor(floor):
    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            print(floor[(x,y)], end="")
        print()

steps = 0

changed = True
while changed:
    changed = False

    tomove = []
    # figure out what can move right
    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            if floor[(x, y)] == ">":
                if (x + 1, y) in floor:
                    if floor[(x + 1, y)] == ".":
                        tomove.append((x,y))
                else:
                    if floor[(0, y)] == ".":
                        tomove.append((x,y))

    # move them right
    for coord in tomove:
        changed = True
        floor[(coord)] = "."
        if (coord[0] + 1, coord[1]) in floor:
            floor[(coord[0] + 1, coord[1])] = ">"
        else:
            floor[(0, coord[1])] = ">"

    tomove = []
    # figure out what can move down
    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            if floor[(x, y)] == "v":
                if (x, y + 1) in floor:
                    if floor[(x, y + 1)] == ".":
                        tomove.append((x,y))
                else:
                    if floor[(x, 0)] == ".":
                        tomove.append((x,y))

    # move them down
    for coord in tomove:
        changed = True
        floor[(coord)] = "."
        if (coord[0], coord[1] + 1) in floor:
            floor[(coord[0], coord[1] + 1)] = "v"
        else:
            floor[(coord[0], 0)] = "v"

    steps += 1

print(steps)