import sys
import itertools

grid = {}
xmax = 0
ymax = 0

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            grid[(x,y)] = c
            x += 1
            if x > xmax:
                xmax = x
        y += 1
        if y > ymax:
            ymax = y

nogalaxies = {'x': [], 'y': []}

for y in range(0, ymax):
    galaxies = 0
    for x in range(0, xmax):
        if grid[x,y] == "#":
            galaxies += 1
    if galaxies == 0:
        # addline
        nogalaxies['y'].append(y)

for x in range(0, xmax):
    galaxies = 0
    for y in range(0, ymax):
        if grid[x,y] == "#":
            galaxies += 1
    if galaxies == 0:
        # addline
        nogalaxies['x'].append(x)

newgrid = {}

y2 = 0
for y in range(0, ymax):
    x2 = 0
    for x in range(0, xmax):
        newgrid[x2, y2] = grid[x, y]
        if x in nogalaxies['x']:
            x2 += 1
            newgrid[x2, y2] = grid[x, y]
        x2 += 1
    if y in nogalaxies['y']:
        y2 += 1
        for x3 in range(0, xmax + len(nogalaxies['x'])):
            newgrid[x3, y2] = '.'
    y2 += 1

def printgrid(g):
    xmax = 0
    ymax = 0
    for k in g:
        if k[0] > xmax:
            xmax = k[0]
        if k[1] > ymax:
            ymax = k[1]

    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            print(g[x,y], end="")
        print()

grid = newgrid

xmax = 0
ymax = 0
for k in grid:
    if k[0] > xmax:
        xmax = k[0]
    if k[1] > ymax:
        ymax = k[1]

galaxies = []
for y in range(0, ymax + 1):
    for x in range(0, xmax + 1):
        if grid[x, y] == '#':
            galaxies.append((x,y))
total = 0

for gs in itertools.combinations(galaxies, 2):
    g1 = gs[0]
    g2 = gs[1]
    dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    total += dist
print(total)

