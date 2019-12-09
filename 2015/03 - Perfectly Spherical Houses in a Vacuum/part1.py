import sys

x = 0
y = 0
deliveries = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        for dir in line:
            if (x, y) in deliveries:
                deliveries[(x, y)] += 1
            else:
                deliveries[(x, y)] = 1
            if dir == "^":
                y += 1
            elif dir == "v":
                y -= 1
            elif dir == ">":
                x += 1
            elif dir == "<":
                x -= 1

print(len(deliveries))