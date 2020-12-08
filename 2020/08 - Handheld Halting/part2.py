import sys

class Instruction:
    def __init__(self, s):
        s = s.strip()
        self.instruction, self.num = s.split()
        self.num = int(self.num)
        self.ran = False

instructions = []

with open(sys.argv[1], "r") as f:
    for line in f:
        instructions.append(Instruction(line))

for inum in range(0, len(instructions)):
    p = 0
    accumulator = 0
    
    if instructions[inum].instruction == "nop":
        instructions[inum].instruction = "jmp"
    elif instructions[inum].instruction == "jmp":
        instructions[inum].instruction = "nop"
    else:
        continue

    for i in instructions:
        i.ran = False

    try:
        while instructions[p].ran is False:
            instructions[p].ran = True
            if instructions[p].instruction == "nop":
                p += 1
            elif instructions[p].instruction == "acc":
                accumulator += instructions[p].num
                p += 1
            elif instructions[p].instruction == "jmp":
                p += instructions[p].num
    except:
        print(accumulator)
        exit()
    else:
        if instructions[inum].instruction == "nop":
            instructions[inum].instruction = "jmp"
        elif instructions[inum].instruction == "jmp":
            instructions[inum].instruction = "nop"