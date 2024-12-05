import sys
import functools

rules = []
updates = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if "|" in line:
            (l,r) = line.split("|")
            rules.append((int(l),int(r)))
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

def compare(x, y):
    for r in rules:
        if r[0] == x and r[1] == y:
            return -1
        elif r[1] == x and r[0] == y:
            return 1
    return 0

total = 0

for u in updates:
    correctorder = True
    for r in rules:
        if r[0] in u and r[1] in u:
            if u.index(r[0]) > u.index(r[1]):
                correctorder = False
                break
    if not correctorder:
        sorted_u = sorted(u, key=functools.cmp_to_key(compare))
        total += sorted_u[len(sorted_u)//2]

print(total)