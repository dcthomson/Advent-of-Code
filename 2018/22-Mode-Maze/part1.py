import sys

file = open(sys.argv[1], "r")

class Coord:

    def __init__(self, x, y, target, depth, coords):
        (targetx, targety) = target.split(",")
        targetx = int(targetx)
        targety = int(targety)
        self.x = x
        self.y = y
        self.el= False
        if self.setGI(target, depth, coords):
            self.el = (self.gi + depth) % 20183
            self.type = self.el % 3

    def setGI(self, target, depth, coords):
#        print "t: %s, d: %s" % (target, depth)
        if x == 0 and y == 0:
            self.gi = 0
        elif x == targetx and y == targety:
            self.gi = 0
        elif y == 0:
            self.gi = x * 16807
        elif x == 0:
            self.gi = y * 48271
        else:
            if (x - 1, y) in coords and (x, y - 1) in coords:
                self.gi = coords[(x - 1, y)].el * coords[(x, y - 1)].el
            else:
                return False
        return True


    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False
        else:
            if self.x < other.x:
                return True
            else:
                return False    

    def printChar(self):
        if self.type == 0:
            sys.stdout.write(".")
        elif self.type == 1:
            sys.stdout.write("=")
        elif self.type == 2:
            sys.stdout.write("|")
        else:
            sys.stdout.write("E")

for line in file:
    if line.startswith("depth"):
        line = line.rstrip()
        depth = line.lstrip("depth: ")
    if line.startswith("target"):
        target = line.lstrip("target: ")

(targetx, targety) = target.split(",")
targetx = int(targetx)
targety = int(targety)
depth = int(depth)

coords = dict()

allgood = False
while not allgood:
    allgood = True
    for y in range(0, targety + 1):
        for x in range(0, targetx + 1):
            if (x, y) in coords:
                if not coords[(x, y)].el:
                    allgood = coords[(x, y)].setGI
            else:
                coords[(x, y)] = Coord(x, y, target, depth, coords)
                if not coords[(x, y)].el:
                    allgood = False

for y in range(0, targety + 1):
    for x in range(0, targetx + 1):
        coords[(x, y)].printChar()
    print


total = 0
for coordxy in coords:
    total += coords[coordxy].type

print(total)
