import sys
import os.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import OpcodeComputer

def str2asciinum(s):
    retarr = []
    commands = s.split(",")
    for i in commands:
        if len(retarr):
            retarr.append(44)
        for c in i:
            retarr.append(ord(c))
    return retarr

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line)

while intcode.done == False:

    ascii = intcode.runOpcode()

    try:
        if ascii == 10:
            print()
        else:
            if 0 <= ascii <= 127: 
                print(str(chr(ascii)), end="")
                pass        
            else:
                print(ascii)
    except:
        break