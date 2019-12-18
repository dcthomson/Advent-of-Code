import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

game = {}

with open(sys.argv[1]) as f:
    line = f.readline()

    opcode = OpcodeComputer.Opcode(line)

    coord = []

    while True:
        if len(coord) == 3:
            game[(coord[0], coord[1])] = coord[2]
            coord = []
        coord.append(opcode.runOpcode())
        if opcode.checkifdone():
            break
    count = 0
    for k, v in game.items():
        if v == 2:
            count += 1
    print(count)