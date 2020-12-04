import sys

treekey = list()
treemap = list()

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.rstrip()
        treekey.append(line)
        treemap.append(line)

slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

treeproduct = 1

for slope in slopes:

    x = 0
    y = 0
    trees = 0

    while y < len(treemap) - 1:
        x += slope[0]
        y += slope[1]
        while len(treemap[y]) <= x:
            treemap[y] += treekey[y]
        if treemap[y][x] == "#":
            trees += 1

    treeproduct *= trees

print(treeproduct)