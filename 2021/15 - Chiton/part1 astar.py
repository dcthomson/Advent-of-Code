#from logging.config import _RootLoggerConfiguration
import sys
import time
import os
import heapdict

##############################################
### LETS FIGURE OUT A*
##############################################

grid = {}

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = int(c)
            x += 1
        maxx = x
        y += 1
    maxy = y
    
start = (0,0)
end = (maxx-1,maxy-1)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

frontier = heapdict.heapdict()
frontier[start] = 0
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0
dirs = ((0,-1),(1,0),(0,1),(-1,0))
while frontier.keys():
    (current, prio) = frontier.popitem()

    if current == end:
        print(prio)
        break

    for d in dirs:
        next = (current[0] + d[0], current[1] + d[1])
        try: 
            new_cost = cost_so_far[current] + grid[next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(end, next)
                frontier[next] = priority
                came_from[next] = current
        except:
            pass