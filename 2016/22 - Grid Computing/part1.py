import sys

class Node:
    def __init__(self, x, y, size, used, avail, use):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use

    def fit(self, n):
        if n.used > 0 and n.used < self.avail:
            return True
        else:
            return False


nodes = {}

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
            use = int(splitline[4].rstrip("%"))
            nodes[(x,y)] = Node(x, y, size, used, avail, use)

count = 0
for i in nodes:
    for j in nodes:
        if nodes[i].fit(nodes[j]):
            count += 1
print(count)