import sys

class Point:

    def __init__(self, w, x, y, z):
        self.w = int(w)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.closelist = list()
        self.constellationID = False

    def checkConstellation(self, other):
        w = abs(self.w - other.w)
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        z = abs(self.z - other.z)

        if w + x + y + z == 0:
            # it's me...
            return
        if w + x + y + z <= 3:
            self.closelist.append(other)
            other.closelist.append(self)
            return True
        else:
            return False

    def setConstellation(self, cID):
        if self.constellationID:
            return self.constellationID
        else:
            self.constellationID = cID
            for point in self.closelist:
                self.constellation = point.setConstellation(cID)
            if not self.constellationID:
                self.constellationID = cID
                return self.constellationID

    def __str__(self):
        return "(%s,%s,%s,%s): %s" % (self.w, self.x, self.y, self.z, self.constellationID)



file = open(sys.argv[1], 'r')

points = list()


for line in file:
    (w,x,y,z) = line.rstrip().split(",")
    points.append(Point(w,x,y,z))

constellationID = 1
changed = True
while changed:
    changed = False
    for p1 in points:
        for p2 in points:
            if p1.checkConstellation(p2):
#                print "Check"
#                print p1
#                print p2
                if p1.constellationID and p2.constellationID:
                    if p1.constellationID < p2.constellationID:
                        p2.constellationID = p1.constellationID
                        changed = True
                    elif p2.constellationID < p1.constellationID:
                        p1.constellationID = p2.constellationID
                        changed = True
                elif p1.constellationID:
                    p2.constellationID = p1.constellationID
                    changed = True
                elif p2.constellationID:
                    p1.constellationID = p2.constellationID
                    changed = True
                else:
                    p1.constellationID = constellationID
                    p2.constellationID = constellationID
                    constellationID += 1
                    changed = True

# check if any starts still don't have ID
for p in points:
    if not p.constellationID:
        p.constellationID = constellationID
        constellationID += 1


#constellationCount = dict()
#constellationID = 1
#for point in points:
#    point.constellationID = point.setConstellation(constellationID)
#    constellationID += 1

constellationIDs = dict()
for point in points:
    constellationIDs[point.constellationID] = 1

print len(constellationIDs)
