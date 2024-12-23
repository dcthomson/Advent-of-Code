import sys
from queue import PriorityQueue

maze = {}

x = y = xmax = ymax = 0
start = end = None

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            maze[(x,y)] = c
            if c == 'S':
                start = (x,y)
            if c == 'E':
                end = (x,y)
            xmax = x
            x += 1
        ymax = y
        y += 1

q = PriorityQueue()
q.put((start, "E"), 0)
came_from = dict()
cost_so_far = dict()
came_from[(start, "E")] = None
cost_so_far[(start, "E")] = 0
dirs = {"N":(0,-1), 
        "E":(1,0),
        "S":(0,1),
        "W":(-1,0)}

while not q.empty():
    current = q.get()
    print(current)
    if current[0] == end:
        print(current)
        break

    for d in dirs:
        next = ((current[0][0] + dirs[d][0], current[0][1] + dirs[d][1]), d)
        if maze[next[0]] != "#":
            if d == current[0][1]:
                new_cost = cost_so_far[current] + 1
            elif (dirs[current[1]][0] == dirs[d][0] or
                dirs[current[1]][1] == dirs[d][1]):
                new_cost = cost_so_far[current] + 1000
            else:
                continue
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                q.put(next, priority)
                came_from[next] = current