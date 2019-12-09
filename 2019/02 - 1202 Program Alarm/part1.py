import sys

with open(sys.argv[1]) as f:
    index = 0
    for line in f:
        nums = line.split(",")
        nums = list(map(int, nums))
        nums[1] = 12
        nums[2] = 2
        while nums[index] != 99:
            print(nums)
            if nums[index] == 1:
                nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
            elif nums[index] == 2:
                nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
            index += 4
        print(nums)