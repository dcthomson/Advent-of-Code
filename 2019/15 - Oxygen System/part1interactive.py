import sys
import os
import OpcodeComputer

class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line)

map = {}
current = (0,0)
map[current] = "."

while True:
    dir = getch()
    print(dir)
    if dir == b'w':
        dir = 1
    elif dir == b'a':
        dir = 3
    elif dir == b's':
        dir = 2
    elif dir == b'd':
        dir = 4
    if dir in (1,2,3,4):
        out = intcode.runOpcode(dir)
        
        if out == 0:
            if dir == 1:
                map[current[0], current[1] - 1] = '#'
            elif dir == 2:
                map[current[0], current[1] + 1] = '#'
            elif dir == 3:
                map[current[0] - 1, current[1]] = '#'
            elif dir == 4:
                map[current[0] + 1, current[1]] = '#'
        elif out == 1 or out == 2:
            if dir == 1:
                current = (current[0], current[1] - 1)
            elif dir == 2:
                current = (current[0], current[1] + 1)
            elif dir == 3:
                current = (current[0] - 1, current[1])
            elif dir == 4:
                current = (current[0] + 1, current[1])
            if out == 1:
                map[current] = "."
            elif out == 2:
                map[current] = "O"
            

        print(out)

        os.system('cls||clear')
        line = False
        minx = miny = maxx = maxy = 0
        for k in map:
            x = k[0]
            y = k[1]
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                try:
                    if (x, y) == current:
                        print("D", end='')
                    else:
                        print(map[(x,y)], end='')
                except:
                    print(" ", end='')
            print()


