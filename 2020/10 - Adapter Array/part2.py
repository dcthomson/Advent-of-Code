import sys

adapters = [0]

with open(sys.argv[1], "r") as f:
    for line in f:
        adapters.append(int(line.rstrip()))

adapters.sort()

arrsegments = []

segment = []

for i in adapters:
    paths = 0
    if not i in segment:
        segment.append(i)
    for j in range(1, 4):
        if i + j in adapters:
            paths += 1
            if not i + j in segment:
                segment.append(i + j)
    if paths == 1:
        arrsegments.append(segment.copy())
        segment = []  

def getnext(i):
    if i == max:
        global arrangements
        arrangements += 1
    for j in range(1, 4):
        if i + j in segment:
            getnext(i + j)

total = 1

for segment in arrsegments:

    max = segment[-1]

    arrangements = 0

    getnext(segment[0])

    total *= arrangements

print(total)