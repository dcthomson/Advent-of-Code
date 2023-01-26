import sys
import math

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()

        dec = 0
        pow = 0

        while line != "":
            line, c = line[:-1], line[-1] 
            if c == "-":
                c = -1
            elif c == "=":
                c = -2
            c = int(c)
            dec += int(c * math.pow(5, pow))
            pow += 1

        total += dec

print(total)