import sys
from itertools import permutations

happiness = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().split(" ")
        p1 = line[0]
        updown = line[2]
        amount = int(line[3])
        p2 = line[10]
        p2 = p2.rstrip(".")
        if p1 not in happiness:
            happiness[p1] = dict()
        if updown == 'lose':
            amount = -amount
        happiness[p1][p2] = amount

largesthappiness = False

for seating in permutations(list(happiness), len(happiness)):
    i = 0
    happynum = 0
    while i < len(seating):
        if i == 0:
            happynum += happiness[seating[i]][seating[-1]]
        else:
            happynum += happiness[seating[i]][seating[i - 1]]
        if i == len(seating) - 1:
            happynum += happiness[seating[i]][seating[0]]
        else:
            happynum += happiness[seating[i]][seating[i + 1]]
        i += 1
    if not largesthappiness or happynum > largesthappiness:
        largesthappiness = happynum

print(largesthappiness)

