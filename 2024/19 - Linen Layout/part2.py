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

def beginswith(s, cache={}):
    count = 0
    if s in cache:
        count = cache[s]
    elif s == "":
        count = 1
    else:
        for towel in towels:
            if s.startswith(towel):
                count += beginswith(s[len(towel):])
    cache[s] = count
    return count

totalcount = 0

for pattern in patterns:
    count = beginswith(pattern)
    totalcount += count

print(totalcount)
