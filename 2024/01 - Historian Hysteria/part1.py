import sys

left = []
right = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        (l, r) = line.split("   ")
        left.append(int(l))
        right.append(int(r))

total = 0

left.sort()
right.sort()

for n, i in enumerate(left):
    total += abs(left[n] - right[n])

print(total)