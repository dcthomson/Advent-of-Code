import sys
import itertools

s = sys.argv[1]

def swap_position(s, x, y):
    c = s[x]
    s[x] = s[y]
    s[y] = c
    return s

def swap_letter(s, x, y):
    xi = False
    yi = False
    for i, c in enumerate(s):
        if c == x:
            xi = i
        if c == y:
            yi = i
    return swap_position(s, xi, yi)

def rotate_left(s, x):
    Lfirst = s[0 : x]
    Lsecond = s[x :]
    return Lsecond + Lfirst

def rotate_right(s, x):
    Rfirst = s[0 : len(s) - x]
    Rsecond = s[len(s) - x : ]
    return Rsecond + Rfirst

def rotate_position(s, x):
    for i, c in enumerate(s):
        if c == x:
            xi = i
    s = rotate_right(s, 1)
    s = rotate_right(s, xi)
    if xi >= 4:
        s = rotate_right(s, 1)
    return s

def reverse_positions(s, x, y):
    s = "".join(s)
    return list(s[0:x] + s[x:y+1][::-1] + s[y+1:])

def move_position(s, x, y):
    c = s[x]
    del s[x]
    s.insert(y, c)
    return s

lines = []

with open(sys.argv[2]) as f:
    for line in f:
        lines.append(line)

for s in itertools.permutations(s):
    orig = s

    # print("".join(s))
    s = list("".join(s))
    for line in lines:
        line = line.rstrip()
        splitline = line.split()
        if line.startswith("swap position"):
            s = swap_position(s, int(splitline[2]), int(splitline[5]))
        if line.startswith("swap letter"):
            s = swap_letter(s, splitline[2], splitline[5])
        if line.startswith("rotate left"):
            s = rotate_left(s, int(splitline[2]))
        if line.startswith("rotate right"):
            s = rotate_right(s, int(splitline[2]))
        if line.startswith("rotate based on position of letter"):
            s = rotate_position(s, splitline[6])
        if line.startswith("reverse positions"):
            s = reverse_positions(s, int(splitline[2]), int(splitline[4]))
        if line.startswith("move position"):
            s = move_position(s, int(splitline[2]), int(splitline[5]))
        # print(line + ":", "".join(s))

    if "".join(s) == "fbgdceah":
        print("Found:", "".join(orig))
        exit()