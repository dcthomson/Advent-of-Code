import sys
import functools

stones = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        stones = [int(x) for x in line.split()]

@functools.cache
def splitstone(stone):
    s = str(stone)
    mid = len(s) // 2
    l = int(s[:mid])
    r = int(s[mid:])
    return (l, r)

@functools.cache
def mult2024(num):
    return num * 2024

unique = {}

for j in range(0,75):

    for i in range(0, len(stones)):
        if stones[i] == 0:
            stones[i] = 1
        elif not len(str(stones[i])) % 2:
            (l, r) = splitstone(stones[i])
            stones[i] = l
            stones.append(r)
        else:
            stones[i] = mult2024(stones[i])
        unique[stones[i]] = True
    print(j, len(stones), len(unique))
print(len(stones))