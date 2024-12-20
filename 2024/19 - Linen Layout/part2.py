import sys

towels = []
patterns = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if "," in line:
            towels = line.split(", ")
        elif line != "":
            patterns.append(line)

count = 0

def beginswith(s):
    global count
    if s == "":
        count += 1
        # print(count)
        return
    for towel in towels:
        if s.startswith(towel):
            # print(towel, s)
            beginswith(s[len(towel):])

totalcount = 0

for pattern in patterns:
    print(pattern)
    count = 0
    beginswith(pattern)
    totalcount += count

print(totalcount)
