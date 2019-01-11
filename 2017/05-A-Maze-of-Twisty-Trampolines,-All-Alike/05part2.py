import sys

f = open(sys.argv[1])

inst = list()

for line in f:
    inst.append(int(line.strip()))

index = 0
steps = 0 
while True:
    try:
        newindex = index + inst[index]
        if inst[index] >= 3:
            inst[index] -= 1
        else:
            inst[index] += 1
        index = newindex
        steps += 1
    except IndexError:
        break
print(steps)
