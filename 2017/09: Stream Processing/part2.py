import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        total = depth = totalgarbage= 0
        depth = 0
        garbage = False
        cancelnext = False
        for c in line:
            if cancelnext:
                cancelnext = False
                continue
            if c == "!":
                cancelnext = True
            if c == ">":
                garbage = False
            if garbage:
                if c != "!":
                    totalgarbage += 1
                continue
            if c == "<":
                garbage = True
            if c == "{":
                depth += 1
                total += depth
#                print("total:", total)
            elif c == "}":
                depth -= 1
            lastc = c
        print(totalgarbage)