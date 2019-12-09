import sys

class Disc:

    def __init__(self, positions, position):
        self.positions = positions
        self.position = position

    def open(self, time):
        pos = time % self.positions + self.position
        if pos >= self.positions:
            pos = pos - self.positions
        if pos == 0:
            return True
        return False

discs = {}

with open(sys.argv[1]) as f:
    for line in f:
        linebits = line.split()
        discnum = linebits[1].lstrip("#")
        positions = linebits[3]
        position = linebits[11].rstrip(".")
        discs[int(discnum)] = Disc(int(positions), int(position))

gotcapsule = False
time = 0

while not gotcapsule:
    discnum = 1
    gotcapsule = True
    for k, v in discs.items():
        if not v.open(time + k):
            # capsule bounced out
            gotcapsule = False
            time += 1
            break

print(time)