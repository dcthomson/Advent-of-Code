import sys

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

while True:
    period = file = None
    length = len(disk)
    for l, i in enumerate(disk):
        r = length - l - 1
        if period is None and disk[l] == ".":
            period = l
        if file is None and disk[r] != ".":
            file = r
        if period is not None and file is not None:
            break
    if period < file:
        disk[period] = disk[file]
        disk[file] = "."
    else:
        break

total = 0
for n, i in enumerate(disk):
    if i != ".":
        total += i * n
print(total)