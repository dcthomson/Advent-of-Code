import sys

sys.setrecursionlimit(5000)

grid = {}

with open(sys.argv[1], "r") as f:

    y = 0
    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            if (x,y) not in grid:
                grid[x,y] = {}
            grid[x,y]['char'] = c
            grid[x,y]['camefrom'] = ""
            grid[x,y]['num'] = 0
            x += 1
        y += 1



def move(grid, x=0, y=0, camefrom="W", space = ""):

    try:
        grid[x,y]['num'] += 1
    except KeyError:
        return

    if camefrom in grid[x,y]['camefrom']:
        return
    else:
        grid[x,y]['camefrom'] += camefrom

    if grid[x,y]['char'] == ".":
        if camefrom == "W":
            move(grid, x+1, y, camefrom, space)
        elif camefrom == "E":
            move(grid, x-1, y, camefrom, space)
        elif camefrom == "N":
            move(grid, x, y+1, camefrom, space)
        elif camefrom == "S":
            move(grid, x, y-1, camefrom, space)
    elif grid[x,y]['char'] == "/":
        if camefrom == "W":
            move(grid, x, y-1, "S", space)
        elif camefrom == "E":
            move(grid, x, y+1, "N", space)
        elif camefrom == "N":
            move(grid, x-1, y, "E", space)
        elif camefrom == "S":
            move(grid, x+1, y, "W", space)
    elif grid[x,y]['char'] == "\\":
        if camefrom == "W":
            move(grid, x, y+1, "N", space)
        elif camefrom == "E":
            move(grid, x, y-1, "S", space)
        elif camefrom == "N":
            move(grid, x+1, y, "W", space)
        elif camefrom == "S":
            move(grid, x-1, y, "E", space)
    elif grid[x,y]['char'] == "-":
        if camefrom == "W":
            move(grid, x+1, y, camefrom, space)
        elif camefrom in "E":
            move(grid, x-1, y, camefrom, space)
        elif camefrom in "NS":
            move(grid, x+1, y, "W", space + " ")
            move(grid, x-1, y, "E", space + " ")
    elif grid[x,y]['char'] == "|":
        if camefrom == "N":
            move(grid, x, y+1, camefrom, space)
        elif camefrom in "S":
            move(grid, x, y-1, camefrom, space)
        elif camefrom in "WE":
            move(grid, x, y+1, "N", space + " ")
            move(grid, x, y-1, "S", space + " ")

move(grid)

count=0

for g in grid:
    if grid[g]['num']:
        count += 1
print(count)