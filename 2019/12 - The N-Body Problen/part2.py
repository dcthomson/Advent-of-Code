import sys
from functools import reduce

class Planet:
    def __init__(self, line, num):
        self.num = num
        line = line.rstrip().rstrip(">").lstrip("<")
        (x, y, z) = line.split(", ")
        self.position = {}
        self.position["x"] = int(x.split("=")[1])
        self.position["y"] = int(y.split("=")[1])
        self.position["z"] = int(z.split("=")[1])
        self.velocity = {}
        
        self.loopstep = {}
        self.start = {}
        for c in ("x", "y", "z"):
            self.velocity[c] = 0

            self.start[c] = (self.position[c], self.velocity[c])

            self.loopstep[c] = False

        print(self)

    def setvelocity(self, p):
        for c in ("x", "y", "z"):
            if p.position[c] > self.position[c]:
                self.velocity[c] += 1
            elif p.position[c] < self.position[c]:
                self.velocity[c] -= 1

    
    def moveplanet(self):
        for c in ("x", "y", "z"):
            self.position[c] += self.velocity[c]

    def __str__(self):
        ret = str(self.num) + ": pos=<x=" + str(self.position['x'])
        ret += ", y=" + str(self.position['y'])
        ret += ", z=" + str(self.position['z'])
        ret += ">, "
        ret += "vel=<x=" + str(self.velocity['x'])
        ret += ", y=" + str(self.velocity['y'])
        ret += ", z=" + str(self.velocity['z'])
        ret += ">"
        return ret

    def getenergy(self):
        return self.getpotentialenergy() * self.getkineticenergy()

    def getpotentialenergy(self):
        pe = 0
        for c in ("x", "y", "z"):
            pe += abs(self.position[c])
        return pe

    def getkineticenergy(self):
        ke = 0
        for c in ("x", "y", "z"):
            ke += abs(self.velocity[c])
        return ke

    def shortstring(self):
        ss = "x" + str(self.position['x'])
        ss += "y" + str(self.position['y'])
        ss += "z" + str(self.position['z'])
        ss += "x" + str(self.velocity['x'])
        ss += "y" + str(self.velocity['y'])
        ss += "z" + str(self.velocity['z'])
        return ss

    def checkforloop(self, step):
        for c in ("x", "y", "z"):
            if step > 0:
                if not self.loopstep[c]:
                    if self.start[c] == (self.position[c], self.velocity[c]):
                        self.loopstep[c] = step
                        
                        print("STEP", step)
                        print(self)

    def allLooped(self):
        ret = True
        for c in ("x", "y", "z"):
            if not self.loopstep[c]:
                ret = False
        return ret

def lowestcommonmultiple(l):
    l.sort()
    largest = l.pop()
    current = largest
    found = False
    while found == False:
        # print(current)
        found = True
        for i in l:
            if current % i != 0:
                found = False
                break
        if not found:
            current += largest
    return current


planets = []

with open(sys.argv[1]) as f:
    num = 1
    for line in f:
        planets.append(Planet(line, num))
        num += 1
print()
count = 0
allLooped = False
while allLooped == False:

    allLooped = True
    for p in planets:
        p.checkforloop(count)
        if not p.allLooped():
            allLooped = False

    for i in planets:
        for j in planets:
            if i != j:
                i.setvelocity(j)

    for p in planets:
        p.moveplanet()
    
    count += 1


steps = {}
for p in planets:
    for c in ("x", "y", "z"):
        steps[p.loopstep[c]] = True

steps = list(steps.keys())

print(steps)

print(lowestcommonmultiple(steps))