import sys

prevnum = -1

largercount = -1

with open(sys.argv[1], "r") as f:

    for line in f:
        i = int(line)
        if i > prevnum:
            largercount += 1
        prevnum = i

print(largercount)