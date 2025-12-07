import sys
from time import sleep

def mergeranges(allranges):
    
    changed = False
    newranges = []

    for n1, r1 in enumerate(allranges):
        for n2, r2 in enumerate(allranges):
            if n1 == n2:
                continue
            if r2[0] >= r1[0] and r2[0] <= r1[1]: 
                changed = True
                r1[2] = 1
                r2[2] = 1
                if r2[1] >= r1[1]:
                    newranges.append([r1[0], r2[1], 0])
                else:
                    newranges.append([r1[0], r1[1], 0])
                break
            elif r2[1] >= r1[0] and r2[1] <= r1[1]: 
                changed = True
                r1[2] = 1
                r2[2] = 1
                if r2[0] <= r1[0]:
                    newranges.append([r2[0], r1[1], 0])
                else:
                    newranges.append([r1[0], r1[1], 0])
                break
        if changed:
            break
    for r in allranges:
        if not r[2]:
            newranges.append(r)

    return newranges, changed


with open(sys.argv[1], "r") as f:

    allranges = []

    for line in f:
        line = line.strip()
        if "-" in line:
            begin, end = line.split("-")
            begin = int(begin)
            end = int(end)
            allranges.append([begin, end, 0])

    changed = True
    while changed:
        allranges, changed = mergeranges(allranges)

    total = 0

    for r in allranges:
        total += r[1] - r[0] + 1

    print(total)