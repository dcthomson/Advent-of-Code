import sys

class Coord:
    def __init__(self, coord, size, found, complete=False):
        self.x = coord[0]
        self.y = coord[1]
        self.pathsize = size
        self.found = found
        self.complete = complete
        

    def getneighbors(self, duct):
        neighbors = []
        pathsize = self.pathsize + 1
        for c in ((self.x + 1, self.y),
                  (self.x - 1, self.y),
                  (self.x, self.y + 1),
                  (self.x, self.y - 1)):
            if duct[c] != "#":
                found = self.found.copy()
                if duct[c] != ".":
                    found[duct[c]] = True
                neighbors.append(Coord(c, pathsize, found, self.complete))

        return neighbors

    def stringify(self):
        retstr = str(self.x) + "-" + str(self.y) + "-"
        for i in sorted(self.found.keys()):
            retstr += str(i)
        retstr = retstr.rstrip("-")
        return retstr


duct = {}

tofind = []
findcount = 0

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            duct[(x,y)] = c
            try:
                num = int(c)
                if num == 0:
                    start = (x,y)
                tofind.append((x,y))
                findcount += 1
            except:
                pass
            x += 1
        y += 1

Q = [Coord(start, 0, {'0': True})]

visited = {}

mostfound = ""

while Q:
    node = Q.pop(0)
    # print(node.stringify(), node.pathsize)
    # print(node)
    if len(node.found) == findcount:
        node.complete = True
    if node.complete and duct[(node.x, node.y)] == "0":
        print(node.pathsize)

    for neighbor in node.getneighbors(duct):
        neighborstr = neighbor.stringify()
        if neighborstr not in visited:
            visited[neighborstr] = True
            Q.append(neighbor)