import sys

grid = {}

x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            grid[(x,y)] = c
            x += 1
        y += 1

