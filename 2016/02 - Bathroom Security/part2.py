import sys

steps = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        steps.append(line.strip())

keypad = dict()
keypad[(3, 1)] = 1
keypad[(2, 2)] = 2
keypad[(3, 2)] = 3
keypad[(4, 2)] = 4
keypad[(1, 3)] = 5
keypad[(2, 3)] = 6
keypad[(3, 3)] = 7
keypad[(4, 3)] = 8
keypad[(5, 3)] = 9
keypad[(2, 4)] = 'A'
keypad[(3, 4)] = 'B'
keypad[(4, 4)] = 'C'
keypad[(3, 5)] = 'D'

coord = [1, 3]

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