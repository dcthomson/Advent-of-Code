import sys
from collections import defaultdict
from itertools import combinations
from itertools import permutations

wires = {}
rules = []


with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if ":" in line:
            (k, v) = line.split(": ")
            wires[k] = int(v)
        elif "->" in line:
            rule = {}
            (gate, out) = line.split(" -> ")
            rule["output"] = out
            (l, logic, r) = gate.split()
            rule["left"] = l
            rule["logic"] = logic
            rule["right"] = r
            rules.append(rule)

def getcombinations(num):
    retlist = []

    for a in range(0,num):
        for b in range(0,num):
            for c in range(0,num):
                for d in range(0,num):
                    mydict = {}
                    mydict[a] = True
                    mydict[b] = True
                    mydict[c] = True
                    mydict[d] = True
                    if len(mydict) == 4:
                        retlist.append([a, b, c, d])
    return retlist

changed = True

while changed:
    changed = False

    for rule in rules:
        if (rule["left"] in wires and 
            rule['right'] in wires and
            rule['output'] not in wires):
            if rule['logic'] == "AND":
                if (wires[rule["left"]] == 1 and
                    wires[rule["right"]] == 1):
                    wires[rule["output"]] = 1
                else:
                    wires[rule["output"]] = 0
            elif rule['logic'] == "OR":
                if (wires[rule["left"]] == 0 and
                    wires[rule["right"]] == 0):
                    wires[rule["output"]] = 0
                else:
                    wires[rule["output"]] = 1
            elif rule['logic'] == "XOR":
                if wires[rule["left"]] != wires[rule["right"]]:
                    wires[rule["output"]] = 1
                else:
                    wires[rule["output"]] = 0
            changed = True


perms = permutations(rules, 8)

count = 0
for p in perms:
    count += 1
print(count)

exit()

xs = []
ys = []
zs = []

for k in wires:
    if k.startswith('z'):
        zs.append(k)
    if k.startswith('y'):
        ys.append(k)
    if k.startswith('x'):
        xs.append(k)

xs.sort(reverse=True)
ys.sort(reverse=True)
zs.sort(reverse=True)


xbinstr = ybinstr = zbinstr = ""

for wire in xs:
    xbinstr += str(wires[wire])
for wire in ys:
    ybinstr += str(wires[wire])
for wire in zs:
    zbinstr += str(wires[wire])

print(int(xbinstr, 2))
print(int(ybinstr, 2))
print(int(zbinstr, 2))

print(len(wires))

pairs = combinations(rules, 2)

# comb = combinations(wires.keys(), 4)

fours = combinations(list(pairs), 4)

print(len(list(fours)))

# for i in :
#     print(i)
# print(len(biglist))