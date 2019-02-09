import sys

grid = dict()

with open(sys.argv[1], 'r') as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            grid[(x, y)] = c

dir = 'd'
x = 0
while grid[(x, 0)] != "|":
    x += 1

coord = (x, 0)

