import sys

input = open("input.txt", "r")

class Acre:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + "): " + str(self.state)

    def nextIteration(self, land):
        adjacent = list()
        try:
            adjacent.append(land[(self.x - 1, self.y - 1)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x,     self.y - 1)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x + 1, self.y - 1)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x - 1, self.y)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x + 1, self.y)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x - 1, self.y + 1)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x,     self.y + 1)])
        except KeyError:
            pass
        try:
            adjacent.append(land[(self.x + 1, self.y + 1)])
        except KeyError:
            pass
        if self.x == 6 and self.y == 2:
            for a in adjacent:
                print a

        # OPEN
        if self.state == ".":
            treecount = 0
            for a in adjacent:
                if a.state == "|":
                    treecount += 1
            if treecount >= 3:
                return "|"
            else:
                return "."

        # TREE
        if self.state == "|":
            lycount = 0
            for a in adjacent:
                if a.state == "#":
                    lycount += 1
            if lycount >= 3:
                return "#"
            else:
                return "|"

        # LUMBERYARD
        if self.state == "#":
            ly = False
            tree = False
            for a in adjacent:
                if a.state == "#":
                    ly = True
                elif a.state == "|":
                    tree = True
            if ly and tree:
                return "#"
            else:
                return "."



def printland(land, size):
    for y in range(0, size['y']):
        for x in range(0, size['x']):
            sys.stdout.write(land[(x, y)].state)
        print
    print

land = dict()
newland = dict()

landsize = {'x':0, 'y':0}
y = 0
for line in input:
    x = 0
    for c in line:
        c = c.rstrip()
        # create land
        land[(x, y)] = Acre(x, y, c)
        if x > landsize['x']:
            landsize['x'] = x
        x += 1
    y += 1
    if y > landsize['y']:
        landsize['y'] = y
 
printland(land, landsize)

minutes = 10

for i in range(1, minutes + 1):
    for y in range(0, landsize['y']):
        for x in range(0, landsize['x']):
            newstate = land[(x, y)].nextIteration(land)
            newland[(x, y)] = Acre(x, y, newstate)
            x += 1
        y += 1

    for y in range(0, landsize['y']):
        for x in range(0, landsize['x']):
            land[(x, y)] = newland[(x, y)]

    printland(land, landsize)

trees = 0
lumberyards = 0
for y in range(0, landsize['y']):
    for x in range(0, landsize['x']):
        if land[(x, y)].state == "|":
            trees += 1
        elif land[(x, y)].state == "#":
            lumberyards += 1

print trees * lumberyards
