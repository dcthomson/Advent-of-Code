import sys
import math

with open(sys.argv[1], "r") as f:

    seatids = list()

    for line in f:
        lrow = 0
        hrow = 127
        lcol = 0
        rcol = 7

        line = line.rstrip()
        for c in line:
            if c == "F":
                hrow = lrow + math.floor((hrow - lrow) / 2)
            if c == "B":
                lrow = hrow - math.floor((hrow - lrow) / 2)
            if c == "L":
                rcol = lcol + math.floor((rcol - lcol) / 2)
            if c == "R":
                lcol = rcol - math.floor((rcol - lcol) / 2)
        seatid = lrow * 8 + lcol
        seatids.append(seatid)
    seatids.sort()
    for i in range(seatids[0], seatids[-1]):
        if i not in seatids:
            print(i)