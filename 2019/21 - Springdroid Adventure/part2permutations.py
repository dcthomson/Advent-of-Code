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
registers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "T", "J"]
end = "RUN\n"

perm = permutations(registers, 2)
regpairs = []
for i in list(perm):
    if i[1] == "T" or i[1] == "J":
        regpairs.append(i)

commands = []
for i in instructions:
    for rp in regpairs:
        commands.append(i + " " + rp[0] + " " + rp[1] + "\n")

commandnum = 1

for c in commands:
    inpoot += getascii(c)

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

Q = commands.copy()

intcode = OpcodeComputer.Opcode(line)

while True:
    c = Q.pop(0)

    inpoot = getascii(c)
    inpoot += getascii(end)

    intcode.reset()

    inputted = False
    while True:
        if not inputted:
            ascii = intcode.runOpcode(inpoot)
            inputted = True
        else:
            ascii = intcode.runOpcode()


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
                print(c)
                print(ascii)
                exit()

    for nextc in commands:
        Q.append(c + nextc)