import sys
from queue import PriorityQueue

class node:
    def __init__(self, coord, dir="N"):
        self.coord = coord
        self.dir = dir
        

class graph:
    def __init__(self):
        self.coords = {}
        self.dirs = {"N": (0,-1),
                     "E": (1,0),
                     "S": (0,1),
                     "W": (-1,0)}

    def cost(self, n, n2):
        if n.dir == n2.dir:
            return 1
        elif (self.dirs[n.dir][0] == self.dirs[n2.dir][0] or
              self.dirs[n.dir][1] == self.dirs[n2.dir][1]):
            return 2001
        else:
            return 1001

    def neighbors(self, onode):
        n = []
        for dletter, dcoord in self.dirs.items():
            coord = (onode.coord[0] + dcoord[0], onode.coord[1] + dcoord[1])
            n.append(node(coord, dletter))
        return n

maze = graph()

x = y = xmax = ymax = 0
start = end = None

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            maze.coords[(x,y)] = c
            if c == 'S':
                start = node((x,y), "E")
            if c == 'E':
                end = node((x,y))
            xmax = x
            x += 1
        ymax = y
        y += 1


frontier = PriorityQueue()
frontier.put(0, start)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()
    print(current)

    if current.coord == end.coord:
        break

    for next in maze.neighbors(current):
        new_cost = cost_so_far[current] + maze.cost(current, next)
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost
            frontier.put(priority, next)
            came_from[next] = current