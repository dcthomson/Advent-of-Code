import sys

first = 0
with open(sys.argv[1]) as f:
    line = f.readline()
    index = 0
    nums = line.rstrip().split(",")
    nums = list(map(int, nums))
    nums[1] = 12
    nums[2] = 2
    while nums[index] != 99:
        # print(nums)
        if nums[index] == 1:
            nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
        elif nums[index] == 2:
            nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
        index += 4
    first = nums[0]
print(first)