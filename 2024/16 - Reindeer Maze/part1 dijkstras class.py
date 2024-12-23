import sys
from queue import PriorityQueue

class node:
    def __init__(self, coord, dir="N"):
        self.coord = coord
        self.dir = dir

class graph:
    def __init__(self):
        self.coords = {}

    def cost(self, coord):
        for d in dirs
maze = {}

x = y = xmax = ymax = 0
start = end = None

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            graph.coords[(x,y)] = c
            if c == 'S':
                start = node((x,y), "E")
            if c == 'E':
                end = node((x,y))
            xmax = x
            x += 1
        ymax = y
        y += 1


frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()

    if current.coord == end.coord:
        break

    for next in maze.neighbors(current):
        new_cost = cost_so_far[current] + graph.cost(current, next)
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            frontier.put(next, priority)
            came_from[next] = current