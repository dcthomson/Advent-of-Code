import sys

cmap = dict()

with open(sys.argv[1], "r") as f:
    for line in f:
        (l, r) = line.rstrip().split("-")
        if l not in cmap:
            cmap[l] = [r]
        else:
            cmap[l].append(r)
        if r not in cmap:
            cmap[r] = [l]
        else:
            cmap[r].append(l)

def traverse(cmap, cave, total=0, path=[list(), False]):
    newpath = [path[0].copy(), path[1]]
    newpath[0].append(cave)
    for c in cmap[cave]:
        if c == "end":
            total += 1
            newpath[0].append(c)
        else:
            if c == 'start' or (c.islower() and 
                                c in newpath[0] and 
                                newpath[1]):
                # can't go to lowercase cave twice
                continue
            else:
                if c.islower() and c in newpath[0]:
                    total = traverse(cmap, c, total, [newpath[0], True])
                else:
                    total = traverse(cmap, c, total, newpath)
    return total

print(traverse(cmap, 'start'))