import sys

if sys.argv[1].isdigit():
    nums = list(sys.argv[1].rstrip())
else:
    f = open(sys.argv[1], "r")

    for line in f:
        nums = list(line.rstrip())

total = 0
numlen = len(nums)
oppoffset = int(numlen / 2)
i = 0
while i <= numlen:
    try:
        if int(nums[i]) == int(nums[i + oppoffset]):
            total += int(nums[i])
            total += int(nums[i])
    except IndexError:
        pass
    i += 1

print(total)
