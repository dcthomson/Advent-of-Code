import sys
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()
    opcode = OpcodeComputer.Opcode(line)
    
    diagnosticcode = 0
    while diagnosticcode == 0:
        diagnosticcode = opcode.runOpcode(1)
    print(diagnosticcode)