import sys

wires = dict()
instructions = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        instructions[line.strip()] = False

while True:
    oldwires = wires.copy()
    for i in instructions:
        if not instructions[i]:
            if "AND" in i:
                (l, r) = i.split(" -> ")
                (l, m) = l.split(" AND ")
                try:
                    int(l)
                    if m in wires:
                        wires[r] = 1 & wires[m]
                        instructions[i] = True
                except ValueError:
                    if l in wires and m in wires:
                        wires[r] = wires[l] & wires[m]
                        instructions[i] = True
            elif "OR" in i:
                (l, r) = i.split(" -> ")
                (l, m) = l.split(" OR ")
                if l in wires and m in wires:
                    wires[r] = wires[l] | wires[m]
                    instructions[i] = True
            elif "LSHIFT" in i:
                (l, r) = i.split(" -> ")
                (l, lshiftnum) = l.split(" LSHIFT ")
                if l in wires:
                    wires[r] = wires[l] << int(lshiftnum)
                    instructions[i] = True
            elif "RSHIFT" in i:
                (l, r) = i.split(" -> ")
                (l, rshiftnum) = l.split(" RSHIFT ")
                if l in wires:
                    wires[r] = wires[l] >> int(rshiftnum)
                    instructions[i] = True
            elif "NOT" in i:
                tmp = i.lstrip("NOT ")
                (l, r) = tmp.split(" -> ")
                if l in wires:
                    wires[r] = ~wires[l]
                    if wires[r] < 0:
                        wires[r] = 65536 + wires[r]
                        instructions[i] = True
            elif "->" in i:
                (l, r) = i.split(" -> ")
                try:
                    int(l)
                    if r == "b":
                        wires[r] = 956
                    else:
                        wires[r] = int(l)
                        instructions[i] = True
                except ValueError:
                    if l in wires:
                        if r == "b":
                            wires[r] = 956
                        else:
                            wires[r] = wires[l]
                        instructions[i] = True
    if oldwires == wires:
        print(wires["a"])
        break