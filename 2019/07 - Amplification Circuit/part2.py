import sys
from itertools import permutations
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

phasesettings = [5,6,7,8,9]

largestsignal = None

for i in permutations(phasesettings):
    inpoot = 0
    A = OpcodeComputer.Opcode(line)
    B = OpcodeComputer.Opcode(line)
    C = OpcodeComputer.Opcode(line)
    D = OpcodeComputer.Opcode(line)
    E = OpcodeComputer.Opcode(line)
    
    
    inpoot = opcode.runOpcode([i[0], inpoot])
    inpoot = opcode.runOpcode([i[1], inpoot])
    inpoot = opcode.runOpcode([i[2], inpoot])
    inpoot = opcode.runOpcode([i[3], inpoot])
    signal = opcode.runOpcode([i[4], inpoot])
    if largestsignal is None:
        largestsignal = signal
    elif signal > largestsignal:
        largestsignal = signal

print(largestsignal)