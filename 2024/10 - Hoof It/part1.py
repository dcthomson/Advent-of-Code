import sys

grid = {}

x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            try:
                grid[(x,y)] = int(c)
            except:
                grid[(x,y)] = c
            x += 1
            if x > xmax:
                xmax = x
        y += 1
        if y > ymax:
            ymax = y

nines = []

def path(coord, nextnum = 1, total = 0):
    global nines
    dirs = ((0,-1), (1,0), (0,1), (-1,0))
    for d in dirs:
        c = (coord[0] + d[0], coord[1] + d[1])
        try:
            if grid[c] == nextnum:
                if grid[c] != 9:
                    total += path(c, nextnum + 1)
                else:
                    if c not in nines:
                        nines.append(c)
        except:
            pass

total = 0

for y in range(0, ymax):
    for x in range(0, xmax):
        if grid[(x,y)] == 0:
            path((x,y))
            total += len(nines)
            nines = []

print(total)