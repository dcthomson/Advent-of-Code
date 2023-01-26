import sys

class Cup:

    def __init__(self, num):
        self.num = num
        self.nextcup = False

    def __str__(self):
        retstr = ""
        retstr += str(self.num) + "\n  "
        retstr += str(self.nextcup)
        return retstr
    
    def __repr__(self):
        retstr = ""
        retstr += str(self.num) + "->"
        retstr += str(self.nextcup)
        return retstr

cups = {}
prevcup = None
currentup = None
min = None
max = 1000000
lastcup = False
firstcup = False

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        for c in line:
            i = int(c)
            if min is None or i < min:
                min = i
            cups[i] = Cup(i)
            if c == line[0]:
                firstcup = i
                currentcup = i
            if c == line[-1]:
                cups[i].nextcup = int(line[0])
                lastcup = i
            if prevcup is not None:
                cups[prevcup].nextcup = i
            prevcup = i

cups[lastcup].nextcup = 10
for i in range(10, 1000000 + 1):
    cups[i] = Cup(i)
    cups[i].nextcup = i + 1

moving = []

cups[1000000].nextcup = firstcup

for move in range (1, 10000000 + 1):
    moving = []
    curcup = cups[currentcup].nextcup
    for i in range(1, 3 + 1):
        moving.append(curcup)
        curcup = cups[curcup].nextcup

    cups[currentcup].nextcup = cups[moving[2]].nextcup

    moveto = currentcup - 1
    while moveto in moving or moveto == min - 1:
        if moveto == min - 1:
            moveto = max
        else:
            moveto = moveto - 1

    cups[moving[2]].nextcup = cups[moveto].nextcup
    cups[moveto].nextcup = moving[0]

    currentcup = cups[currentcup].nextcup

curcup = 1

nextcup1 = cups[1].nextcup
nextcup2 = cups[nextcup1].nextcup

print(nextcup1 * nextcup2)