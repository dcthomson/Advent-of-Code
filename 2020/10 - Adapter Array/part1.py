import sys

adapters = []

with open(sys.argv[1], "r") as f:
    for line in f:
        adapters.append(int(line.rstrip()))

adapters.sort()

one = 0
two = 0
three = 1   # always 1 for the final jump

prev = 0

for i in adapters:
    if i - prev == 1:
        one += 1
    if i - prev == 2:
        two += 1
    if i - prev == 3:
        three += 1
    prev = i

print(one * three)