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

def beginswith(s):
    # print(s)
    if s == "":
        return True
    for towel in towels:
        # print(towel)
        if s.startswith(towel):
            ret = beginswith(s[len(towel):])
            if ret:
                return True
    return False

count = 0

for pattern in patterns:
    if beginswith(pattern):
        count += 1

print(count)