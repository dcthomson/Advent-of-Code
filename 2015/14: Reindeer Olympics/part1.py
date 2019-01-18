import sys

class Reindeer:

    def __init__(self, name, speed, gotime, rest):
        self.name = name
        self.speed = int(speed)
        self.gotimetotal = int(gotime)
        self.resttimetotal = int(rest)
        self.distance = 0
        self.gotimeleft = int(gotime)
        self.resttimeleft = int(rest)
        self.state = "flying"

    def go(self):
        if self.state == "flying":
            self.distance += self.speed
            self.gotimeleft -= 1
            if self.gotimeleft == 0:
                self.state = "resting"
                self.gotimeleft = self.gotimetotal
        elif self.state == "resting":
            self.resttimeleft -= 1
            if self.resttimeleft == 0:
                self.state = "flying"
                self.resttimeleft = self.resttimetotal

reindeer = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        l = line.strip().split()
        reindeer.append(Reindeer(l[0], l[3], l[6], l[13]))

for i in range(1, 2504):
    for r in reindeer:
        r.go()

farthest = False
for r in reindeer:
    if not farthest or r.distance > farthest:
        farthest = r.distance
print(farthest)