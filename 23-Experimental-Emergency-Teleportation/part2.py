import sys

file = open(sys.argv[1], "r")

class Nanobot:

    def __init__(self, x, y, z, r=False):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        if r:
            self.radius = int(r)

    def __str__(self):
        return "x: %s, y: %s, z: %s, r: %s" % (self.x, self.y, self.z, self.radius)

    def inRadius(self, other):
        if self.getDistance(other) <= self.radius:
            return True
        else:
            return False

    def getDistance(self, other):
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        z = abs(self.z - other.z)
        return x + y + z
        
    def getCoords(self, coordDict):
        x = self.x - self.radius
        while x <= self.x + self.radius:
            y = self.y - self.radius
            while y <= self.y + self.radius:
                z = self.z - self.radius
                while z <= self.z + self.radius:
                    if self.getDistance(Nanobot(x, y, z)):
                        if (x,y,z) not in coordDict:
                            coordDict[(x,y,z)] = 1
                        else:
                            coordDict[(x,y,z)] += 1
                    z += 1
                y += 1
            x += 1

nanobots = list()

coordDict = dict()

for line in file:
    (x, y, z, r) = line.split(",")
    x = x.lstrip("pos=<")
    z = z.rstrip(">")
    (_, r) = r.split("=")
    nanobots.append(Nanobot(x, y, z, r))
    print nanobots[-1]
    nanobots[-1].getCoords(coordDict)









sys.exit()
######## OLD (TOO SLOW) ##########

sx = False
sy = False
sz = False
lx = False
ly = False
lz = False
for nanobot in nanobots:
    if not sx or nanobot.x < sx:
        sx = nanobot.x
    if not sy or nanobot.y < sy:
        sy = nanobot.z
    if not sz or nanobot.z < sz:
        sz = nanobot.z
    if not lx or nanobot.x > lx:
        lx = nanobot.x
    if not ly or nanobot.y > ly:
        ly = nanobot.z
    if not lz or nanobot.z > lz:
        lz = nanobot.z

nanobotcount = 0
coord = False
x = sx
while x <= lx:
    print
    print
    print
    print "x: %s" % (x)
    print
    print
    print
    y = sy
    while y <= ly:
        print "y: %s" % (y)
        z = sz
        while z <= lz:
            c = Nanobot(x,y,z)
            ncount = 0
            for nanobot in nanobots:
                if nanobot.inRadius(c):
                    ncount += 1
            if ncount > nanobotcount:
                nanobotcount = ncount
                coord = c

zerozerozero = Nanobot(0,0,0)
print coord.getDistance(zerozerozero)
