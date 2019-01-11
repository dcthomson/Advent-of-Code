import sys
import string
import operator

file = open(sys.argv[1], "r")

class Coord:

    def __init__(self, x, y, important=False, char="."):
        self.x = int(x)
        self.y = int(y)
        self.important = important
        self.char = char
        self.key = False
        self.blacklist = False

    def getKey(self):
        if not self.key:
            self.key = (self.x, self.y)
        return self.key

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

    def findClosest(self, coords):
#        print "findClosest"
#        sys.stdout.write("  ")
#        print self
        if self.important:
            self.closestcoord = self
            return self
        shortest = None
        single = True
        self.closestcoord = False
        for coord in coords:
            distx = abs(coords[coord].x - self.x)
            disty = abs(coords[coord].y - self.y)
            dist = distx + disty
            if shortest is None or dist < shortest:
#                    print str(self.x) + "," + str(self.y) + ": " + coords[coord].char + " - " + str(dist)
                shortest = dist
                single = True
                self.closestcoord = coords[coord]
            elif shortest == dist:
                single = False
                self.closestcoord = None
        if self.closestcoord is not None:
            self.char = self.closestcoord.char
        return self.closestcoord

    def checkInfinite(self, left, right, top, bottom):
#        print "checkInfinite"
#        sys.stdout.write("  ")
#        print self
        if self.char == ".":
            return
        if self.x == left or self.x == right:
            print self.closestcoord
            self.closestcoord.blacklist = True
        if self.y == top or self.y == bottom:
            print self.closestcoord
            self.closestcoord.blacklist = True

    def __str__(self):
        imp = ""
        if self.important:
            imp = " - important"
        return "(" + str(self.x) + "," + str(self.y) + "): char: " + self.char + imp 

# Create important coords
coords = dict()
importantcoords = dict()
atoZ = list(string.ascii_letters)
for line in file:
    (x, y) = line.rstrip().split(", ")
    c = Coord(x, y, True, atoZ.pop(0))
    coords[c.getKey()] = c
    importantcoords[c.getKey()] = c

# find boundries
left = None
right = None
top = None
bottom = None
for coord in coords:
    if left is None or coords[coord].x < left:
        left = coords[coord].x
    if right is None or coords[coord].x > right:
        right = coords[coord].x
    if top is None or coords[coord].y < top:
        top = coords[coord].y
    if bottom is None or coords[coord].y > bottom:
        bottom = coords[coord].y

print "Boundries:"
print left
print right
print top
print bottom

print
sys.stdout.write("Filling in other coords...")
# put in all the other coords
for x in range(left, right + 1):
    for y in range(top, bottom + 1):
        c = Coord(x, y)
        if c.getKey() not in coords:
            coords[c.getKey()] = c
print "DONE"
print


sys.stdout.write("Finding closest and blacklist infinite coords...")
sys.stdout.flush()
# find infinite coords
#for coord in (sorted(coords.values(), key=operator.attrgetter('key'))):
for coord in sorted(coords):
    coords[coord].findClosest(importantcoords)
    coords[coord].checkInfinite(left, right, top, bottom)
print "DONE"
print

# lets print the grid
#letter = dict()
#atoz = list(string.ascii_uppercase)
#for k in sorted(coords.iterkeys()):
#    letter[k] = atoz.pop(0)

print "printing out map..."
for y in range(top, bottom + 1):
    for x in range(left, right + 1):
        sys.stdout.write(coords[(x,y)].char)
    print
print "DONE"

count = dict()
for coord in coords:
    if coords[coord].closestcoord:
        if not coords[coord].closestcoord.blacklist:
            if coords[coord].closestcoord not in count:
                count[coords[coord].closestcoord] = 1
            else:
                count[coords[coord].closestcoord] += 1

print count

highest = 0
for c in count:
    if count[c] > highest:
        highest = count[c]

print
print highest
