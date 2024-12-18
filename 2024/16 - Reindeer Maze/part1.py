import sys

maze = {}

x = y = xmax = ymax = 0
start = end = None

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0
        for c in line:
            maze[(x,y)] = c
            if c == 'S':
                start = (x,y)
            if c == 'E':
                end = (x,y)
            xmax = x
            x += 1
        ymax = y
        y += 1

moveq = []
turnq = []



while moveq or turnq:
