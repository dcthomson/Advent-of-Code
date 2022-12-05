import sys
import string

with open(sys.argv[1], "r") as f:

    atoZ = string.ascii_lowercase + string.ascii_uppercase

    totalpriorities = 0

    line1 = line2 = line3 = ""

    for line in f:
        line = line.strip()

        if line1 == "":
            line1 = line
        elif line2 == "":
            line2 = line
        elif line3 == "":
            line3 = line
            for c in line1:
                if c in line2:
                    if c in line3:
                        totalpriorities += atoZ.index(c) + 1
                        line1 = line2 = line3 = ""
                        break

print(totalpriorities)