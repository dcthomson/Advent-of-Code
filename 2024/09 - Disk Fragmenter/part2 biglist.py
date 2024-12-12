import sys
import time

disk = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        id = 0
        s = ""
        for i, c in enumerate(line):
            if not i % 2:
                for j in range(0, int(c)):
                    disk.append(id)
                id += 1
            else:
                for j in range(0, int(c)):
                    disk.append(".")

moved = []
numindexes = []
numid = False
for i in range(len(disk) - 1, 0, -1):
    if disk[i] != ".":
        if not numid or numid == disk[i]:
            numid = disk[i]
            numindexes.append(i)
        if numid in moved:
            numid = False
            numindexes = []
            continue
        if numid and disk[i - 1] != numid:
            spacelength = 0
            spacestart = False
            for j in range(0, len(disk)):
                if j >= i:
                    break
                if disk[j] == ".":
                    if not spacestart:
                        spacestart = j
                        spacelength = 1
                    else:
                        spacelength += 1
                else:
                    # end of space
                    if spacestart and spacelength >= len(numindexes):
                        for n, k in enumerate(numindexes):
                            disk[spacestart + n] = numid
                            disk[k] = "."
                        spacestart = False  
                        moved.append(numid)
                        break
                    spacestart = False
            numid = False
            numindexes = []              

total = 0
for n, i in enumerate(disk):
    if i != ".":
        total += i * n
print(total)