import sys
import os
import OpcodeComputer

intcode = None

with open(sys.argv[1]) as f:
    line = f.readline()
    intcode = OpcodeComputer.Opcode(line, "map", {0: 2})

def getascii(s):
    retarr = []
    commands = s.split(",")
    for i in commands:
        if len(retarr):
            retarr.append(44)
        for c in i:
            retarr.append(ord(c))
    retarr.append(10)
    return retarr
        

mmr = getascii("A,B,A,B,A,C,B,C,A,C")
A = getascii("R,4,L,10,L,10")
B = getascii("L,8,R,12,R,10,R,4")
C = getascii("L,8,L,8,R,10,R,4")

print(mmr)
print(A)
print(B)
print(C)

# [65, 44, 66, 44, 65, 44, 66, 44, 65, 44, 67, 44, 66, 44, 67, 44, 65, 44, 67, 10]
# [82, 44, 52, 44, 76, 44, 49, 48, 44, 76, 44, 49, 48, 10]
# [76, 44, 56, 44, 82, 44, 49, 50, 44, 82, 44, 49, 48, 44, 82, 44, 52, 10]
# [76, 44, 56, 44, 76, 44, 56, 44, 82, 44, 49, 48, 44, 82, 44, 52, 10]


inpoot = mmr + A + B + C

print(inpoot)

map = {}

x = 0
y = 0
inputted = False
while intcode.done == False:
    if not inputted:
        ascii = intcode.runOpcode(inpoot)
        inputted = True
    else:
        ascii = intcode.runOpcode()
    try:
        if ascii == 10:
            # os.system('cls||clear')
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