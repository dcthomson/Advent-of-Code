import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()
    opcode = OpcodeComputer.Opcode(line)
    for noun in range(0, 100):
        for verb in range(0, 100):
            opcode.setInput(line, {1: noun, 2: verb})
            if opcode.runOpcode()[0] == 19690720:
                print(100 * noun + verb)
                exit()