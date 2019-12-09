import sys

count = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        sides = line.split()
        for i in range(0, 3):
            sides[i] = int(sides[i])

        triangle = True
        if sides[0] + sides[1] <= sides[2]:
            triangle = False
        elif sides[1] + sides[2] <= sides[0]:
            triangle = False
        elif sides[0] + sides[2] <= sides[1]:
            triangle = False
        if triangle:
            count += 1

print(count)