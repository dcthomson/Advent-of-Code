import sys

nums = {}
lastnum = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        strnums = line.split(",")
        inputlen = len(strnums)
        for i in range(0, inputlen):
            lastnum = int(strnums[i])
            if i != inputlen - 1:
                nums[lastnum] = i

for i in range(len(nums), 30000000 - 1):
    if lastnum in nums:
        newlastnum = i - nums[lastnum]
        nums[lastnum] = i
        lastnum = newlastnum
    else:
        nums[lastnum] = i
        lastnum = 0
print(lastnum)