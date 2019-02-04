import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        total = 0
        depth = 0
        garbage = False
        for c in line:
            if c == "<":
                garbage = True
            if garbage:

            if c == ""
            if c == "{":
                depth += 1
                total += depth
#                print("total:", total)
            elif c == "}":
                depth -= 1
            lastc = c
        print(total)