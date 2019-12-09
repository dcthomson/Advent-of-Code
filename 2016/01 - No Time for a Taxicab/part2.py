import sys
from itertools import cycle

dirs = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        dirs = line.split(", ")

visits = dict()
visits[(0, 0)] = 1

pointing = "N"
coord = [0,0]
nsew = ('N', 'E', 'S', 'W')

for dir in dirs:
    turn = dir[:1]
    blocks = int(dir[1:])
    initialdir = nsew.index(pointing)
    if turn == 'R':
        try:
            pointing = nsew[initialdir + 1]
        except IndexError:
            pointing = nsew[0]
    else:
        try:
            pointing = nsew[initialdir - 1]
        except IndexError:
            pointing = nsew[len(nsew) - 1]
    if pointing == "N":
        i = 0
        while i < blocks:
            coord[1] += 1
            if (coord[0], coord[1]) not in visits:
                visits[(coord[0], coord[1])] = 1
            else:
                print(abs(coord[0]) + abs(coord[1]))
                sys.exit()
            i += 1
    elif pointing == "S":
        i = 0
        while i < blocks:
            coord[1] -= 1
            if (coord[0], coord[1]) not in visits:
                visits[(coord[0], coord[1])] = 1
            else:
                print(abs(coord[0]) + abs(coord[1]))
                sys.exit()
            i += 1
    elif pointing == "E":
        i = 0
        while i < blocks:
            coord[0] += 1
            if (coord[0], coord[1]) not in visits:
                visits[(coord[0], coord[1])] = 1
            else:
                print(abs(coord[0]) + abs(coord[1]))
                sys.exit()
            i += 1
    elif pointing == "W":
        i = 0
        while i < blocks:
            coord[0] -= 1
            if (coord[0], coord[1]) not in visits:
                visits[(coord[0], coord[1])] = 1
            else:
                print(abs(coord[0]) + abs(coord[1]))
                sys.exit()
            i += 1