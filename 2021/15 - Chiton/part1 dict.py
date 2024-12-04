import sys
import time

sys.setrecursionlimit(50000)

grid = dict()

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = {"value": int(c), "steps": None}
            x += 1
        maxx = x
        y += 1
    maxy = y

shortest = None

def go(grid, coord, steps=0, prev=None):
    global shortest
    # time.sleep(.4)

    # we've gone out of the boundries of the grid
    if coord not in grid:
        return
    
    steps += grid[coord]["value"]

    # we've gotten to this coord in less steps
    if grid[coord]["steps"] is not None and steps >= grid[coord]["steps"]:
        return
    
    # we're already higher than the shortest path
    if shortest is not None and steps > shortest:
        return
    
    print(shortest, coord, grid[coord])

    if coord == (maxx - 1, maxy - 1):
        # found end
        if shortest is None or steps < shortest:
            shortest = steps
            print("shortest", shortest)
    else:
        grid[coord]["steps"] = steps

        # sort for smallest
        valuedict = {}
        for c in [(coord[0], coord[1] - 1),
                  (coord[0], coord[1] + 1),
                  (coord[0] + 1, coord[1]),
                  (coord[0] - 1, coord[1])]:
            try:
                if prev != (c):
                    valuedict[c] = grid[c]["value"]
            except:
                pass
       
        #sort and run key (coord)

        for c in sorted(valuedict, key=valuedict.get):
            go(grid, c, steps, coord)

        
go(grid, (0,0))

print(shortest - grid[(0,0)]["value"])