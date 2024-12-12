import sys
from collections import defaultdict

stones = defaultdict(int)
newstones = defaultdict(int)

# 2 realizations:
#   order doesn't matter
#   there are lots of duplicate numbers

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        for x in line.split():
            x = int(x)
            stones[x] += 1

for i in range(0, 75):
    for stonenum, stonecount in stones.items():

        if stonenum == 0:
            newstones[1] += stonecount
        elif not len(str(stonenum)) % 2:
            s = str(stonenum)
            mid = len(s) // 2
            newstones[int(s[:mid])] += stonecount
            newstones[int(s[mid:])] += stonecount
        else:
            newstones[stonenum * 2024] = stonecount

    stones = newstones.copy()
    newstones = defaultdict(int)

total = 0 
for stonenum, stonecount in stones.items():
    total += stonecount

print(total)

exit()

for _ in range(0,25):
    j=0
    for i in range(0, len(stones)):
        k = i+j
        if stones[k] == 0:
            stones[k] = 1
        elif not len(str(stones[k])) % 2:
            s = str(stones[k])
            mid = len(s) // 2
            stones[k] = int(s[:mid])
            j += 1
            stones.insert(k+1, int(s[mid:]))
        else:
            stones[k] *= 2024
print(len(stones))