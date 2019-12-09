import sys
from itertools import cycle

dirs = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        dirs = line.split(", ")

visits = dict()

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
        coord[1] += blocks
    elif pointing == "S":
        coord[1] -= blocks
    elif pointing == "E":
        coord[0] += blocks
    elif pointing == "W":
        coord[0] -= blocks

print(abs(coord[0]) + abs(coord[1]))