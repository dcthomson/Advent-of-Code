import sys

verts = []
max = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        for i, c in enumerate(line):
            if i > max:
                max = i
            try:
                verts[i] += c
            except IndexError:
                verts.append(c)

total = 0
for v in verts:
    s = list(v)

    positions = [pos for pos, char in enumerate(s) if char == "O"]

    for p in positions:
        for i in range(p-1, -1, -1):
            if s[i] == "#" or s[i] == "O":
                s[p] = "."
                s[i+1] = "O"
                break
            elif i == 0:
                s[p] = "."
                s[i] = "O"

    for n, c in enumerate(s):
        if c == "O":
            total += max - n + 1
print(total)
