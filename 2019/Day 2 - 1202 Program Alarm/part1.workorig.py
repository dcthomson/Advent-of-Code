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
    if len(sys.argv) == 2:
        nums = run_opcode(line)
    else:
        nums = run_opcode(line, int(sys.argv[2]), int(sys.argv[3]))

    print(nums)