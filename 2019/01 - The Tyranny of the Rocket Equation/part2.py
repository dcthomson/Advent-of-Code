import sys
import math

with open(sys.argv[1], "r") as f:
    
    total = 0

    for line in f:
        num = int(line)
        modtotal = 0

        while num > 0:
            num = num / 3
            num = math.floor(num)
            num -= 2

            if num > 0:
                modtotal += num

        total += modtotal

    print(total)