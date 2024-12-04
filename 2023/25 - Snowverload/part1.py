import sys
import copy
from itertools import combinations

origconnections = {}
componentcombos = []

with open(sys.argv[1], "r") as f:
  
    for line in f:
        line = line.strip()

        (l, r) = line.split(": ")
            
        rs = r.split()
        try:
            origconnections[l] = origconnections[l] + rs
        except:
            origconnections[l] = rs
        for r in rs:
            componentcombos.append([l, r])
            try:
                origconnections[r].append(l)
            except:
                origconnections[r] = [l]

# put all data into original dict --DONE

# for c, links in origconnections.items():
    # print(c, links)

# for loop combination of 3 names in component names
# FIXME
for removals in combinations(componentcombos, 3):
    # print("removals", removals)
    # removals = (('pzl', 'hfx'), ('cmg', 'bvb'), ('jqt', 'nvd'))
    # create copy of original dict
    connections = copy.deepcopy(origconnections)
    # for each name in combination
    for r in removals:
        connections[r[0]].remove(r[1])
        connections[r[1]].remove(r[0])

    # for c, links in connections.items():
        # print(c, links)

    # check number of groups
    groups = []
    # loop copy of original dict
    for c in connections:
        g = connections[c]
        g = g + [c]
        g = list(set(g))
        groups.append(g)

    # print()
    # print()

    # -- combine groups
    foundlink = True
    while foundlink:
        # print(len(groups), groups)
        foundlink = False
        # loop groups as g1 and enumerate
        g1num = None
        g2num = None
        for n1, g1 in enumerate(groups):
            # loop groups as g2 and enumerate
            for n2, g2 in enumerate(groups):
                if n1 != n2:
                    if [i for i in g1 if i in g2]:
                        g1num = n1
                        g2num = n2
                        foundlink = True
                        break
        if foundlink:
            newgroup = list(set(groups[g1num] + groups[g2num]))
            groups.append(newgroup)
            for i in sorted([g1num, g2num], reverse=True):
                # print(i, groups)
                try:
                    del groups[i]
                except IndexError:
                    break

    if len(groups) == 2:
        # print(removals)
        # print(groups)
        print(len(groups[0]) * len(groups[1]))
        break        