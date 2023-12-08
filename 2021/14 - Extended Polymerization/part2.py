import sys

polymer = ""
pairs = dict()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if " -> " in line:
            (pair, insert) = line.split(" -> ")
            pairs[pair] = insert
        elif line != '':
            polymer = line


for j in range(0, 40):
    print(j)
    newpolymer = ""
    polymerlen = len(polymer)
    for i, c in enumerate(polymer):
        # print(i, c)
        newpolymer += c
        if i < polymerlen - 1:
            newpolymer += pairs[c + polymer[i+1]]
    polymer = newpolymer

elements = dict()
for c in polymer:
    if c in elements:
        elements[c] += 1
    else:
        elements[c] = 0

lowest = None
highest = 0

for e, count in elements.items():
    if count > highest:
        highest = count
    if lowest is None or count < lowest:
        lowest = count

print(highest - lowest)