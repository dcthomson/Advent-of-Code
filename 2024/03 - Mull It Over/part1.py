import sys
import re

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()

        muls = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", line)

        for mul in muls:
            (_, nums) = mul.split("mul(")
            nums = nums[:-1]
            (f, s) = nums.split(",")
            total += int(f) * int(s)

    print(total)