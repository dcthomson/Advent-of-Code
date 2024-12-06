import sys

ogrid = {}

start = None

x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            ogrid[(x,y)] = c
            if c not in "#.":
                start = (x,y)
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y
        y += 1

def runguard(grid, start):

    dirs = [(0,-1),(1,0),(0,1),(-1,0)]
    dir = None
    if grid[start] == "^":
        dir = 0
    elif grid[start] == ">":
        dir = 1
    elif grid[start] == "v":
        dir = 2
    elif grid[start] == "<":
        dir = 3

    visited = {}
    visiteddir = {}
    current = start
    try:
        while (current, dir) not in visiteddir:
            visited[current] = True
            visiteddir[(current, dir)] = True
            next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
            if grid[next] == "#":
                dir += 1
                if dir > 3:
                    dir = 0
                next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
            current = next
        return (visited, "loop")
    except:
        # we hit an edge, pass to next iteration
        return (visited, "hitedge")

(visited, _) = runguard(ogrid, start)

totalloops = 0

for coord in visited:
    if coord != start:
        newgrid = ogrid.copy()
        newgrid[coord] = "#"
        (_, type) = runguard(newgrid, start)
        if type == "loop":
            totalloops += 1

print(totalloops)