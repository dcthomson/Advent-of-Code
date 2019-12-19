import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

with open(sys.argv[1]) as f:
    line = f.readline()

    sleighsize = 100
    sleighoffset = sleighsize - 1

    count = 0

    lowestx = 0

    # opcode = OpcodeComputer.Opcode(line)
    y = 10 # start at 10 to skip those first few lines that don't get hit by beam
    while True:
        x = lowestx
        while True:
            if OpcodeComputer.Opcode(line).runOpcode([x, y]):
                # print("F", x, y)
                lowestx = x
                # if OpcodeComputer.Opcode(line).runOpcode([x + sleighoffset, y]):
                if y - (sleighsize - 1) >= 0:
                    if OpcodeComputer.Opcode(line).runOpcode([x + sleighoffset, y - sleighoffset]):
                        print(x * 10000 + (y - sleighoffset))
                        exit()
                break
            x += 1
        y += 1