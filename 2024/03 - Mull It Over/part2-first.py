import sys
import re

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()

        dos = [(m.start(0), m.end(0)) for m in re.finditer(r'do\(\)', line)]
        donts = [(m.start(0), m.end(0)) for m in re.finditer(r'don\'t\(\)', line)]
        muls = [(m.start(0), m.end(0)) for m in re.finditer(r"mul\(\d\d?\d?,\d\d?\d?\)", line)]

        for mul in muls:
            start = mul[0]
            lowest = 0
            do = True
            for d in dos:
                end = d[1]
                if end <= start:
                    if end > lowest:
                        lowest = end
            for d in donts:
                end = d[1]
                if end <= start:
                    if end > lowest:
                        lowest = end
                        do = False
            if do:
                (_, nums) = line[mul[0]:mul[1]].split("mul(")
                nums = nums[:-1]
                (l, r) = nums.split(",")
                total += int(l) * int(r)

    print(total)