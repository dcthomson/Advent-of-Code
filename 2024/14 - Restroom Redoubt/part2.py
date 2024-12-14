import sys
from collections import defaultdict
import time

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

def printrobots(robots):
    for y in range(0, ymax):
        for x in range(0, xmax):
            num = 0
            for robot in robots:
                if robot['p'][0] == x and robot['p'][1] == y:
                    num += 1
            if num:
                print(str(num), end="")
            else:
                print(".", end="")
        print()
    
i = 1

while True:
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
    if not (i - 14) % 101 and not (i - 94) % 103:
        printrobots(robots)
        print(i)
        exit()
    i += 1