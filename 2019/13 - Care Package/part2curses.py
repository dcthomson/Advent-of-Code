import sys
import os
import curses
import time
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


def main(stdscr):
    curses.curs_set(0)
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
                stdscr.addstr(0, 13, "Score: " + str(score))
            else:
                game[(coord[1], coord[0])] = coord[2]

                tile = ""
                if coord[2] == 0:
                    tile = " "
                elif coord[2] == 1:
                    tile = u"\u2588"
                elif coord[2] == 2:
                    tile = "#"
                elif coord[2] == 3:
                    tile = u"\u1397"
                elif coord[2] == 4:
                    tile = "O"
                stdscr.addstr(coord[1] + 1, coord[0], tile)
                stdscr.refresh()
            coord = []
            # uncomment next 2 lines to show game
            # printgame(game, score)
            # print("\n")
            bally = getbally(game)
            paddley = getpaddley(game)

        if bally and paddley:
            time.sleep(0.05)
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

curses.wrapper(main)