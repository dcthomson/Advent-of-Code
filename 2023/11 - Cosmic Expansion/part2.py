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

galaxies = []
for y in range(0, ymax):
    for x in range(0, xmax):
        if grid[x, y] == '#':
            galaxies.append((x,y))
total = 0

galaxyspace = 1000000

for gs in itertools.combinations(galaxies, 2):
    g1 = gs[0]
    g2 = gs[1]
    for g in nogalaxies['x']:
        if g1[0] < g < g2[0] or g2[0] < g < g1[0]:
            total += galaxyspace - 1
    for g in nogalaxies['y']:
        if g1[1] < g < g2[1] or g2[1] < g < g1[1]:
            total += galaxyspace - 1
    dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    total += dist
print(total)

