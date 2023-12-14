import sys
from math import pow
from itertools import product

springs = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        springs.append(line.split())

for spr in springs:
    s = spr[0]
    print(s)
    positions = [pos for pos, char in enumerate(s) if char == "?"]
    for s in product(*(["#."] * s.count('?'))):
        #print("".join(s))
        print(s)

    print() 