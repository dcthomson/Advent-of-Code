import sys

x = 0
y = 0
z = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        for dir in line.strip().split(","):
            if dir == 'n':
                y += 1
                z -= 1
            elif dir == 'ne':
                x += 1
                z -= 1
            elif dir == 'se':
                x += 1
                y -= 1
            elif dir == 's':
                y -= 1
                z += 1
            elif dir == 'sw':
                x -= 1
                z += 1
            elif dir == 'nw':
                x -= 1
                y += 1

coords = [abs(x),abs(y),abs(z)]
print(max(coords))