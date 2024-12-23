import sys
from collections import defaultdict

pairs = defaultdict(list)

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (l,r) = line.split("-")
        pairs[l].append(r)
        pairs[r].append(l)

triplets = []

for k, v in pairs.items():
    for a in v:
        for b in v:
            if b in pairs[a]:
                triplet = sorted([k,a,b])
                if triplet not in triplets:
                    triplets.append(triplet)

count = 0
for triplet in triplets:
    found = False
    for t in triplet:
        if t.startswith("t"):
            found = True
    if found:
        count += 1

print(count)