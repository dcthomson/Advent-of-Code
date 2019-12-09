import sys

def run_opcode(s, v1=False, v2=False):
    s = s.rstrip()
    strs = s.split(",")
    nums = list(map(int, strs))
    index = 0

    if v1:
        nums[1] = v1
    if v2:
        nums[2] = v2

    while nums[index] != 99:
        if nums[index] == 1:
            nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
        elif nums[index] == 2:
            nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
        index += 4

    return nums

with open(sys.argv[1]) as f:
    line = f.readline()

    for i in range(0, 100):
        for j in range(0, 100):
            nums = run_opcode(line, i, j)
            if nums[0] == 19690720:
                print( 100 * i + j )