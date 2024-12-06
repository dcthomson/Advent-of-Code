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
            x += 1
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

current = start

try:
    while True:
        if grid[current] != "X":
            grid[current] = "X"
            total += 1
        next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
        if grid[next] == "#":
            dir += 1
            if dir > 3:
                dir = 0
            next = (current[0] + dirs[dir][0], current[1] + dirs[dir][1])
        current = next

except:
    print(total)