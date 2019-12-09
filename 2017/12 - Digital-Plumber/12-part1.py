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

linked = getPipes(0, progs, linked)
print(len(linked))