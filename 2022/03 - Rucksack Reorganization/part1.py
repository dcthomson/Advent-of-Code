import sys
import string

with open(sys.argv[1], "r") as f:

    atoZ = string.ascii_lowercase + string.ascii_uppercase

    totalpriorities = 0

    for line in f:
        line = line.strip()

        compartmentsize = int(len(line) / 2)

        comp1 = line[0 : compartmentsize]
        comp2 = line[compartmentsize:]

        for c in comp1:
            if c in comp2:
                totalpriorities += atoZ.index(c) + 1
                break

print(totalpriorities)