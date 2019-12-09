import sys

file = open(sys.argv[1], "r")


class Nanobot:

    def __init__(self, x, y, z, r):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.radius = int(r)

    def __str__(self):
        return "x: %s, y: %s, z: %s, r: %s" % (self.x, self.y, self.z, self.radius)

    def inRadius(self, other):
        x = abs(self.x - other.x)
        y = abs(self.y - other.y)
        z = abs(self.z - other.z)
        if x + y + z <= self.radius:
            return True
        else:
            return False


nanobots = list()

for line in file:
    (x, y, z, r) = line.split(",")
    x = x.lstrip("pos=<")
    z = z.rstrip(">")
    (_, r) = r.split("=")
    nanobots.append(Nanobot(x, y, z, r))

largestradius = False
for nanobot in nanobots:
    if not largestradius:
        largestradius = nanobot
    elif largestradius.radius < nanobot.radius:
        largestradius = nanobot

inRangeNanobots = 0
for nanobot in nanobots:
    if largestradius.inRadius(nanobot):
        inRangeNanobots += 1

print(inRangeNanobots)