import sys
import string

with open(sys.argv[1], 'r') as f:
    for line in f:
        instructions = line.strip().split(",")

danceline = list(string.ascii_lowercase)
danceline = danceline[0:16]

for inst in instructions:
    if inst.startswith("s"):
        # spin
        i = int(inst.lstrip("s"))
        danceline = danceline[-i:] + danceline[:-i]
    elif inst.startswith("x"):
        # exchange
        inst = inst.lstrip("x")
        (i,j) = [int(x) for x in inst.split("/")]
        temp = danceline[i]
        danceline[i] = danceline[j]
        danceline[j] = temp
    elif inst.startswith("p"):
        # partner
        inst = inst.split("p", 1)[1]
        (i, j) = inst.split("/")
        i = danceline.index(i)
        j = danceline.index(j)
        temp = danceline[i]
        danceline[i] = danceline[j]
        danceline[j] = temp

print(''.join(danceline))