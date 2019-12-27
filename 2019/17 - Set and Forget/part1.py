import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line)

map = {}

x = 0
y = 0
while intcode.done == False:
    ascii = intcode.runOpcode()
    try:
        if ascii == 10:
            x = 0
            y += 1
            print()
        else:
            map[(x, y)] = str(chr(ascii))
            x += 1
            print(str(chr(ascii)), end="")
    except:
        break

intersectionsum = 0

for k, v in map.items():
    try:
        if (v == "#" and
            map[(k[0] - 1, k[1])] == "#" and
            map[(k[0] + 1, k[1])] == "#" and
            map[(k[0], k[1] + 1)] == "#" and
            map[(k[0], k[1] - 1)] == "#"):
            # found intersection
            intersectionsum += k[0] * k[1]
    except:
        pass

print(intersectionsum)