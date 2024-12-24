import sys
from collections import defaultdict

wires = {}
rules = []


with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if ":" in line:
            (k, v) = line.split(": ")
            wires[k] = v
        elif "->" in line:
            rule = {}
            (gate, out) = line.split(" -> ")
            rule["output"] = out
            (l, logic, r) = gate.split()
            rule["left"] = l
            rule["logic"] = logic
            rule["right"] = r
            rules.append(rule)

print(wires)

print(rules)