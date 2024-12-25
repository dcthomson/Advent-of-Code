import sys
import heapdict
import time

class node:
    def __init__(self, coord, dir="N"):
        self.coord = coord
        self.dir = dir

    def __repr__(self):
        retstr = "(x="
        retstr += "{:03d}".format(self.coord[0])
        retstr += ", "
        retstr += "y={:03d}".format(self.coord[1])
        retstr += ") - "
        retstr += self.dir
        return retstr
        

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
            return False
        else:
            return 1001

    def neighbors(self, onode):
        # print(onode)
        n = []
        for dletter, dcoord in self.dirs.items():
            coord = (onode.coord[0] + dcoord[0], onode.coord[1] + dcoord[1])
            if self.coords[coord] != "#":
                n.append(node(coord, dletter))
        # print(n)
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

frontier = heapdict.heapdict()
frontier[start] = 0
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while list(frontier.keys()):
    currenttuple = frontier.popitem()
    print(currenttuple)
    current = currenttuple[0]

    if current.coord == end.coord:
        print(currenttuple[1])
        break

    for next in maze.neighbors(current):
        cost = maze.cost(current, next)
        if cost:
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier[next] = priority
                came_from[next] = current