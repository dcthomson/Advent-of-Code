import sys
from math import lcm

leftright = ""
dirs = {}
pos = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if "=" not in line:
            if line != "":
                leftright = line
        else:
            (d, lr) = line.split(" = ")
            lr = lr.replace("(", "")
            lr = lr.replace(")", "")
            (l, r) = lr.split(", ")
            if d.endswith("A"):
                pos.append(d)
            dirs[d] = {}
            dirs[d]['L'] = l
            dirs[d]['R'] = r

steplist = []

for position in pos:

    steps = 0
    p = position
    foundend = False
    while not foundend:
        for lr in leftright:
            steps += 1
            p = dirs[p][lr]
            if p.endswith("Z"):
                steplist.append(steps)
                foundend = True

print(lcm(*steplist))