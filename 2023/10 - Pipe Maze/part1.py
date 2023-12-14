import sys

start = None
grid = {}
charmap = {'|': "NS",
           '-': "EW",
           'L': "NE",
           'J': "NW",
           '7': "SW",
           'F': "SE",
           '.': ""}

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            grid[(x,y)] = c
            if c == 'S':
                start = (x,y)
            x += 1

        y += 1

nextpipe = None

if "S" in charmap[grid[start[0], start[1]-1]]:
    nextpipe = (start[0], start[1]-1)
elif "N" in charmap[grid[start[0], start[1]+1]]:
    nextpipe = (start[0], start[1]+1)
elif "E" in charmap[grid[start[0], start[1]-1]]:
    nextpipe = (start[0]+1, start[1])
elif "W" in charmap[grid[start[0], start[1]-1]]:
    nextpipe = (start[0]-1, start[1])

steps = 0
prevpipe = start

while nextpipe != start:
    steps += 1
    dirs = []
    for c in charmap[grid[nextpipe]]:
        if c == "N":
            dirs.append((nextpipe[0], nextpipe[1]-1))
        elif c == "S":
            dirs.append((nextpipe[0], nextpipe[1]+1))
        elif c == "E":
            dirs.append((nextpipe[0]+1, nextpipe[1]))
        elif c == "W":
            dirs.append((nextpipe[0]-1, nextpipe[1]))

    for d in dirs:
        if d != prevpipe:
            prevpipe = nextpipe
            nextpipe = d
            break

print(steps // 2 + (steps % 2 > 0)) # divide and round up