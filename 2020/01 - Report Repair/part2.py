import sys
import math

nums = []

with open(sys.argv[1], "r") as f:

    for line in f:
        nums.append(int(line))

for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                print(i * j * k)
                exit()