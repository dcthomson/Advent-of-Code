import sys
from collections import defaultdict

keys = []
locks = []
linecount = 0
with open(sys.argv[1], "r") as f:

    type = False
    heights = defaultdict(int)
    for line in f:
        linecount += 1
        line = line.strip()
            
        if "#####" == line:
            if linecount == 1:
                type = "lock"
                continue
            elif linecount == 7:
                type = "key"
                continue
        if line == "":
            h = []
            for i in range(0,5):
                h.append(heights[i])
            if type == "key":
                keys.append(h)
            elif type == "lock":
                locks.append(h)
            heights = defaultdict(int)
            type = False
            linecount = 0
        else:
            linelist = list(line)
            for n, c in enumerate(linelist):
                if c == "#":
                    heights[n] += 1

    h = []
    for i in range(0,5):
        h.append(heights[i])
    if type == "key":
        keys.append(h)
    elif type == "lock":
        locks.append(h)
    heights = defaultdict(int)

total = 0

for l in locks:
    for k in keys:
        fits = True
        for i in range(0,5):
            if l[i] + k[i] > 5:
                fits = False
                break
        if fits:
            total += 1

print(total)