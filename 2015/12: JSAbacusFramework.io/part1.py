import sys
import re

with open(sys.argv[1], 'r') as f:
    for line in f:
        nums = list(map(int, re.findall("[-\d]+", line)))
        print(nums)

total = 0
for i in nums:
    total += i

print(total)