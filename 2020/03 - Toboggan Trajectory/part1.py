import sys

treekey = list()
treemap = list()

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.rstrip()
        treekey.append(line)
        treemap.append(line)

x = 0
y = 0

trees = 0

while y < len(treemap) - 1:
    x += 3
    y += 1
    while len(treemap[y]) <= x:
        treemap[y] += treekey[y]
    if treemap[y][x] == "#":
        trees += 1

print(trees)