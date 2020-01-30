import sys
import OpcodeComputer

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()
    
nics = []
nextpacket = []
hasinput = []
for i in range(0, 50):
    nics.append(OpcodeComputer.Opcode(line, i))
    nextpacket.append(-1)

def sendcode(nics, addr, x=None, y=None):
    print(addr, x, y)
    if addr == 255:
        print(y)
        exit()
    if addr not in initialized:
        newaddr = nics[addr].runOpcode(addr)
        newx = nics[addr].runOpcode(-1)
        newy = nics[addr].runOpcode(-1)
        initialized.append(addr)
        sendcode(nics, newaddr, newx, newy)
    if x is not None and y is not None:
        newaddr = nics[addr].runOpcode([addr, x, y])
        newx = nics[addr].runOpcode()
        newy = nics[addr].runOpcode()
        sendcode(nics, newaddr, newx, newy)

while True:
    for i in range(0, 50):
        addr = nics[i].runOpcode([i])
        x = nics[i].runOpcode()
        y = nics[i].runOpcode()
        print(i, addr, x, y)
        nics[addr].receivePacket([x, y])
        # sendcode(nics, addr, x, y)