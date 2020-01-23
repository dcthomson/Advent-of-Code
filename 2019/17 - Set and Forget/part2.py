import sys
import os
import OpcodeComputer
import time

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line, "map", {0: 2})

def getascii(s):
    retarr = []
    commands = s.split(",")
    for i in commands:
        if len(retarr):
            retarr.append(44)
        for c in i:
            retarr.append(ord(c))
    retarr.append(10)
    return retarr
        

mmr = getascii("A,B,A,B,A,C,B,C,A,C")
A = getascii("R,4,L,10,L,10")
B = getascii("L,8,R,12,R,10,R,4")
C = getascii("L,8,L,8,R,10,R,4")

# [65, 44, 66, 44, 65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 65, 44, 67, 10]
# [82, 44, 52, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
# [76, 44, 56, 44, 82, 44, 49, 50, 44, 82, 44, 49, 48, 44, 82, 44, 52, 10]
# [76, 44, 56, 44, 76, 44, 56, 44, 82, 44, 49, 48, 44, 82, 44, 52, 10]

inpoot = mmr + A + B + C

inpoot += [110, 10]

map = {}

x = 0
y = 0
inputted = False
while intcode.done == False:
    if not inputted:
        ascii = intcode.runOpcode(inpoot)
        inputted = True
    else:
        ascii = intcode.runOpcode()

    try:
        if ascii == 10:
            x = 0
            y += 1
            # print()  # uncomment for output
        else:
            map[(x, y)] = str(chr(ascii))
            x += 1
            if 0 <= ascii <= 127: 
                # print(str(chr(ascii)), end="") # uncomment for output
                pass        
            else:
                print(ascii)
    except:
        break