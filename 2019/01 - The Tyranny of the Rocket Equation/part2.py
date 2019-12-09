import sys
import math

def calc_fuel(num):
    num = num / 3
    num = math.floor(num)
    return num - 2

with open(sys.argv[1], "r") as f:
    
    total = 0

    for line in f:
        num = int(line)
        modtotal = 0

        while num > 0:
            num = calc_fuel(num)
            if num > 0:
                modtotal += num

        total += modtotal

    print(total)