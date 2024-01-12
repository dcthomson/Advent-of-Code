import sys

sys.setrecursionlimit(10000)

grid = {}

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            grid[x,y] = c
            x += 1
        y += 1

xmax = 0
ymax = 0

for c in grid:
    if c[0] > xmax:
        xmax = c[0]
    if c[1] > ymax:
        ymax = c[1]

end = (xmax -1, ymax)

def printgrid(g):

    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            print(g[x,y], end="")
        print()

# printgrid(grid)

longest = 0

def go(path=[(0,1)]):
    global longest
    # print("path:", path)
    # print("path -1:", path[-1])
    pos = path[-1]
    # print("yo")
    if pos == end:
        # print(len(path) - 1)
        if len(path) - 1 > longest:
            longest = len(path) - 1
        # print(path)
        # print()
        return
    if grid[pos] == "^":
        nextpos = (pos[0], pos[1] - 1) # UP
        if grid[nextpos] == ".":
            newpath = path.copy()
            newpath.append(nextpos)
            go(newpath)
    elif grid[pos] == "v":
        nextpos = (pos[0], pos[1] + 1) # DOWN
        if grid[nextpos] == ".":
            newpath = path.copy()
            newpath.append(nextpos)
            go(newpath)
    elif grid[pos] == "<":
        nextpos = (pos[0] - 1, pos[1]) # LEFT
        if grid[nextpos] == ".":
            newpath = path.copy()
            newpath.append(nextpos)
            go(newpath)
    elif grid[pos] == ">":
        nextpos = (pos[0] + 1, pos[1]) # RIGHT
        if grid[nextpos] == ".":
            newpath = path.copy()
            newpath.append(nextpos)
            go(newpath)
    else:
        nextpos = (pos[0], pos[1] - 1)
        if nextpos not in path:
            try:
                if grid[nextpos] in ".<>^":
                    newpath = path.copy()
                    newpath.append(nextpos)
                    # print("newpath:", newpath)
                    go(newpath)
            except KeyError:
                pass
        nextpos = (pos[0], pos[1] + 1)
        if nextpos not in path:
            try:
                if grid[nextpos] in ".<>v":
                    newpath = path.copy()
                    newpath.append(nextpos)
                    # print("newpath:", newpath)
                    go(newpath)
            except KeyError:
                pass
        nextpos = (pos[0] + 1, pos[1])
        if nextpos not in path:
            try:
                if grid[nextpos] in ".>v^":
                    newpath = path.copy()
                    newpath.append(nextpos)
                    # print("newpath:", newpath)
                    go(newpath)
            except KeyError:
                pass
        nextpos = (pos[0] - 1, pos[1])
        if nextpos not in path:
            try:
                if grid[nextpos] in ".<v^":
                    newpath = path.copy()
                    newpath.append(nextpos)
                    # print("newpath:", newpath)
                    go(newpath)
            except KeyError:
                pass

go()

print(longest)