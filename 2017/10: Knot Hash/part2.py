import sys

listsize = 256

lengths = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        for c in line:
            lengths.append(ord(c))

lengths = lengths + [17, 31, 73, 47, 23]

dalist = list(range(0, listsize))

pos = 0
skipsize = 0

for _ in range(64):
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

densehash = list()
for s in zip(*[iter(dalist)]*16):
    dhelement = False
    for i in s:
        if not dhelement:
            dhelement = i
        else:
            dhelement = dhelement ^ i
    densehash.append(dhelement)

knothash = ""
for i in densehash:
    hexstr = str(hex(i))
    hexstr = hexstr.lstrip("0x")
    if len(hexstr) == 1:
        hexstr = "0" + hexstr
    knothash += hexstr

print(knothash)