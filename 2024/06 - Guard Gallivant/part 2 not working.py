import sys

grid = {}

start = None

x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            grid[(x,y)] = c
            if c not in "#.":
                start = (x,y)
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y
        y += 1

dir = None

total = 0

dirs = [(0,-1),(1,0),(0,1),(-1,0)]

if grid[start] == "^":
    dir = 0
elif grid[start] == ">":
    dir = 1
elif grid[start] == "v":
    dir = 2
elif grid[start] == "<":
    dir = 3

startdir = dir

for y in range(0, ymax):
    for x in range(0, xmax):
        current = start
        dir = startdir
        currentgrid = grid.copy()
        visited = {}
        if currentgrid[(x,y)] == ".":
            currentgrid[(x,y)] = "#"
        else:
            continue
        try:
            while (current, dir) not in visited:
                visited[(current, dir)] = True
                next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
                if currentgrid[next] == "#":
                    dir += 1
                    if dir > 3:
                        dir = 0
                    next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
                current = next
            total += 1
            print((x,y))
        except:
            # we hit an edge, pass to next iteration
            pass

print(total)