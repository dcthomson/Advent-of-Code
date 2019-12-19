import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()

    count = 0

    # opcode = OpcodeComputer.Opcode(line)
    for y in range(0, 50):
        for x in range(0, 50):
            if OpcodeComputer.Opcode(line).runOpcode([x, y]):
                print("#", end="")
                count += 1
            else:
                print(".", end="")
        print()
    print(count)