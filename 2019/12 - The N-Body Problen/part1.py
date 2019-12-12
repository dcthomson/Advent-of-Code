import sys

class Planet:
    def __init__(self, line):
        line = line.rstrip().rstrip(">").lstrip("<")
        (x, y, z) = line.split(", ")
        self.px = int(x.split("=")[1])
        self.py = int(y.split("=")[1])
        self.pz = int(z.split("=")[1])

        self.vx = 0
        self.vy = 0
        self.vz = 0

    def setvelocity(self, p):
        if p.px > self.px:
            self.vx += 1
        elif p.px < self.px:
            self.vx -= 1
        if p.py > self.py:
            self.vy += 1
        elif p.py < self.py:
            self.vy -= 1
        if p.pz > self.pz:
            self.vz += 1
        elif p.pz < self.pz:
            self.vz -= 1
    
    def moveplanet(self):
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def __str__(self):
        ret = "pos=<x=" + str(self.px)
        ret += ", y=" + str(self.py)
        ret += ", z=" + str(self.pz)
        ret += ">, "
        ret += "vel=<x=" + str(self.vx)
        ret += ", y=" + str(self.vy)
        ret += ", z=" + str(self.vz)
        ret += ">"
        return ret

    def getenergy(self):
        return self.getpotentialenergy() * self.getkineticenergy()

    def getpotentialenergy(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

    def getkineticenergy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

planets = []


with open(sys.argv[1]) as f:
    for line in f:
        planets.append(Planet(line))

for k in range(0, 1000):
    for i in planets:
        for j in planets:
            if i != j:
                i.setvelocity(j)

    for p in planets:
        p.moveplanet()

totalenergy = 0
for p in planets:
    totalenergy += p.getenergy()
print(totalenergy)