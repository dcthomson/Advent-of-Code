import sys

f = open(sys.argv[1], 'r')

checksum = 0

for line in f:
    low = False
    high = False
    nums = list(map(int, line.rstrip().split()))
    numlen = len(nums)
    i = 0
    while i < numlen:
        j = 0
        while j < numlen:
            if i != j:
                if nums[i] % nums[j] == 0:
                    checksum += int(nums[i] / nums[j])
            j += 1
        i += 1
print(checksum)
