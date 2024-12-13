import sys
from sympy import symbols, Eq, solve

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
            cm = {}
            cm["ax"] = ax
            cm["bx"] = bx
            cm["ay"] = ay
            cm["by"] = by
            cm["x"] = px + 10000000000000
            cm["y"] = py + 10000000000000
            clawmachines.append(cm)

totaltokens = 0

a, b = symbols('a b')

for cm in clawmachines:

    eq1 = Eq(cm["ax"]*a + cm["bx"]*b, cm["x"])
    eq2 = Eq(cm["ay"]*a + cm["by"]*b, cm["y"])

    solution = solve((eq1, eq2), (a, b))
    if (solution[a].is_integer):
        if (solution[b].is_integer):
            totaltokens += solution[a]*3 + solution[b]

print(totaltokens)