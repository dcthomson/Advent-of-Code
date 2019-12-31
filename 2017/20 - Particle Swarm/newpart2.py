import sys
import time

class Particle:

    def __init__(self, i,  p, v, a):
        self.id = i
        self.px = int(p[0])
        self.py = int(p[1])
        self.pz = int(p[2])
        self.vx = int(v[0])
        self.vy = int(v[1])
        self.vz = int(v[2])
        self.ax = int(a[0])
        self.ay = int(a[1])
        self.az = int(a[2])
        self.alive = True
        self.collided = False
        self.others = dict()

    def getposition(self):
        retstr = str(self.px)
        retstr += "-" + str(self.py)
        retstr += "-" + str(self.pz)
        return retstr

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def __str__(self):
        retstr = "p=<" + str(self.px) + ","
        retstr += str(self.py) + "," + str(self.pz) + ">" + ", "
        retstr += "v=<" + str(self.vx) + ","
        retstr += str(self.vy) + "," + str(self.vz) + ">" + ", "
        retstr += "a=<" + str(self.ax) + ","
        retstr += str(self.ay) + "," + str(self.az) + ">"
        return retstr

particles = []

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        p, v, a = line.rstrip().split(", ")
        p = p.rstrip(">")
        p = p.lstrip("p=<")
        p = p.split(",")
        v = v.rstrip(">")
        v = v.lstrip("v=<")
        v = v.split(",")
        a = a.rstrip(">")
        a = a.lstrip("a=<")
        a = a.split(",")
        # print(p, v, a)
        particles.append(Particle(i, p, v, a))
        i += 1

while True:
    # time.sleep(1)

    for p1 in particles:
        if not p1.collided:
            # print(p1)
            for p2 in particles:
                if p1.id == p2.id:
                    continue
                if not p2.collided:
                    if p1.px == p2.px:
                        if p1.py == p2.py:
                            if p1.pz == p2.pz:
                                print("COLLIDED")
                                p1.collided = True
                                p2.collided = True
                    # print()
    for p in particles:
        p.tick()

    pcount = 0
    for p in particles:
        if not p.collided:
            pcount += 1
    print(pcount)

