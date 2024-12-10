import sys
import time

disk = []

maxid = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        id = 0
        s = ""
        for i, c in enumerate(line):
            if not i % 2:
                for j in range(0, int(c)):
                    disk.append(id)
                    maxid = id
                id += 1
            else:
                for j in range(0, int(c)):
                    disk.append(".")

moved = {}

def getfile(id):
    indexes = []
    for n, i in enumerate(disk):
        if i == id:
            indexes.append(n)
    return indexes

def getspace(size):
    indexes = []
    for n, i in enumerate(disk):
        found = True
        if i == ".":
            for k in range(0, size):
                try:
                    if disk[n + k] != ".":
                        found = False
                        break
                except:
                    pass
            if found:
                for k in range(0, size):
                    indexes.append(n + k)
                break
    return indexes

def swap(disk, file, space):
    if file[0] > space[0]:
        for n, i in enumerate(file):
            disk[space[n]] = disk[file[n]]
            disk[file[n]] = "."

for i in range(maxid, 0, -1):
    file = getfile(i)
    filesize = len(file)
    space = getspace(filesize)

    swap(disk, file, space)
    # for i in disk:
    #     print(str(i), end="")
    # print()

total = 0
for n, i in enumerate(disk):
    if i != ".":
        total += i * n
print(total)