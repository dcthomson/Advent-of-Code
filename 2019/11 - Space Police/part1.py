import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer
from itertools import cycle

with open(sys.argv[1]) as f:
    line = f.readline()

    opcode = OpcodeComputer.Opcode(line)

    painting = {}
    #         N      E      S        W
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]


    x = 0
    y = 0
    direction = 0

    count = 0

    while True:
        # print("running")
        if not (x, y) in painting:
            painting[(x, y)] = 'B'
            count += 1
        if painting[(x, y)] == 'B':
            paint = opcode.runOpcode(0)
            if opcode.checkifdone():
                break
            turn = opcode.runOpcode()
            if opcode.checkifdone():
                break
        else:
            paint = opcode.runOpcode(1)
            if opcode.checkifdone():
                break
            turn = opcode.runOpcode()
            if opcode.checkifdone():
                break
        if paint == 0:
            painting[(x, y)] = 'B'
        else:
            painting[(x, y)] = 'W'
        if turn == 0:
            # LEFT
            try:
                direction -= 1
                dirs[direction]
            except:
                direction = 3
        else:
            # RIGHT
            try:
                direction += 1
                dirs[direction]
            except:
                direction = 0
        # MOVE
        x += dirs[direction][0]
        y += dirs[direction][1]

    print(count)