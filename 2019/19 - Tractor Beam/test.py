import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()

    sleighsize = 100
    sleighoffset = sleighsize - 1

    x = 929
    y = 911

    print(OpcodeComputer.Opcode(line).runOpcode([x, y]))
    print(OpcodeComputer.Opcode(line).runOpcode([x + sleighoffset, y]))    
    print(OpcodeComputer.Opcode(line).runOpcode([x + sleighoffset, y - (sleighoffset)]))
