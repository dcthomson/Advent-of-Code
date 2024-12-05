import sys

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

total = 0

for u in updates:
    correctorder = True
    for r in rules:
        if r[0] in u and r[1] in u:
            if u.index(r[0]) > u.index(r[1]):
                correctorder = False
                break
    if correctorder:
        total += u[len(u)//2]

print(total)