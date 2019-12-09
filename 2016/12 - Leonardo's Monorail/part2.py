import sys

instructions = []

with open(sys.argv[1]) as f:
    for line in f:
        instructions.append(line.strip())

regs = {'c': 1}

instindex = 0
while instindex < len(instructions):

    try:
        (command, val1, val2) = instructions[instindex].split()
    except:
        (command, val1) = instructions[instindex].split()
    if command == 'cpy':
        try:
            regs[val2] = int(val1)
        except:
            regs[val2] = regs[val1]
    elif command == 'inc':
        regs[val1] += 1
    elif command == 'dec':
        regs[val1] -= 1
    elif command == 'jnz':
        jump = False
        try:
            if int(val1) != 0:
                jump = True
        except:
            if val1 not in regs:
                jump = False
            elif regs[val1] != 0:
                jump = True
        if jump:
            instindex += int(val2)
            continue
    instindex += 1

print(regs['a'])