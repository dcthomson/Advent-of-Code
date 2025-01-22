import sys
from collections import defaultdict

# AND 00:0 01:0 11:1
# OR  00:0 01:1 11:1
# XOR 00:0 01:1 11:0

wires = {}
rules = {}

numbits = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if ":" in line:
            (k, v) = line.split(": ")
            wires[k] = int(v)
        elif "->" in line:
            (gate, out) = line.split(" -> ")
            rules[out] = {}
            (l, logic, r) = gate.split()
            rules[out]["l"] = l
            rules[out]["op"] = logic
            rules[out]["r"] = r
            if out.startswith("z"):
                if int(out[1:3]) > numbits:
                    numbits = int(out[1:3])

carry = 0

def getbit(s):
    if s in wires:
        # print(" ", s, wires[s])
        return wires[s]
    else:
        # print(s, rules[s])
        l = getbit(rules[s]['l'])
        r = getbit(rules[s]['r'])
        if rules[s]["op"] == "AND":
            if l and r:
                return 1
            else:
                return 0
        elif rules[s]["op"] == "OR":
            if l or r:
                return 1
            else:
                return 0
        elif rules[s]["op"] == "XOR":
            if l != r:
                return 1
            else:
                return 0

def bintostr(numlist):
    return ''.join(str(i) for i in numlist)

def addbins(x, y):
    return bin(int(bintostr(x), 2) + int(bintostr(y), 2))[2:]

xlist = []
ylist = []
zlist = []

for init in ((None, None), (0,0), (0,1), (1,0), (1,1)):

    for i in range(0, numbits + 1):
        strnum = str(i).zfill(2)
        if init[0] is None:
            try:
                xlist.append(wires["x" + strnum])
            except:
                pass
        else:
            xlist.append(init[0])
        if init[1] is None:
            try:
                ylist.append(wires["y" + strnum])
            except:
                pass
        else:
            ylist.append(init[1])

        s = "z" + strnum
        zlist.append(getbit(s))

    xlist.reverse()
    ylist.reverse()
    zlist.reverse()
    xstr = ''.join(str(i) for i in xlist)
    ystr = ''.join(str(i) for i in ylist)
    zstr = ''.join(str(i) for i in zlist)
    realsum = bin(int(xstr, 2) + int(ystr, 2))[2:]
