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
max = None

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        for c in line:
            i = int(c)
            if max is None or i > max:
                max = i
            if min is None or i < min:
                min = i
            cups[i] = Cup(i)
            if c == line[0]:
                currentcup = i
            if c == line[-1]:
                cups[i].nextcup = int(line[0])
            if prevcup is not None:
                cups[prevcup].nextcup = i
            prevcup = i


for move in range (1, 100 + 1):
    curcup = 1
    while True:
        curcup = cups[curcup].nextcup
        if curcup == 1:
            break
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

while True:
    if curcup != 1:
        print(curcup, end="")
    curcup = cups[curcup].nextcup
    if curcup == 1:
        break