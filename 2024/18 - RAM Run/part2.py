import sys

grid = {}
fallingblocks = []

x = y = 0
xmax = ymax = 70

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
        fallingblocks.append((x,y))

found = True
dirs = ((1,0),(0,1),(-1,0),(0,-1))

fallingcoord = None

while found:

    # for y in range(0, ymax+1):
    #     for x in range(0, xmax+1):
    #         print(grid[(x,y)], end="")
    #         x += 1
    #     print()
    #     y += 1

    fallingcoord = fallingblocks.pop(0)
    grid[fallingcoord] = "#"

    q = [(0,0)]
    camefrom = {}
    camefrom[(0,0)] = None
    found = False

    while True:
        try:
            coord = q.pop(0)
        except:
            found = False
            break      
        # print(coord)
        if coord == (xmax, ymax):
            # print("found:",coord)
            # print()
            found = True
            break
        for d in dirs:
            nextcoord = (coord[0] + d[0], coord[1] + d[1])
            try:
                if nextcoord not in camefrom and grid[nextcoord] == ".":
                    q.append(nextcoord)
                    camefrom[nextcoord] = coord
            except:
                pass

print(fallingcoord)