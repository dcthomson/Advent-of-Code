import sys
import string

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()
        (l, r) = line.split(",")
        (l1, l2) = l.split("-")
        (r1, r2) = r.split("-")
        l1 = int(l1)
        l2 = int(l2)
        r1 = int(r1)
        r2 = int(r2)

        if l1 >= r1 and l1 <= r2:
            total += 1
        elif l2 >= r1 and l2 <= r2:
            total += 1
        elif r1 >= l1 and r1 <= l2:
            total += 1
        elif r2 >= l1 and r2 <= l2:
            total += 1

print(total)