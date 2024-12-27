import sys
from collections import defaultdict

y = 0
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
        y += 1

# loop through every available space use manhatten
# distance to check cheat distance then check distance
# from start to coord and end to cheat coord

def getsteps(startcoord, grid):
    q = []
    q.append(startcoord)
    stepsdict = {}
    steps = 0
    stepsdict[startcoord] = steps
    dirs = [(0,-1),(1,0),(0,1),(-1,0)]

    while q:
        current = q.pop(0)
        steps += 1
        for d in dirs:
            next = (current[0] + d[0], current[1] + d[1])
            if next not in stepsdict and grid[next] != "#":
                q.append(next)
                stepsdict[next] = steps
    return stepsdict

ssteps = getsteps(start, grid)
esteps = getsteps(end, grid)

# print(ssteps)
# print(esteps)

cheats = defaultdict(int)

manhattencoords = {}
for x in range(-21, 21):
    for y in range(-21, 21):
        cheatsteps = abs(x) + abs(y)
        if cheatsteps <= 20:
            manhattencoords[(x,y)] = cheatsteps


for c in grid:
    if grid[c] != "#":
        for cheatdiff in manhattencoords:
            cheatcoord = (c[0] + cheatdiff[0], cheatdiff[1] + c[1])
            try:
                if grid[cheatcoord] != "#":

                    newsteps = ssteps[c]
                    newsteps += manhattencoords[cheatdiff]
                    newsteps += esteps[cheatcoord]

                    difference = ssteps[end] - newsteps

                    if difference >= 100:
                        cheats[difference] += 1
            except:
                pass
total = 0
for k, v in sorted(cheats.items()):
    # print(v, k)
    total += v
print(total)