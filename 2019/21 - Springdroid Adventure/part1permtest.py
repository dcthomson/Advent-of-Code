import sys
import os
from itertools import permutations
import OpcodeComputer

def getascii(s):
    retarr = []
    commands = s.split(",")
    for i in commands:
        if len(retarr):
            retarr.append(44)
        for c in i:
            retarr.append(ord(c))
    # retarr.append(10)
    return retarr

# instructions = []
# with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "instructions2.txt")) as w:
#     for line in w:
#         instructions.append(line)


inpoot = []
# for instruction in instructions:
#     inpoot += getascii(instruction)

# print(inpoot)

intcode = None

instructions = ["NOT", "AND", "OR"]
reg1 = ["A", "B", "C", "D", "T", "J"]
reg2 = ["T", "J"]
end = "WALK\n"
commandend = getascii(end)

commands = []
for i in instructions:
    for r1 in reg1:
        for r2 in reg2:
            if r1 != r2:
                s = i + " " + r1 + " " + r2 + "\n"
                commands.append(getascii(s))

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

Q = []
for i in range(0, len(commands)):
    Q.append([i])

intcode = OpcodeComputer.Opcode(line)

while True:
    # print(Q)
    c = Q.pop(0)

    inpoot = []

    for i in c:        
        inpoot += commands[i]
    inpoot += commandend

    # print("inpoot:", inpoot)

    intcode.reset()

    inputted = False
    while True:
        if not inputted:
            ascii = intcode.runOpcode(inpoot)
            inputted = True
        else:
            ascii = intcode.runOpcode()

        # print(chr(ascii))

        if ascii == 10:
            # print()  # uncomment for output
            pass
        else:
            if 0 <= ascii <= 127: 
                # print(str(chr(ascii)), end="") # uncomment for output
                if str(chr(ascii)) == "D":
                    break
                pass
            else:
                print(inpoot)
                print(ascii)
                exit()

    for i in range(0, len(commands)):
        Q.append(c + [i])