import sys
from itertools import permutations

distances = dict()

shortestdist = False

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        (p1, p2) = line.split(" to ")
        (p2, dist) = p2.split(" = ")
        if p1 not in distances:
            distances[p1] = dict()
        distances[p1][p2] = int(dist)
        if p2 not in distances:
            distances[p2] = dict()
        distances[p2][p1] = int(dist)

placenum = len(distances)

for path in permutations(list(distances), len(distances)):
    i = 0
    dist = 0
    while i < placenum - 1:
        dist += distances[path[i]][path[i + 1]]

        i += 1
    if not shortestdist or dist > shortestdist:
        shortestdist = dist

print(shortestdist)