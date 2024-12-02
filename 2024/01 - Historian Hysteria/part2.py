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

for l in left:
    num = 0
    for r in right:
        if l == r:
            num += 1
    total += l * num

print(total)