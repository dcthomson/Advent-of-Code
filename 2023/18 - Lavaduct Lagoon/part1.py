import sys

x = 0
y = 0
xmin = xmax = ymin = ymax = 0

grid = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (direction, distance, _) = line.split()

        distance = int(distance)

        if direction == "R":
            for i in range(0, distance):
                x += 1
                if x < xmin:
                    xmin = x
                elif x > xmax:
                    xmax = x
                grid[x,y] = "#"
        elif direction == "L":
            for i in range(0, distance):
                x -= 1
                if x < xmin:
                    xmin = x
                elif x > xmax:
                    xmax = x
                grid[x,y] = "#"
        elif direction == "U":
            for i in range(0, distance):
                y -= 1
                if y < ymin:
                    ymin = y
                elif y > ymax:
                    ymax = y
                grid[x,y] = "#"
        elif direction == "D":
            for i in range(0, distance):
                y += 1
                if y < ymin:
                    ymin = y
                elif y > ymax:
                    ymax = y
                grid[x,y] = "#"

# mark everything else with "."
for y in range(ymin, ymax + 1):
    for x in range(xmin, xmax + 1):
        if (x,y) not in grid:
            grid[x,y] = "."

#for y in range(ymin, ymax + 1):
#    for x in range(xmin, xmax + 1):
#        print(grid[x,y], end="")
#    print()

# lets mark everything outside
edges = []

for x in range(xmin, xmax):
    edges.append((x, ymin))
    edges.append((x, ymax))
for y in range(ymin, ymax):
    edges.append((xmin, y))
    edges.append((xmax, y))

visited = []

queue = []
for edgecoord in edges:
    if grid[edgecoord] == ".":
        queue.append(edgecoord)
    while queue:
        coord = queue.pop(0)
        if grid[coord] == ".":
            grid[coord] = "E"
            for c in ((coord[0], coord[1] + 1),
                    (coord[0], coord[1] - 1),
                    (coord[0] + 1, coord[1]),
                    (coord[0] - 1, coord[1])):
                if c in grid and c not in visited and grid[c] == ".":
                    visited.append(c)
                    queue.append(c)

cmlava = 0

for y in range(ymin, ymax + 1):
    for x in range(xmin, xmax + 1):
        if grid[x,y] == "E":
            grid[x,y] = "."
        elif grid[x,y] == ".":
            grid[x,y] = "#"
        if grid[x,y] == "#":
            cmlava += 1
#        print(grid[x,y], end="")
#    print()

print(cmlava)