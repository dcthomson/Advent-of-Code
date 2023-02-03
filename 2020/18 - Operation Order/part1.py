import sys

lines = []

with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line.rstrip())

def domath(s, i=0):
    total = None
    while i < len(s):
        c = s[i]
        if c == ")":
            return total, i
        elif c == "+":
            op = "+"
        elif c == "*":
            op = "*"
        elif c != " ":
            if c == "(":
                num, i = domath(s, i + 1)

            else:
                num = int(c)
            if total is None:
                total = num 
            else:
                if op == "+":
                    total += num
                elif op == "*":
                    total *= num

        i += 1
    return total, i

t = 0
for line in lines:
    num = domath(line)[0]
    t += num
print(t)