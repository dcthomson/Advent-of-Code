import sys
import itertools

nums = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        nums.append(int(line.strip()))

for p in itertools.permutations(nums):
    print(p)