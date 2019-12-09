import sys

listsize = 256

lengths = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        lengths = [int(x) for x in line.split(",")]

dalist = list(range(0, listsize))

pos = 0
skipsize = 0

for length in lengths:
    sublist = list()
    tmppos = pos
    for _ in range(length):
        try:
            sublist.append(dalist[tmppos])
        except IndexError:
            tmppos = 0
            sublist.append(dalist[tmppos])
        tmppos += 1
    sublist = list(reversed(sublist))

    tmppos = pos
    for i in range(length):
        try:
            dalist[tmppos] = sublist[i]
        except IndexError:
            tmppos = 0
            dalist[tmppos] = sublist[i]
        tmppos += 1

    for _ in range(length + skipsize):
        if pos >= len(dalist):
            pos = 0
        pos += 1
    skipsize += 1
print(dalist[0] * dalist[1])