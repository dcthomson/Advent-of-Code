import sys

count = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        for c in line.rstrip():
            if c == "#":
                count += 1

print(count)