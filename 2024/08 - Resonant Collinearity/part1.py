import sys

grid = {}
antinodes = {}
x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            if c != ".":
                if c not in grid:
                    grid[c] = []
                grid[c].append((x,y))
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y    
        y += 1
        

def getantinodes(x, y):
    xdiff = x[0] - y[0]
    ydiff = x[1] - y[1]
    return x[0] + xdiff, x[1] + ydiff

for k in grid:
    for i in grid[k]:
        for j in grid[k]:
            if i != j:
                an = getantinodes(i,j)
                if (an[0] >= 0 and an[0] <= xmax):
                    if (an[1] >= 0 and an[1] <= ymax):
                        if an not in antinodes:
                            antinodes[an] = []
                        antinodes[an].append(k)

print(len(antinodes))