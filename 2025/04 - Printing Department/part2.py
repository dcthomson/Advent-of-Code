import sys

def printgrid(grid):
    xmin = xmax = ymin = ymax = 0
    for coord in grid:
        if coord[0] > xmax:
            xmax = coord[0]
        if coord[1] > ymax:
            ymax = coord[1]

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print(grid[(x,y)], end="")
        print()

with open(sys.argv[1], "r") as f:

    grid = {}

    y = 0

    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            grid[(x, y)] = c
            x += 1
        y += 1

    total_rolls = 0

    changed = True

    while changed:
        remove_list = []
        changed = False
        for coord in grid:
            if grid[(coord)] != "@":
                continue
            paper_rolls = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    
                    try:
                        if grid[(coord[0] + x, coord[1] + y)] == "@":
                            paper_rolls += 1
                    except:
                        pass
            if paper_rolls < 4:
                remove_list.append(coord)

        for coord in remove_list:
            changed = True
            total_rolls += 1
            grid[(coord)] = "."
        # printgrid(grid)

    print(total_rolls)
