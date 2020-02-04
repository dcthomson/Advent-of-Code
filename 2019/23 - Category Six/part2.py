import sys
import OpcodeComputer

line = ""
with open(sys.argv[1]) as f:
    line = f.readline()

natx = None
naty = None
lasty = None

def idle(n):
    for i in n:
        if i.input:
            return False
    return True

nics = []
for i in range(0, 50):
    nics.append(OpcodeComputer.Opcode(line, i))

for i in range(0, 50):
    addr = nics[i].runOpcode([i])

while True:
    for i in range(0, 50):
        if nics[i].input:
            while nics[i].input:
                nics[i].runOpcode()
        else:
            nics[i].runOpcode(-1)
        while len(nics[i].packet) >= 3:
            addr = nics[i].packet.pop(0)
            x = nics[i].packet.pop(0)
            y = nics[i].packet.pop(0)
            if addr == 255:
                natx = x
                naty = y
            else:
                nics[addr].receivePacket([x, y])
    if idle(nics):
        if lasty is not None:
            if lasty == naty:
                print(naty)
                exit()
        lasty = naty
        if natx is not None and naty is not None:
            nics[0].receivePacket([natx, naty])