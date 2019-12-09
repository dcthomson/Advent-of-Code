import sys

instructions = []

with open(sys.argv[1]) as f:
    for line in f:
        instructions.append(line.strip())

regs = {'a': 7}
# regs = {}

instindex = 0
while instindex < len(instructions):
    # print(instructions[instindex])
    try:
        (command, val1, val2) = instructions[instindex].split()
    except:
        (command, val1) = instructions[instindex].split()
    try:
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
                try:
                    instindex += int(val2)
                except:
                    instindex += regs[val2]
                continue
        elif command == 'tgl':
            changeindex = instindex + regs[val1]
            instarr = instructions[changeindex].split()

            if len(instarr) == 2:
                if instarr[0] == 'inc':
                    instructions[changeindex] = 'dec ' + instarr[1]
                else:
                    instructions[changeindex] = 'inc ' + instarr[1]
            elif len(instarr) == 3:
                if instarr[0] =='jnz':
                    instructions[changeindex] = 'cpy ' + instarr[1] + " " + instarr[2]
                else:
                    instructions[changeindex] = 'jnz ' + instarr[1] + " " + instarr[2]
    except:
        pass
    instindex += 1
    # print(instructions)
    # print(regs)

print(regs['a'])