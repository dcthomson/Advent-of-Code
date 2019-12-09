import sys

nicecount = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        nice = True
        line = line.strip()

        vowelcount = 0
        for c in "aeiou":
            vowelcount += line.count(c)
        if vowelcount < 3:
            nice = False
            print(line, "vowelcount: ", vowelcount)
            continue

        lastc = False
        founddouble = False
        for c in line:
            if not lastc:
                lastc = c
            else:
                if lastc == c:
                    founddouble = True
                    break
                lastc = c
        if not founddouble:
            nice = False
            print(line, "no double")
            continue

        for s in ["ab", "cd", "pq", "xy"]:
            if s in line:
                nice = False
                print(line, "found: ", s)
                break

        if nice:
            print(line, "NICE")
            nicecount += 1

print(nicecount)