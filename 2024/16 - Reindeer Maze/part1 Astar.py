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
q.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0
dirs = ((0,-1),(1,0),(0,1),(-1,0))

while not q.empty():
    current = q.get()

    if current == end:
        break

    for d in dirs:
        next = (current[0] + d[0], current[1] + d[1])
        new_cost = cost_so_far[current] + 