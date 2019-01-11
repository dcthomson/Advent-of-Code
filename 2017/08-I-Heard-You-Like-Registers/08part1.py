import sys

inst = list()
regs = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        inst.append(line.strip())
        regs[line.split()[0]] = 0
        regs[line.split()[4]] = 0

for i in inst:
    (run, cond) = i.split(" if ")
    (reg, op, val) = cond.split()
    dorun = False
    if op == "<":
        if regs[reg] < val:
            dorun = True
    elif op == ">":
        if regs[reg] > val:
            dorun = True
    elif op == ">=":
        if regs[reg] >= val:
            dorun=True
    elif op == "<=":
        if regs[reg] <= val:
            dorun = True
    elif op == "!=":
        if regs[reg] != val:
            dorun = True
    elif op == "==":
        if regs[reg] == val:
            dorun =True

    if dorun:
        (reg, incdec, val) = run.split()
        if incdec == "inc":
            regs[reg] += val
        elif incdec == "dec":
            regs[reg] -= val

print(max(regs, key=regs.get))