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
                    founddouble = True
                    print("double: ", line[i] + line[i + 1])
                else:
                    doubles[line[i] + line[i + 1]] = 1
                if line[i] == line[i + 2]:
                    print("pali: ", line[i] + line[i + 1] + line[i + 2])
                    foundpali = True
            except IndexError:
                pass
            i += 1
        if not founddouble:
            nice = False
            print(line, "no double")

        if not foundpali:
            nice = False
            print(line, "no palindrome")

        if nice:
            print(line, "NICE")
            nicecount += 1

print(nicecount)