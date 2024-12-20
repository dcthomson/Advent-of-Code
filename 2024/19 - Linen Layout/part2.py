import sys

towels = []
patterns = []

with open(sys.argv[1], "r") as f:

    blocks = 0
    for line in f:
        line = line.strip()

        if "," in line:
            towels = line.split(", ")
        elif line != "":
            patterns.append(line)

q = [patterns[0]]
count = 0
while q:
    s = q.pop(0)

    for towel in towels:
        if s == towel:
            count += 1
            print(count)
        elif s.startswith(towel):
            print(s[len(towel):])
            q.append(s[len(towel):])

print(count)