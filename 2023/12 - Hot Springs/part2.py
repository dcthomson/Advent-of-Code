import sys
from itertools import product

springs = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (s, n) = line.split()

        n +=","
        n = n*5
        n = n[:-1]

        print(s*5, " ", end="")
        print(n)

        springs.append([s*5, n])

def parsespr(spr):
    nums = []
    s = 0
    for c in spr:
        if c == "#":
            s += 1
        else:
            if s > 0:
                nums.append(s)
            s = 0
    if s != 0:
        nums.append(s)
    return ",".join(str(x) for x in nums)
        
arrangements = 0

for spr in springs:
    arr = 0
    s = spr[0]
    positions = [pos for pos, char in enumerate(s) if char == "?"]
    newstr = s
    for l in product(*(["#."] * s.count('?'))):
        for n, p in enumerate(positions):
            newstr = newstr[:p] + l[n] + newstr[p+1:]
        if parsespr(newstr) == spr[1]:
            arrangements += 1
            arr += 1
    print(arr)
print(arrangements)
