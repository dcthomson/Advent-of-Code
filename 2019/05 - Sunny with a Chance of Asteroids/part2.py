import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()
    opcode = OpcodeComputer.Opcode(line)
    
    diagnosticcode = 0
    while diagnosticcode == 0:
        diagnosticcode = opcode.runOpcode(5)
    print(diagnosticcode)