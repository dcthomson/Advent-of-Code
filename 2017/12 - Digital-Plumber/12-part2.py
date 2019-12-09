import sys

progs = list()

def getPipes(index, progs, linked):
    for i in progs[index]:
        i = int(i)
        if i not in linked:
            linked[i] = 1
            linked = getPipes(i, progs, linked)
    return linked

linked = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip().split(" <-> ")[1]
        progs.append(line.split(", "))

index = 0
groups = 0
while True:
    linked = getPipes(index, progs, linked)
    groups += 1
    i = 0
    notfound = True
    while i < len(progs):
        if i not in linked:
            index = i
            notfound = False
            break
        i += 1
    if notfound:
        break
print(groups)

