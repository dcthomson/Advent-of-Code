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
        self.vz += self.vz
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def getdistance(self, other):
        x = abs(self.px - other.px)
        y = abs(self.py - other.py)
        z = abs(self.pz - other.pz)
        return x + y + z

    def getothers(self, particles):
        for k in particles:
            self.others[k] = None
        # print(len(self.others))

    def checkcollisions(self, particles):
        if self.alive:
            for k in particles:
                if particles[k].alive:
                    if self.num != k:
                        if particles[k].px == self.px:
                            if particles[k].py == self.py:
                                print("YYYYYYYYYY")
                                if particles[k].pz == self.pz:
                                    print("ZZZZZZZZZZZZZZZZZZ")
                                    self.collided = True
                                    print("COLLIDED!!!")

    def comingorgoing(self, particles):
        if self.alive:
            for k in particles:
                if k != self.num:
                    if particles[k].alive:
                        dist = self.getdistance(particles[k])
                        if k in self.others:
                            if self.others[k] is None:
                                self.others[k] = dist
                            elif self.others[k] > dist:
                                self.others[k] = dist
                            else:
                                self.others.pop(k)

    def removedead(self, particles):
        remlist = list()
        for k in self.others:
            if not particles[k].alive:
                remlist.append(k)
        for k in remlist:
            self.others.pop(k)


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

for k in particles:
    particles[k].getothers(particles)

done = False
while not done:
    print("checking collisions\ncoming or going")
    for k in particles:
        particles[k].checkcollisions(particles)
        particles[k].comingorgoing(particles)

    print("setting collided to dead")
    for k in particles:
        if particles[k].collided:
            particles[k].alive = False

    print("removing dead particles from particle.others")
    for k in particles:
        particles[k].removedead(particles)

    print("checking if done")
    done = True
    totallen = 0
    for k in particles:
        # print(len(particles[k].others))
        otherslen = len(particles[k].others)
        totallen += otherslen
        if otherslen > 1:
            done = False
    print("total len:", totallen)


    print("tick\n")
    for k in particles:
        # print(particles[k].num, "", end="")
        # print(particles[k].px, particles[k].py, particles[k].pz)
        particles[k].tick()
    # print()

count = 0
for k in particles:
    if particles[k].alive:
        count += 1
print(count)

