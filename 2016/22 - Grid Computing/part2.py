import sys
import copy
import curses

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

class Node:
    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.thedata = False
    
    def __str__(self):
        retstr = "(" + str(self.x) + ", " + str(self.y) + "): "
        retstr += str(self.used) + " / " + str(self.size)
        if self.thedata:
            retstr += " DATA"
        return retstr


class Grid:
    def __init__(self, nodes, steps=0, empty=False, changes=[]):
        self.nodes = grid
        self.steps = steps
        if empty:
            self.empty = empty
        else:
            self.empty = self.getempty()
        for n in changes:
            self.nodes[(n.x, n.y)] = n

    def stringify(self):
        retstr = ""
        for k in sorted(self.nodes):
            n = self.nodes[k]
            for i in (n.x, n.y, n.size, n.used, n.avail, n.thedata):
                retstr += str(i) + "-"
            
        return retstr[:-1]


    def setdata(self):
        for _, n in self.nodes.items():
            try:
                _ = self.nodes[(n.x, n.y - 1)]
            except:
                try:
                    _ = self.nodes[(n.x + 1, n.y)]
                except:
                    n.thedata = True
                    # print(n)

    def getempty(self):
        for _, n in self.nodes.items():
            if n.used == 0:
                return n

    def __str__(self):
        retstr = ""
        longest = 0
        for _, n in self.nodes.items():
            l = len(str(n.used) + "/" + str(n.size))
            if l > longest:
                longest = l
        
        y = 0
        for k in sorted(self.nodes.keys(), key=lambda n: (n[1], n[0])):
            node = self.nodes[k]
            if node.y != y:
                retstr += "\n"
                y = node.y
            s = str(node.used) + "/" + str(node.size)
            for _ in range(len(s), longest):
                retstr += " "
            retstr += str(node.used) + "/" + str(node.size) + "  "
        return retstr
    
    
    def getNextMoves(self):
        nodes = []
        for c in ((self.empty.x, self.empty.y - 1),
                  (self.empty.x, self.empty.y + 1),
                  (self.empty.x - 1, self.empty.y),
                  (self.empty.x + 1, self.empty.y)):
            try:
                nodes.append(self.nodes[c])
            except:
                pass

        grids = []

        for node in nodes:
            if node.used <= self.empty.size:
                # if data fits
                used = copy.deepcopy(node)
                empty = copy.deepcopy(self.empty)
            
                empty.used = used.used
                if used.thedata:
                    empty.thedata = True
                    used.thedata = False
                grids.append(Grid(self.nodes, self.steps + 1, used, [empty]))
        return grids
        

grid = {}

with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith("/dev/grid"):
            splitline = line.split()
            (_, x, y) = splitline[0].split("-")
            x = int(x.lstrip("x"))
            y = int(y.lstrip("y"))
            size = int(splitline[1].rstrip("T"))
            used = int(splitline[2].rstrip("T"))
            avail = int(splitline[3].rstrip("T"))
            grid[(x,y)] = Node(x, y, size, used, avail)

g = Grid(grid)

g.setdata()

print(g)

Q = [g]

visited = {}

while Q:
    print(visited)
    g = Q.pop(0)
    if g.nodes[(0, 0)].thedata:

        print(g.steps)
        break
    for ng in g.getNextMoves():
        ngstr = ng.stringify()
        if ngstr not in visited:
            Q.append(ng)
            visited[ngstr] = True

print("DONE")