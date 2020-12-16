import sys

nums = []

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        for i in line.split(","):
            nums.append(int(i))

print(nums)

for i in range(len(nums) - 1, 2019):
    num = nums[-1]
    found = False
    for j in range(len(nums) - 2, -1, -1):
        if nums[j] == num:
            nums.append(i - j)
            found = True
            break
    if not found:
        nums.append(0)

print(nums[-1])