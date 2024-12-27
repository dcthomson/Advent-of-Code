import sys
from collections import defaultdict

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

for wire in wires:
    if wire.startswith("x"):
        wires[wire] = 1
    if wire.startswith("y"):
        wires[wire] = 1

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

zs = []

for k in wires:
    if k.startswith('z'):
        zs.append(k)

zs.sort(reverse=True)

binstr = ""

for z in zs:
    binstr += str(wires[z])

print(int(binstr, 2))