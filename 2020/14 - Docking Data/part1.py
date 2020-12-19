import sys

lines = []

with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line.rstrip())

mem = {}

mask = []
for line in lines:
    if line.startswith("mask"):
        _, mask = line.split(" = ")
        mask = [c for c in mask]
    else:
        memaddr, val = line.split("] = ")
        _, memaddr = memaddr.split("[")
        memaddr = int(memaddr)
        val = int(val)
        mem[memaddr] = [i for i in bin(val)[2:]]
        while len(mem[memaddr]) < len(mask):
            mem[memaddr].insert(0, '0')
        for i in range(0, len(mem[memaddr])):
            if mask[i] != 'X':
                mem[memaddr][i] = mask[i]

sum = 0

for k in mem:
    s = ""
    sum += int(s.join(mem[k]), 2)

print(sum)