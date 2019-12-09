import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()
    replacements = {1: 12, 2: 2}
    opcode = OpcodeComputer.Opcode(line, replacements)
    print(opcode.runOpcode()[0])