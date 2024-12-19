import sys

grid = {}

x = y = 0
xmax = ymax = 6
fallingblocks = 12

for y in range(0, ymax+1):
    for x in range(0, xmax+1):
        grid[(x,y)] = "."
        x += 1
    y += 1

with open(sys.argv[1], "r") as f:

    blocks = 0
    for line in f:
        line = line.strip()
        (x, y) = [int(x) for x in line.split(",")]
        grid[(x,y)] = "#"
        blocks += 1
        if blocks == fallingblocks:
            break

for y in range(0, ymax+1):
    for x in range(0, xmax+1):
        print(grid[(x,y)], end="")
        x += 1
    print()
    y += 1