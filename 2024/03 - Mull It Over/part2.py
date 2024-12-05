import sys
import re

with open(sys.argv[1], "r") as f:

    total = 0
    do = True

    for line in f:
        s = line.strip()

        regex = re.findall(r"do\(\)|don\'t\(\)|mul\(\d\d?\d?,\d\d?\d?\)", s)

        for r in regex:
            if r.startswith("mul"):
                if do:
                    numsstr = re.findall(r'\((.*?)\)', r)
                    nums = numsstr[0].split(",")
                    total += int(nums[0]) * int(nums[1])
            elif r.startswith("don"):
                do = False
            elif r.startswith("do"):
                do = True

    print(total)
