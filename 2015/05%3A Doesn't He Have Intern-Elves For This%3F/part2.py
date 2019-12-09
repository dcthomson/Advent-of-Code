import sys

nicecount = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        nice = True
        line = line.strip()

        doubles = dict()
        i = 0
        founddouble = False
        foundpali = False
        while i < len(line):
            try:
                if line[i] + line[i + 1] in doubles:
                    if doubles[line[i] + line[i + 1]] != i - 1:
                        founddouble = line[i] + line[i + 1]
                else:
                    doubles[line[i] + line[i + 1]] = i
                if line[i] == line[i + 2]:
                    foundpali = line[i] + line[i + 1] + line[i + 2]
            except IndexError:
                pass
            i += 1
        if not founddouble:
            nice = False

        if not foundpali:
            nice = False

        if nice:
            nicecount += 1

print(nicecount)