import sys
import os

import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

game = {}

def printgame(game, score):
    os.system('cls||clear')
    currenty = None
    for k, v in sorted(game.items()):
        if currenty is not None:
            if currenty != k[0]:
                print()
        currenty = k[0]
        tile = ""
        if v == 0:
            tile = " "
        elif v == 1:
            tile = "W"
        elif v == 2:
            tile = "#"
        elif v == 3:
            tile = "_"
        elif v == 4:
            tile = "O"
        print(tile, end="")
    print("\nscore: ", score)

line = ""

def getbally(game):
    for k, v in game.items():
        if v == 4:
            return k[1]
    return False

def getpaddley(game):
    for k, v in game.items():
        if v == 3:
            return k[1]
    return False

with open(sys.argv[1]) as f:
    line = f.readline()

# set mem address 0 to 2 so we can play for free
opcode = OpcodeComputer.Opcode(line, "game", {0 : 2})

coord = []

score = 0

while True:
    bally = False
    paddley = False
    if len(coord) == 3:
        if coord[0] == -1 and coord[1] == 0:
            score = coord[2]
        game[(coord[1], coord[0])] = coord[2]
        coord = []
        # uncomment next 2 lines to show game
        printgame(game, score)
        print("\n")
        bally = getbally(game)
        paddley = getpaddley(game)

    if bally and paddley:
        if paddley == bally:
            coord.append(opcode.runOpcode(0))
        elif paddley > bally:
            coord.append(opcode.runOpcode(-1))
        elif paddley < bally:
            coord.append(opcode.runOpcode(1))
    else:
        coord.append(opcode.runOpcode())

    if opcode.checkifdone():
        break

print(score)