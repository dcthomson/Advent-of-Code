import sys
from itertools import combinations

origgroups = []

with open(sys.argv[1], "r") as f:
  
    for line in f:
        line = line.strip()

        group = {}

        for c in line.replace(':', '').split():
            group[c] = True
        origgroups.append(group)

components = {}

for g in origgroups:
    for c in g:
        components[c] = True

for removals in combinations(components.keys(), 3):

    groups = origgroups.copy()

    for g in groups:
        print(g)
    print(removals)

    for g in groups:
        for r in removals:
            if r in g:
                del g[r]

    for g in groups:
        print(g)



    somethingchanged = True

    while somethingchanged:

        somethingchanged = False
        newgroups = []
        combinedgroups = []

        for c in combinations(groups, 2):
            g1 = c[0]
            g2 = c[1]
            makenewgroup = False
            newgroup = {}
            for c1 in g1:
                newgroup[c1] = True
                for c2 in g2:
                    newgroup[c2] = True
                    if c1 == c2:
                        somethingchanged = True
                        makenewgroup = True
            
            if makenewgroup:
                newgroups.append(newgroup)
                combinedgroups.append(g1)
                combinedgroups.append(g2)
                break
        
        for g in groups:
            if g not in combinedgroups:
                newgroups.append(g)

        groups = newgroups

    for g in groups:
        print(g)