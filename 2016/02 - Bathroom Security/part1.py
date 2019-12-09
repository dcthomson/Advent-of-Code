import sys

steps = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        steps.append(line.strip())

keypad = dict()
keypad[(0, 0)] = 1
keypad[(1, 0)] = 2
keypad[(2, 0)] = 3
keypad[(0, 1)] = 4
keypad[(1, 1)] = 5
keypad[(2, 1)] = 6
keypad[(0, 2)] = 7
keypad[(1, 2)] = 8
keypad[(2, 2)] = 9

coord = [1, 1]

code = ""

for step in steps:
    for c in step:
        if c == 'U':
            if (coord[0], coord[1] - 1) in keypad:
                coord[1] -= 1
        if c == 'D':
            if (coord[0], coord[1] + 1) in keypad:
                coord[1] += 1
        if c == 'L':
            if (coord[0] - 1, coord[1]) in keypad:
                coord[0] -= 1
        if c == 'R':
            if (coord[0] + 1, coord[1]) in keypad:
                coord[0] += 1

    code += str(keypad[(coord[0], coord[1])])
print(code)