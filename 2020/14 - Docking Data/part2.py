import sys

lines = []

with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line.rstrip())

mem = {}

def getaddrs(mask, val):
    newmask = mask.copy()
    for i in range(0, len(mask)):
        if mask[i] == "X":
            newmask[i] = "0"
            getaddrs(newmask, val)
            newmask[i] = "1"
            getaddrs(newmask, val)
            return()
        else:
            newmask[i] = mask[i]
    # print(str(int(int("".join(newmask), 2))), ":  ", end="")
    mem[int(int("".join(newmask), 2))] = val
    # print("".join(newmask))

    # print(newmask)


mask = []
address = []
for line in lines:
    if line.startswith("mask"):
        _, mask = line.split(" = ")
        mask = [c for c in mask]
        # print()
        # print("mask: ", end="")
        # print("".join(mask))

    else:
        memaddr, val = line.split("] = ")
        _, memaddr = memaddr.split("[")
        memaddr = int(memaddr)
        val = int(val)
        address = [i for i in bin(memaddr)[2:]]
        while len(address) < len(mask):
            address.insert(0, '0')
        for i in range(0, len(address)):
            if mask[i] == "1":
                address[i] = "1"
            if mask[i] == 'X':
                address[i] = 'X'
        # print("addr: ", end="")
        # print("".join(address))
        # print()
        getaddrs(address, val)

# print(mem)

total = 0

for v in mem.values():
    total += v

print(total)