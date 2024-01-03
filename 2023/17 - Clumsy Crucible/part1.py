import sys

grid = {}

with open(sys.argv[1], "r") as f:

    y = 0
    for line in f:
        line = line.strip()
    
        x = 0

        for c in line:
            grid[x,y] = c
            x += 1

        y += 1

