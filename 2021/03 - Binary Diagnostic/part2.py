import sys

masterlist = list()

with open(sys.argv[1], "r") as f:

    for line in f:
        masterlist.append(line.rstrip())

ratings = {'ogr': 0, 'scr': 0}

for k in ratings:
    pos = 0
    rem = '0'
    binarylist = masterlist.copy()
    while len(binarylist) > 1:
        todelete = list()
        zeros = 0
        ones = 0
        for b in binarylist:
            if b[pos] == '0':
                zeros += 1
            else:
                ones += 1
        if k == 'ogr':
            if zeros <= ones:
                rem = '0'
            else:
                rem = '1'
        if k == 'scr':
            if zeros > ones:
                rem = '0'
            else:
                rem = '1'
        for index, b in enumerate(binarylist):
            if b[pos] == rem:
                todelete.append(index)
        for i in sorted(todelete, reverse=True):
            del binarylist[i]
        pos += 1
    ratings[k] = binarylist[0]

print(int(ratings['scr'], 2) * int(ratings['ogr'], 2))