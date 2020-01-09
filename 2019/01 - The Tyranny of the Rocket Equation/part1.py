import sys
import math

with open(sys.argv[1], "r") as f:
    
    total = 0

    for line in f:

        num = int(line)
        num = num / 3
        num = math.floor(num)
        num = num - 2
        total = total + num
        print(total)

    print(total)
