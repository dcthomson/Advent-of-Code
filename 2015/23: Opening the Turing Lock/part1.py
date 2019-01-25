import sys

instructions = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        instructions.append(line)

regs = dict()
regs['a'] = 0
regs['b'] = 0

index = 0

while True:
    try:
        instruction = instructions[index]
    except IndexError:
        break
#    print("index:", index, "   a:", regs['a'], "   b:", regs['b'])
#    print(instruction)
    if instruction.startswith("hlf"):
        reg = instruction.split()[1]
        regs[reg] /= 2
        index += 1
    elif instruction.startswith("tpl"):
        reg = instruction.split()[1]
        regs[reg] *= 3
        index += 1
    elif instruction.startswith("inc"):
        reg = instruction.split()[1]
        regs[reg] += 1
        index += 1
    elif instruction.startswith("jmp"):
        offset = instruction.split()[1]
        index += int(offset)
    elif instruction.startswith("jie"):
        (_, reg, offset) = instruction.split()
        reg = reg.strip(",")
        offset = offset.strip("+")
        if regs[reg] % 2 == 0:
            index += int(offset)
        else:
            index += 1
    elif instruction.startswith(""):
        (_, reg, offset) = instruction.split()
        reg = reg.strip(",")
        offset = offset.strip("+")
        if regs[reg] == 1:
            index += int(offset)
        else:
            index += 1
#    print("index:", index, "   a:", regs['a'], "   b:", regs['b'])
#    print()

print(regs['b'])
