import sys

total = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        hist = []

        hist.append([int(x) for x in line.split()])

        while not all(v == 0 for v in hist[-1]):
            nexthist = []

            for n, i in enumerate(hist[-1]):
                try:
                    nexthist.append(hist[-1][n+1] - hist[-1][n])
                except IndexError:
                    pass
            hist.append(nexthist.copy())

        n = 0

        for i, h in enumerate(reversed(hist)):
            if i != 0:
                n = h[0] - n
        total += n

print(total)