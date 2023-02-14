import sys

lines = []

with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line.rstrip())

def addmult(s):
    matharr = s.split()
    multnums = []
    op = None
    num = None
    for i in matharr:
        try:
            i = int(i)
            if num is None:
                num = i
            elif op == "+":
                num += i
            elif op == "*":
                multnums.append(num)
                num = i
        except(TypeError, ValueError) as e:
            op = i

    multnums.append(num)
    
    total = 1
    for i in multnums:
        total *= i
    return(total)

total = 0

for line in lines:
    while "(" in line:
        # find any inner () then evaluate that
        i = 0
        start = None
        while i < len(line):
            c = line[i]
            if c == "(":
                start = i
            else:
                if start is not None:
                    if c == ")":
                        newline = line[0:start]
                        newline += str(addmult(line[start + 1:i]))
                        newline += line[i + 1:]
                        line = newline
                        break
            i += 1
    total += addmult(line)

print(total)