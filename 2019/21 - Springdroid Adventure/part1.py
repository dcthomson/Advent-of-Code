import sys
import os
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

instructions = []
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "instructions1.txt")) as w:
    for line in w:
        instructions.append(line)

inpoot = []
for instruction in instructions:
    inpoot += getascii(instruction)

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line)

inputted = False
while intcode.done == False:
    if not inputted:
        ascii = intcode.runOpcode(inpoot)
        inputted = True
    else:
        ascii = intcode.runOpcode()

    try:
        if ascii == 10:
            print()  # uncomment for output
        else:
            if 0 <= ascii <= 127: 
                print(str(chr(ascii)), end="") # uncomment for output
                pass        
            else:
                print(ascii)
    except:
        break