import sys

garden = {}

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            garden[x,y] = c
            x += 1
        y += 1

def printgarden(g):
    xmax = 0
    ymax = 0

    for c in g:
        if c[0] > xmax:
            xmax = c[0]
        if c[1] > ymax:
            ymax = c[1]

    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            print(g[x,y], end="")
        print()

for i in range(0, 64):

    newgarden = {}

    for c in garden:
        if garden[c] == "#":
            newgarden[c] = "#"
        elif garden[c] in "SO":
            for add in [[1,0], [-1,0], [0,1], [0,-1]]:
                neighbor = (c[0] + add[0], c[1] + add[1])
                if neighbor in garden:
                    if neighbor in newgarden:
                        if newgarden[neighbor] != "#":
                            newgarden[neighbor] = "O"
                    else:
                        newgarden[neighbor] = "O"
            if c not in newgarden:
                newgarden[c] = "."
        elif garden[c] == ".":
            if c not in newgarden:
                newgarden[c] = "."

    garden = newgarden


    # print()
    # printgarden(garden)

total = 0

for c in garden:
    if garden[c] == "O":
        total += 1

print(total)