import sys

#sys.setrecursionlimit(10**6)

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

# Let's try keeping the shortest path for every coord saved in an object
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = list()
        self.shortest = None



shortest = None

def go(grid, coord, steps=0, path=[]):
    global shortest
    
    #if shortest is not None:
        #print(shortest)
    newpath = path.copy()
    newpath.append(coord)
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
        go(grid, (coord[0], coord[1] + 1), steps, newpath)
        go(grid, (coord[0], coord[1] - 1), steps, newpath)
        go(grid, (coord[0] + 1, coord[1]), steps, newpath)
        go(grid, (coord[0] - 1, coord[1]), steps, newpath)
        
go(grid, (0,0))

print(shortest - grid[(0,0)])