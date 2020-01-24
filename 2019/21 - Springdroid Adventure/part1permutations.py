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

    return retarr

inpoot = []

intcode = None

instructions = ["NOT", "AND", "OR"]
registers = ["C", "T", "A", "D", "B", "J"]
end = "WALK\n"

perm = permutations(registers, 2)
regpairs = []
for i in list(perm):
    if i[1] == "T" or i[1] == "J":
        regpairs.append(i)

commands = []
for i in instructions:
    for rp in regpairs:
        commands.append(i + " " + rp[0] + " " + rp[1] + "\n")

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line)

Q = commands.copy()

while True:
    c = Q.pop(0)

    print(c, end='')
    inpoot = getascii(c)
    inpoot += getascii(end)

    intcode.reset()

    print()

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
                print(ascii)
                exit()

    for nextc in commands:
        Q.append(c + nextc)