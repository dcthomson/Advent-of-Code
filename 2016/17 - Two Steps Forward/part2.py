import sys
import hashlib

class Room:

    def __init__(self, x, y, hash):
        self.x = x
        self.y = y
        self.hash = hash

    def __str__(self):
        retstr = "(" + str(self.x) + ", " + str(self.y) + ") "
        retstr += self.hash
        return retstr

    def getneighbors(self):
        neighbors = []
        md5 = hashlib.md5(self.hash.encode()).hexdigest()
        if md5[0] in ('bcdef'):
            if self.y != 0:
                neighbors.append(Room(self.x, self.y - 1, self.hash + "U"))
        if md5[1] in ('bcdef'):
            if self.y != 3:
                neighbors.append(Room(self.x, self.y + 1, self.hash + "D"))
        if md5[2] in ('bcdef'):
            if self.x != 0:
                neighbors.append(Room(self.x - 1, self.y, self.hash + "L"))
        if md5[3] in ('bcdef'):
            if self.x != 3:
                neighbors.append(Room(self.x + 1, self.y, self.hash + "R"))
        return neighbors

initial = "dmypynyp"

room = Room(0, 0, initial)

# BFS

longestpathsize = 0

Q = [room]
while Q:
    node = Q.pop(0)
    # print(node)
    if node.x == 3 and node.y == 3:
        pathlength = len(node.hash) - len(initial)
        if pathlength > longestpathsize:
            longestpathsize = pathlength
        continue
    for neighbor in node.getneighbors():
        Q.append(neighbor)
    
print(longestpathsize)