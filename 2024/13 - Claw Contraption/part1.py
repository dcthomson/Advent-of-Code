import sys
from collections import defaultdict

clawmachines = []

with open(sys.argv[1], "r") as f:

    a = None
    b = None
    p = None


    for line in f:
        line = line.strip()

        if "Button A" in line:
            (_,_,x,y) = line.split()
            x = x.lstrip("X+")
            ax = int(x.rstrip(","))
            ay = int(y.lstrip("Y+"))
        elif "Button B" in line:
            (_,_,x,y) = line.split()
            x = x.lstrip("X+")
            bx = int(x.rstrip(","))
            by = int(y.lstrip("Y+"))
        elif "Prize" in line:
            (_,x,y) = line.split()
            x = x.lstrip("X=")
            px = int(x.rstrip(","))
            py = int(y.lstrip("Y="))

            a = (ax, ay)
            b = (bx, by)
            p = (px, py)
            clawmachines.append((a, b, p))

totaltokens = 0

for cm in clawmachines:
    tokens = False
    for a in range(0, 100):
        for b in range(0, 100):
            x = cm[0][0] * a
            y = cm[0][1] * a
            x += cm[1][0] * b
            y += cm[1][1] * b
            if x == cm[2][0] and y == cm[2][1]:
                t = tokens = 3 * a + b
                if not tokens:
                    tokens = t
                elif t < tokens:
                    tokens = t
    if tokens:
        totaltokens += tokens

print(totaltokens)