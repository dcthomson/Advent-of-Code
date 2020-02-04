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


for i in range(0, 50):
    addr = nics[i].runOpcode([i])
    if len(nics[i].packet) >= 3:
        addr = nics[i].packet.pop(0)
        x = nics[i].packet.pop(0)
        y = nics[i].packet.pop(0)
        if addr == 255:
            print(y)
            exit()
        # print(i, addr, x, y)
        nics[addr].receivePacket([x, y])
while True:
    for i in range(0, 50):
        if nics[i].input:
            nics[i].runOpcode()
        else:
            nics[i].runOpcode(-1)
        if len(nics[i].packet) >= 3:
            addr = nics[i].packet.pop(0)
            x = nics[i].packet.pop(0)
            y = nics[i].packet.pop(0)
            if addr == 255:
                print(y)
                exit()
            # print(i, addr, x, y)
            nics[addr].receivePacket([x, y])