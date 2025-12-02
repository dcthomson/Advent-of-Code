import sys

with open(sys.argv[1], "r") as f:

    invalidsum = 0

    for line in f:
        line = line.split(",")
        for rangestr in line:
            rangestart, rangeend = rangestr.split("-")
            rangestart = int(rangestart)
            rangeend = int(rangeend)

            for i in range(rangestart, rangeend + 1):
                numstr = str(i)
                strlen = len(numstr)
                if not strlen % 2:
                    half = int(strlen / 2)
                    if numstr[:half] == numstr[half:]:
                        invalidsum += i

print(invalidsum)