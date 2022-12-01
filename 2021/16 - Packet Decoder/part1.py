from ensurepip import version
import sys

hexstr = ""
binstr = ""

with open(sys.argv[1], "r") as f:
    for line in f:
        hexstr = line.rstrip()
        binstr = '{0:b}'.format(int(hexstr, 16)) 

print(binstr)

versiontotal = 0

def parsepacket(binstr):
    
    global versiontotal

    pversion = binstr[0:3]
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
        print("literal:", int(literal, 2))
    
    else:
        # not literal
        i = 0

parsepacket(binstr)

print(versiontotal)