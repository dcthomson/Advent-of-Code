from ensurepip import version
import sys

hexstr = ""
binstr = ""

with open(sys.argv[1], "r") as f:
    for line in f:
        hexstr = line.rstrip()
        h_size = len(hexstr) * 4
        binstr = ( bin(int(hexstr, 16))[2:] ).zfill(h_size)

print(binstr)

versiontotal = 0

def parsepacket(binstr):
    
    global versiontotal

    pversion = binstr[0:3]
    typeid = binstr[3:6]
    binstr = binstr[3:]
    versiontotal += int(pversion, 2)


    ptype = binstr[0:3]
    binstr = binstr[3:]

    if int(ptype, 2) == 4:
        # literal value
        literal = ""
        while binstr[0] == "1":
            literal += binstr[1:5]
            binstr = binstr[5:]
        literal += binstr[1:5]
        binstr = binstr[5:]
        print("version:", int(pversion, 2))
        print("type ID:", int(typeid, 2))
        print("literal:", int(literal, 2))
        return binstr
    
    else:
        # not literal (has sub packets)
        subpackettype = int(binstr[0])
        binstr = binstr[1:]
        if not subpackettype:
            # 15 bit subpacket
            subpackettotal = binstr[0:15]
            parsepacket(binstr[15:])
        
        else:
            # 11 bit subpacket
            subpacketcount = binstr[0:11]
            binstr = binstr[11:]
            for i in range(0, 3):
                binstr = parsepacket(binstr)


parsepacket(binstr)

print(versiontotal)