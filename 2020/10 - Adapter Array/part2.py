import sys

adapters = []

with open(sys.argv[1], "r") as f:
    for line in f:
        adapters.append(int(line.rstrip()))

adapters.sort()

arrangements = 1

for i in adapters:
    nextpossible = 0
    if i + 1 in adapters:
        nextpossible += 1
    if i + 2 in adapters:
        nextpossible += 1
    if i + 3 in adapters:
        nextpossible += 1

    if nextpossible > 1:
        print(i, nextpossible)
        arrangements *= nextpossible

print(arrangements)