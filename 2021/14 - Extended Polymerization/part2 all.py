import sys

polymer = ""
pairs = dict()
pair10 = dict()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if " -> " in line:
            (pair, insert) = line.split(" -> ")
            pairs[pair] = insert
        elif line != '':
            polymer = line

for k in pairs:
    p = k
    for j in range(0, 10):
        i = 0
        while True:
            try:
                p = p[:i+1] + pairs[p[i] + p[i+1]] + p[i+1:] 
                i += 2
            except:
                break
    pair10[k] = p

print(pair10)

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