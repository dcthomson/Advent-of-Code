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
            x += 1
            if x > xmax:
                xmax = x
        y += 1
        if y > ymax:
            ymax = y    
        

def getantinodes(x, y, xmax, ymax):
    xdiff = x[0] - y[0]
    ydiff = x[1] - y[1]
    coord = x
    ans = []
    while x[0] >= 0 and x[0] < xmax and x[1] >= 0 and x[1] < ymax:
        if coord != x:
            ans.append(x)
        x = (x[0] + xdiff, x[1] + ydiff)
    return ans 

for k in grid:
    for i in grid[k]:
        for j in grid[k]:
            if i != j:
                if i not in antinodes:
                    antinodes[i] = []
                antinodes[i].append(k)
                ans = getantinodes(i,j, xmax, ymax)
                for an in ans:
                    if an not in antinodes:
                        antinodes[an] = []
                    antinodes[an].append(k)

print(len(antinodes))