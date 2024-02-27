import sys

sys.setrecursionlimit(5000)

class Node():

    def __init__(self, num):
        self.num = num
        self.path = False
        self.shortest = 


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

shortest = None

def go(grid, coord, steps=0, path=[]):
    global shortest
    
    #if shortest is not None:
        #print(shortest)
    if coord not in grid:
        # we've gone out of the boundries of the grid
        return
    if coord in path:
        # already been to this coord
        return
    steps += grid[coord]
#    print(coord)
    if shortest is not None and steps > shortest:
        # we're already higher than the shortest path
        return
    if coord == (maxx - 1, maxy - 1):
        # found end
        if shortest is None or steps < shortest:
            shortest = steps
            print(shortest)
    else:
        newpath = path.copy()
        newpath.append(coord)
        go(grid, (coord[0], coord[1] + 1), steps, newpath)
        go(grid, (coord[0], coord[1] - 1), steps, newpath)
        go(grid, (coord[0] + 1, coord[1]), steps, newpath)
        go(grid, (coord[0] - 1, coord[1]), steps, newpath)
        
go(grid, (0,0))

print(shortest - grid[(0,0)])