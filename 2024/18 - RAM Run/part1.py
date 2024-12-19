import sys

grid = {}

x = y = 0
xmax = ymax = 70
fallingblocks = 1024

for y in range(0, ymax+1):
    for x in range(0, xmax+1):
        grid[(x,y)] = "."
        x += 1
    y += 1

with open(sys.argv[1], "r") as f:

    blocks = 0
    for line in f:
        line = line.strip()
        (x, y) = [int(x) for x in line.split(",")]
        grid[(x,y)] = "#"
        blocks += 1
        if blocks == fallingblocks:
            break

for y in range(0, ymax+1):
    for x in range(0, xmax+1):
        print(grid[(x,y)], end="")
        x += 1
    print()
    y += 1

q = [(0,0)]
dirs = ((1,0),(0,1),(-1,0),(0,-1))
camefrom = dict()
camefrom[(0,0)] = None

while True:

    coord = q.pop(0)
    if coord == (xmax, ymax):
        break
    for d in dirs:
        nextcoord = (coord[0] + d[0], coord[1] + d[1])
        try:
            if nextcoord not in camefrom and grid[nextcoord] == ".":
                q.append(nextcoord)
                camefrom[nextcoord] = coord
        except:
            pass

coord = (xmax, ymax)
count = 0
while coord != None:
    coord = camefrom[coord]
    count += 1

print(count - 1)