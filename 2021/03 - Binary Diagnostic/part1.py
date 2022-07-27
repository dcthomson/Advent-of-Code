import sys

totallines = 0
totalzeros = list()

with open(sys.argv[1], "r") as f:

    for line in f:
        pos = 0
        for c in line:
            if len(totalzeros) < len(line) - 1:
                totalzeros.append(0)
            if c == "0":
                totalzeros[pos] += 1
            pos += 1
        totallines += 1

halflines = totallines / 2

gamma = ""
epsilon = ""

for i in totalzeros:
    if i > halflines:
        gamma += "0"
        epsilon += "1"
    else:
        epsilon += "0"
        gamma += "1"

print(int(gamma, 2) * int(epsilon, 2))