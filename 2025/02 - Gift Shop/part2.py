import sys
import math

with open(sys.argv[1], "r") as f:

    invalidsum = 0

    for line in f:
        line = line.split(",")
        for rangestr in line:
            rangestart, rangeend = rangestr.split("-")
            rangestart = int(rangestart)
            rangeend = int(rangeend)

            for num in range(rangestart, rangeend + 1):
                invalids = {}
                numstr = str(num)
                strlen = len(numstr)
                for sectionlen in range(1, strlen):
                    if strlen % sectionlen == 0:
                        if numstr == numstr[:sectionlen] * int(strlen / sectionlen):
                            invalids[num] = True
                for k in invalids:
                    invalidsum += k

print(invalidsum)