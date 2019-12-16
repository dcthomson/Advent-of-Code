import sys

basepattern = [0, 1, 0, -1]

with open(sys.argv[1]) as f:
    signal = f.readline()
    # turn string insto a list of ints
    l = list(map(int, list(signal)))

    for i in range(1, len(l) + 1):
        j = i
        if i == 1:
            j += 1
        for j in range(0, j):
            l[i - 1] * basepattern[j]