import sys

total1478 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        r = line.rstrip().split(" | ")[1]
        for num in r.split():
            numlen = len(num)
            if (numlen == 2 or
                numlen == 3 or
                numlen == 4 or
                numlen == 7):
                total1478 += 1
print(total1478)