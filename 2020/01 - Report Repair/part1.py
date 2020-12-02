import sys

nums = []

with open(sys.argv[1], "r") as f:

    for line in f:
        nums.append(int(line))

for i in nums:
    for j in nums:
        if i + j == 2020:
            print(i * j)
            exit()
