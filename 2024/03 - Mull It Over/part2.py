import sys
import re

with open(sys.argv[1], "r") as f:

    total = 0

    # moved enabled state initialization outside for loop
    # as state has to persist across newlines
    enabled = True

    for line in f:
        s = line.strip()

        do = True

        while do or dont or mul:

            do   = re.search(r'do\(\)', s)
            dont = re.search(r'don\'t\(\)', s)
            mul  = re.search(r"mul\(\d\d?\d?,\d\d?\d?\)", s)

            if do:
                if not dont or do.start() < dont.start():
                    if not mul or do.start() < mul.start():
                        enabled = True
                        s = s[do.end():]
            if dont:
                if not do or dont.start() < do.start():
                    if not mul or dont.start() < mul.start():
                        enabled = False
                        s = s[dont.end():]
            if mul:
                if not do or mul.start() < do.start():
                    if not dont or mul.start() < dont.start():
                        if enabled:
                            (_, nums) = mul.group().split("mul(")
                            nums = nums[:-1]
                            (l, r) = nums.split(",")
                            total += int(l) * int(r)
                        s = s[mul.end():]

    print(total)