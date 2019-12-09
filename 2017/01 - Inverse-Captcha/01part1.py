import sys

if sys.argv[1].isdigit():
    nums = list(sys.argv[1].rstrip())
else:
    f = open(sys.argv[1], "r")

    for line in f:
        nums = list(line.rstrip())

last = False
total = 0
first = nums[0]
for num in nums:
    num = int(num)
    if last:
        if last == num:
            total += num
    last = num

if int(last) == int(first):
    total += last

print(total)