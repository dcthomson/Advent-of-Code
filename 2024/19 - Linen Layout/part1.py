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

def beginswith(s, count=0, newtowels=towels.copy()):

    if s == "":
        count += 1
    else:
        for towel in towels:
            if towel in s:
                newtowels.append(towel)
        for towel in newtowels:
            if s.startswith(towel):
                count = beginswith(s[len(towel):], count, newtowels.copy())
    return count

count = 0

for pattern in patterns:
    print(pattern, "", end="", flush=True)
    pcount = beginswith(pattern)
    print(pcount)
    count += pcount

print(count)