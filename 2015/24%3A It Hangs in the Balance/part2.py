import sys
from functools import reduce

weights = list()
totalweight = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        weights.append(int(line))
        totalweight += int(line)

compartmentweight = int(totalweight / 4)
compartmentsets = []

def subset_sum(numbers, target, cs, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        cs.append(partial)
    if s >= target:
        return cs # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        cs = subset_sum(remaining, target, cs, partial + [n])
    return cs
compartmentsets = subset_sum(weights, compartmentweight, compartmentsets)

shortest = False
for cs in compartmentsets:
    if not shortest or shortest > len(cs):
        shortest = len(cs)

smallest = False
for cs in compartmentsets:
    if len(cs) == shortest:
        qe = reduce(lambda x, y: x*y, cs)
        if not smallest or qe < smallest:
            smallest = qe
print(smallest)
