import sys

first = 0
with open(sys.argv[1]) as f:
    line = f.readline()

    orignums = line.rstrip().split(",")
    orignums = list(map(int, orignums))

    for x in range(0, 100):
        for y in range(0, 100):
            index = 0
            nums = orignums.copy()
            nums[1] = x
            nums[2] = y
            while nums[index] != 99:
                # print(nums)
                if nums[index] == 1:
                    nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
                elif nums[index] == 2:
                    nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
                index += 4
            first = nums[0]
            if first == 19690720:
                print(100 * x + y)
                exit()