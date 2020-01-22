import sys
import copy

grids = {}
grids[0] = {}

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line.rstrip():
            if x == 2 and y == 2:
                pass
            else:
                grids[0][(x, y)] = c
            x += 1
        y += 1

def printgrids(grids):
    for gridnum, grid in sorted(grids.items()):
        print("Depth", gridnum)
        for y in range(0,5):
            for x in range(0,5):
                if x == 2 and y == 2:
                    print("?", end="")
                else:
                    print(grid[(x, y)], end="")
            print()
        print()

def getnewgrid():
    grid = {}
    for y in range(0,5):
        for x in range(0,5):
            if x == 2 and y == 2:
                continue
            grid[(x, y)] = "."
    return grid

# printgrids(grids)

for minute in range(1, 200 + 1):
    newgrids = {}

    highestlevel = max(grids.keys())
    lowestlevel = min(grids.keys())
    # print("HIGHEST LEVEL: ", highestlevel)
    # print("LOWEST LEVEL: ", lowestlevel)
    # print("\n")
    for coord in ((1,2),(3,2),(2,1),(2,3)):
        if grids[lowestlevel][coord] == "#":
            grids[lowestlevel - 1] = getnewgrid()
            break
    for y in range(0, 5):
        for x in (0, 4):
            if grids[highestlevel][(x, y)] == "#":
                if highestlevel + 1 not in grids:
                    grids[highestlevel + 1] = getnewgrid()
                    break
    for y in (0, 4):
        for x in range(0, 5):
            if grids[highestlevel][(x, y)] == "#":
                if highestlevel + 1 not in grids:
                    grids[highestlevel + 1] = getnewgrid()
                    break

    for gridnum, grid in grids.items():
        for y in range(0,5):
            for x in range(0,5):
                if x == 2 and y == 2:
                    continue
                adjcount = 0
                try:
                    if grid[(x + 1, y)] == "#":
                        adjcount += 1
                except:
                    # edge
                    if x + 1 == 2 and y == 2:
                        # inner
                        if gridnum - 1 in grids:
                            for y2 in range(0,5):
                                if grids[gridnum - 1][(0, y2)] == "#":
                                    adjcount += 1
                    else:
                        # outer
                        if gridnum + 1 in grids:
                            if grids[gridnum + 1][(3, 2)] == "#":
                                adjcount += 1
                try:
                    if grid[(x - 1, y)] == "#":
                        adjcount += 1
                except:
                    # edge
                    if x - 1 == 2 and y == 2:
                        # inner
                        if gridnum - 1 in grids:
                            for y2 in range(0,5):
                                if grids[gridnum - 1][(4, y2)] == "#":
                                    adjcount += 1
                    else:
                        # outer
                        if gridnum + 1 in grids:
                            if grids[gridnum + 1][(1, 2)] == "#":
                                adjcount += 1
                try:
                    if grid[(x, y + 1)] == "#":
                        adjcount += 1
                except:
                    # edge
                    if x == 2 and y + 1 == 2:
                        # inner
                        if gridnum - 1 in grids:
                            for x2 in range(0,5):
                                if grids[gridnum - 1][(x2, 0)] == "#":
                                    adjcount += 1
                    else:
                        # outer
                        if gridnum + 1 in grids:
                            if grids[gridnum + 1][(2, 3)] == "#":
                                adjcount += 1
                try:
                    if grid[(x, y - 1)] == "#":
                        adjcount += 1
                except:
                    # edge
                    if x == 2 and y - 1 == 2:
                        # inner
                        if gridnum - 1 in grids:
                            for x2 in range(0,5):
                                if grids[gridnum - 1][(x2, 4)] == "#":
                                    adjcount += 1
                    else:
                        # outer
                        if gridnum + 1 in grids:
                            if grids[gridnum + 1][(2, 1)] == "#":
                                adjcount += 1
                

                if gridnum not in newgrids:
                    newgrids[gridnum] = getnewgrid()
        
                if grid[(x, y)] == "#":
                    if adjcount == 1:
                        newgrids[gridnum][(x,y)] = "#"
                    else:
                        newgrids[gridnum][(x,y)] = "."
                elif grid[(x, y)] == ".":
                    if adjcount == 1 or adjcount == 2:
                        newgrids[gridnum][(x,y)] = "#"
                    else:
                        newgrids[gridnum][(x,y)] = "."

    grids = copy.deepcopy(newgrids)
    # print("MINUTE:", minute)
# printgrids(grids)
bugcount = 0
for grid in grids.values():
    for x in range(0, 5):
        for y in range(0, 5):
            try:
                if grid[(x, y)] == "#":
                    bugcount += 1
            except:
                pass

print(bugcount)