import sys

hexstr = ""
binstr = ""

with open(sys.argv[1], "r") as f:
    for line in f:
        hexstr = line.rstrip()
        binstr = '{0:b}'.format(int(hexstr, 16)) 

print(binstr)

pversion = binstr[0:3]
ptype = binstr[3:6]

print(pversion, ptype)