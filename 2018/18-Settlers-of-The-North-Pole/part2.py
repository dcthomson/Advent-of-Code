import sys
from operator import itemgetter
import time

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


def toString(land, size):
    retstring = ""
    for y in range(0, size['y']):
        for x in range(0, size['x']):
            retstring += land[(x, y)].state
    return retstring

def printland(land, size):
    for y in range(0, size['y']):
        for x in range(0, size['x']):
            sys.stdout.write(land[(x, y)].state)
        print
    print

land = dict()
newland = dict()
duplicates = dict()

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
 
iteration = 0
repeatstart = 0
repeatend = 0
while 1:
    for y in range(0, landsize['y']):
        for x in range(0, landsize['x']):
            newstate = land[(x, y)].nextIteration(land)
            newland[(x, y)] = Acre(x, y, newstate)
            x += 1
        y += 1

    for y in range(0, landsize['y']):
        for x in range(0, landsize['x']):
            land[(x, y)] = newland[(x, y)]

    landstr = toString(land, landsize)
    if landstr not in duplicates:
        duplicates[landstr] = iteration
    else:
        repeatstart = duplicates[landstr]
        repeatend = iteration
        break

    iteration += 1

repeatlength = repeatend - repeatstart
between = (1000000000 - repeatend) % repeatlength

landstr = ""
for k in duplicates:
    if duplicates[k] == repeatstart + between - 1:
        landstr = k
        break

print k.count("|") * k.count("#")
