import sys
import math

with open(sys.argv[1], "r") as f:

    coords = []

    for line in f:
        line = line.strip()
        x,y = line.split(",")
        coords.append((int(x), int(y)))

    area = 0

    for c1 in coords:
        for c2 in coords:
            a = abs(c1[0] - c2[0] + 1) * abs(c1[1] - c2[1] + 1)
            if a > area:
                area = a

    print(area)