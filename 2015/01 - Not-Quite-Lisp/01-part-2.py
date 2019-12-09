import sys

floor = 0
position = 1

with open(sys.argv[1], 'r') as f:
    for line in f:
        for c in line:
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
            if floor < 0:
                break
            position += 1

print(position)