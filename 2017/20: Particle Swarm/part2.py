import sys

class Particle:

    def __init__(self, i, p, v, a):
        self.num = i
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
        self.others = dict()

    def getposition(self):
        retstr = str(self.px)
        retstr += "-" + str(self.py)
        retstr += "-" + str(self.pz)
        return retstr

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.vz
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def getdistance(self, other):
        x = abs(abs(self.px) - abs(other.px))
        y = abs(abs(self.py) - abs(other.py))
        z = abs(abs(self.pz) - abs(other.pz))
        return x + y + z

    def comingorgoing(self, particles):
        for k in self.others:
            if k not in particles:
                self.others.pop(k, None)

        for k in particles:
            if k == self.num:
                continue
            else:
                if self.getdistance(particles[k]) <


particles = dict()

with open(sys.argv[1], 'r') as f:
    i = 0
    for line in f:
        line = line.strip()
        p, v, a = line.split(", ")
        p = p.strip("p=<").strip(">").split(",")
        v = v.strip("v=<").strip(">").split(",")
        a = a.strip("a=<").strip(">").split(",")
        particles[i] = Particle(i, p, v, a)
        i += 1

count = 0
while True:
    alive = 0
    for k in particles:
        particles[k].tick()
        alive += 1
    print("alive:", alive, "--", count)

    for k in particles:
        particles[k].comingorgoing(particles)

    a = 0
    collisions = list()
    while a < len(particles):
        if particles[a].alive:
            b = 0
            apos = particles[a].getposition()
            if apos in collisions:
                particles[a].alive = False
            while b < len(particles):
                if a == b:
                    pass
                elif particles[b].alive:
                    bpos = particles[b].getposition()
                    if bpos in collisions:
                        particles[b].alive = False
                    if apos == bpos:
                        print("Collided:", a, b)
                        collisions.append(apos)
                        particles[b].alive = False
                        particles[a].alive = False
                b += 1
        a += 1
    count += 1