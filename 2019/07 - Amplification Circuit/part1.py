import sys
from itertools import permutations
import OpcodeComputer

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

phasesettings = [0,1,2,3,4]

largestsignal = None

for i in permutations(phasesettings):
    inpoot = 0
    opcode = OpcodeComputer.Opcode(line)
    inpoot = opcode.runOpcode([i[0], inpoot])
    opcode = OpcodeComputer.Opcode(line)
    inpoot = opcode.runOpcode([i[1], inpoot])
    opcode = OpcodeComputer.Opcode(line)
    inpoot = opcode.runOpcode([i[2], inpoot])
    opcode = OpcodeComputer.Opcode(line)
    inpoot = opcode.runOpcode([i[3], inpoot])
    opcode = OpcodeComputer.Opcode(line)
    signal = opcode.runOpcode([i[4], inpoot])
    if largestsignal is None:
        largestsignal = signal
    elif signal > largestsignal:
        largestsignal = signal

print(largestsignal)