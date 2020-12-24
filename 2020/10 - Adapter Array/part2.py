import sys

adapters = []

with open(sys.argv[1], "r") as f:
    for line in f:
        adapters.append(int(line.rstrip()))

adapters.sort()



print(one * three)