import sys
import OpcodeComputer

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()
    
nics = []
nextpacket = []
for i in range(0, 50):
    nics.append(OpcodeComputer.Opcode(line, i))
    nextpacket.append(-1)

def sendcode(nics, addr, x, y):
    newaddr = nics[addr].runOpcode(x)
    print(1)
    newx = nics[addr].runOpcode(y)
    print(2)
    newy = nics[addr].runOpcode()
    print(i, newaddr, newx, newy)
    sendcode(nics, newaddr, newx, newy)


for i in range(0, 50):
    addr = nics[i].runOpcode(i)
    x = nics[i].runOpcode()
    y = nics[i].runOpcode()
    print(i, addr, x, y)
    sendcode(nics, addr, x, y)

