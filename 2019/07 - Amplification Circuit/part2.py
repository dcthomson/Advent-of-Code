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

# for i in permutations(phasesettings):
#     inpoot = 0
#     A = OpcodeComputer.Opcode(line)
#     B = OpcodeComputer.Opcode(line)
#     C = OpcodeComputer.Opcode(line)
#     D = OpcodeComputer.Opcode(line)
#     E = OpcodeComputer.Opcode(line)
    
    
#     inpoot = opcode.runOpcode([i[0], inpoot])
#     inpoot = opcode.runOpcode([i[1], inpoot])
#     inpoot = opcode.runOpcode([i[2], inpoot])
#     inpoot = opcode.runOpcode([i[3], inpoot])
#     signal = opcode.runOpcode([i[4], inpoot])
#     if largestsignal is None:
#         largestsignal = signal
#     elif signal > largestsignal:
#         largestsignal = signal

# print(largestsignal)

A = OpcodeComputer.Opcode(line, "A")
B = OpcodeComputer.Opcode(line, "B")
C = OpcodeComputer.Opcode(line, "C")
D = OpcodeComputer.Opcode(line, "D")
E = OpcodeComputer.Opcode(line, "E")

final = ""

inpoot = E.runOpcode([9, D.runOpcode([8, C.runOpcode([7, B.runOpcode([6, A.runOpcode(5)])])])])
print("Past initial")
while not A.done and not B.done and not C.done and not D.done and not E.done:
    inpoot = A.runOpcode(inpoot)
    print("A",inpoot)
    inpoot = B.runOpcode(inpoot)
    print("B", inpoot)
    inpoot = C.runOpcode(inpoot)
    print("C", inpoot)
    inpoot = D.runOpcode(inpoot)
    print("D", inpoot)
    inpoot = E.runOpcode(inpoot)
    print("E", inpoot)

    try:
        inpoot[0]
    except:
        final = inpoot

    print("inpoot:", inpoot)
print(final)