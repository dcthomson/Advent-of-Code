import sys
import time
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

# print(rules)

def printrule(wire, indent = ""):
    print(indent + wire, end=" ")
    try:
        print(rules[wire]["l"], end=" ")
        print(rules[wire]["op"], end=" ")
        print(rules[wire]["r"], end=" ")
        print()
        printrule(rules[wire]["l"], indent + "  ")
        printrule(rules[wire]["r"], indent + "  ")
    except KeyError:
        print()
        return
    if wire.startswith("z"):
        print(wire)
    

for i in range(numbits + 1):
     printrule("z" + f"{i:02}")
     print()
     print()
     time.sleep(2)