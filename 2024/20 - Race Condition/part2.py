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

# run bfs from start and end to get distance
# to both from all nodes

# loop through every available space use manhatten
# distance to check cheat distance then check distance
# from start to coord and end to cheat coord

q = []
q.append(start)
reached = []
reached.append(start)
dirs = {"N":(0,-1), 
        "E":(1,0),
        "S":(0,1),
        "W":(-1,0)}

while q:
    current = q.pop(0)
    for d in dirs.values():
        next = (current[0] + d[0], current[1] + d[1])
        if next not in reached:
            q.append(next)
            reached.append(next)