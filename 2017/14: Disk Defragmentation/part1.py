import sys

def knothash(s):

    lengths = list()

    for c in s:
        lengths.append(ord(c))

    listsize = 256

    dalist = list(range(0, listsize))
    lengths = lengths + [17, 31, 73, 47, 23]
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
    dhcount = 0
    for s in zip(*[iter(dalist)]*16):
        dhelement = False
        for i in s:
            if not dhelement:
                dhelement = i
            else:
                dhelement = dhelement ^ i
        densehash.append(dhelement)
        dhcount += 1

    kh = ""
    hexstrcount = 0
    for i in densehash:
        hexstr = str(hex(i))
        hexstr = hexstr.split("0x")[1]
        if len(hexstr) == 1:
            hexstr = "0" + hexstr
        kh += hexstr
        hexstrcount += 1

    return kh

input = sys.argv[1]

on = 0
for i in range(0, 128):
    kh = knothash(input + "-" + str(i))
    for c in kh:
        dabin = bin(int(c, 16))[2:].zfill(4)
        on += dabin.count('1')
print(on)
