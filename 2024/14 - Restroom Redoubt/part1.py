import sys
from collections import defaultdict

robots = []

xmax = 101
ymax = 103

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (p, v) = line.split()
        p = p.split("=")[1]
        p = [int(x) for x in p.split(",")]
        p = (p[0], p[1])
        v = v.split("=")[1]
        v = [int(x) for x in v.split(",")]
        v = (v[0], v[1])

        robot = {}
        robot['p'] = p
        robot['v'] = v
        robots.append(robot)

for i in range(0, 100):
    for robot in robots:
        x = robot['p'][0] + robot['v'][0]
        y = robot['p'][1] + robot['v'][1]

        if x < 0:
            x += xmax
        if y < 0:
            y += ymax
        if x >= xmax:
            x -= xmax
        if y >= ymax:
            y -= ymax

        robot['p'] = (x, y)

quads = defaultdict(int)

for robot in robots:
    if robot['p'][0] < ((xmax - 1) / 2):
        if robot['p'][1] < ((ymax - 1) / 2):
            quads['NW'] += 1
        elif robot['p'][1] > ((ymax - 1) / 2):
            quads['SW'] += 1
    elif robot['p'][0] > ((xmax - 1) / 2):
        if robot['p'][1] < ((ymax - 1) / 2):
            quads['NE'] += 1
        elif robot['p'][1] > ((ymax - 1) / 2):
            quads['SE'] += 1

total = 1

for v in quads.values():
    total *= v

print(total)