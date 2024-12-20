import sys
from collections import defaultdict

x = y = xmax = ymax = 0
start = end = None
grid = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            grid[(x,y)] = c
            if c == "S":
                start = (x,y)
            elif c == "E":
                end = (x,y)
            x += 1
        xmax = x
        y += 1
    ymax = y

dirs = ((0,-1),(1,0),(0,1),(-1,0))
walls = []
came_from = dict()
came_from[start] = None
q = [start]
foundend = False

while q and not foundend:
    coord = q.pop(0)
    for d in dirs:
        neighbor = (coord[0] + d[0], coord[1] + d[1])
        if grid[neighbor] == "#":
            if neighbor not in walls:
                walls.append(neighbor)
        elif grid[neighbor] == ".":
            if neighbor not in came_from:
                q.append(neighbor)
                came_from[neighbor] = coord
        elif grid[neighbor] == "E":
            came_from[neighbor] = coord
            foundend = True
            break

coord = end
count = 0
while coord is not None:
    coord = came_from[coord]
    count += 1
nocheats = count - 1

cheats = 0

wallnum = 1
for wall in walls:
    newgrid = grid.copy()
    newgrid[wall] = "."
    came_from = dict()
    came_from[start] = None
    q = [start]
    foundend = False

    while q and not foundend:
        coord = q.pop(0)
        for d in dirs:
            neighbor = (coord[0] + d[0], coord[1] + d[1])
            try:
                if newgrid[neighbor] == ".":
                    if neighbor not in came_from:
                        q.append(neighbor)
                        came_from[neighbor] = coord
                elif newgrid[neighbor] == "E":
                    came_from[neighbor] = coord
                    foundend = True
                    break
            except:
                pass
    coord = end
    count = 0
    while coord is not None:
        coord = came_from[coord]
        count += 1
    count -= 1
    if nocheats - count >= 100:
        cheats += 1
    wallnum += 1

print(cheats)