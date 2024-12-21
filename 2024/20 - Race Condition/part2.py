import sys
from collections import defaultdict

x = y = xmax = ymax = 0
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
        xmax = x
        y += 1
    ymax = y

# loop through every available space use manhatten
# distance to check cheat distance then check distance
# from start to coord and end to cheat coord

q = []
q.append(start)
ssteps = {}
steps = 0
ssteps[start] = steps
dirs = {"N":(0,-1), 
        "E":(1,0),
        "S":(0,1),
        "W":(-1,0)}

while q:
    current = q.pop(0)
    steps += 1
    for d in dirs.values():
        next = (current[0] + d[0], current[1] + d[1])
        if next not in ssteps and grid[next] != "#":
            q.append(next)
            ssteps[next] = steps

q = []
q.append(end)
esteps = {}
steps = 0
esteps[end] = steps
dirs = {"N":(0,-1), 
        "E":(1,0),
        "S":(0,1),
        "W":(-1,0)}

while q:
    current = q.pop(0)
    steps += 1
    for d in dirs.values():
        next = (current[0] + d[0], current[1] + d[1])
        if next not in esteps and grid[next] != "#":
            q.append(next)
            esteps[next] = steps

# print(ssteps)
# print(esteps)

cheats = defaultdict(int)

for c in grid:
    if grid[c] != "#":
        for x in range(-20, 20):
            for y in range(-20, 20):
                cheatsteps = abs(x) + abs(y)
                if cheatsteps <= 20:
                    cheatcoord = (c[0] + x, c[1] + y)
                    try:
                        if grid[cheatcoord] != "#":
                            
                            newsteps = ssteps[c]
                            newsteps += esteps[cheatcoord]
                            newsteps += cheatsteps
                            difference = ssteps[end] - newsteps

                            if difference >= 100:
                                cheats[difference] += 1
                    except:
                        pass
total = 0
for k, v in sorted(cheats.items()):
    print(v, k)
    total += v
print(ssteps[end], esteps[start], total)