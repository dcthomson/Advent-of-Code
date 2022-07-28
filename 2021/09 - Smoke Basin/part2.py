import sys

grid = dict()

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = int(c)
            x += 1
        maxx = x
        y += 1
    maxy = y

basinlist = list()

def checkpoint(grid, point, basindict):
    basindict[point] = True
    x = point[0]
    y = point[1]
    for adj in ((x, y-1), 
                (x, y+1),
                (x-1, y),
                (x+1, y)):
        if adj in grid:
            if grid[adj] > grid[(x,y)] and grid[adj] != 9:
                basindict = checkpoint(grid, adj, basindict)
    return basindict

for y in range(0, maxy):
    for x in range(0, maxx):
        lowpoint = True
        for adj in ((x, y-1), 
                    (x, y+1),
                    (x-1, y),
                    (x+1, y)):
            if adj in grid:
                if grid[adj] <= grid[(x,y)]:
                    lowpoint = False
                    break
        if lowpoint:
            # findbasin
            basindict = checkpoint(grid, (x,y), basindict=dict())
            basinlist.append(len(basindict))
b = sorted(basinlist, reverse=True)
print(b[0] * b[1] * b[2])