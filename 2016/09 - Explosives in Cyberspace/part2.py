import sys

strlist = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        s = line.strip()

for c in s:
    strlist.append([c, 1])

weight = 0

i = 0
while i < len(strlist):
    if strlist[i][0] == "(":
        marker = ""
        i += 1
        while strlist[i][0] != ")":
            marker += strlist[i][0]
            i += 1
        length, multiplier = list(map(int, marker.split("x")))
        for j in range(i, i + length):
            j += 1
            strlist[j][1] *= multiplier
    if strlist[i][0] != ")":
        weight += strlist[i][1]
    i += 1

print(weight)