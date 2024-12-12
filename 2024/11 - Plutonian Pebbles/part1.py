import sys

stones = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        stones = [int(x) for x in line.split()]

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