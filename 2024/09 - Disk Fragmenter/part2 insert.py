import sys
import time

disk = []

class File:
    def __init__(self, size, id=False):
        self.id = id
        self.size = size
        self.processed = False

    def __repr__(self):
        if id:
            return str(self.id) * self.size
        else:
            return "." * self.size

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        id = 0
        s = ""
        for i, c in enumerate(line):
            if not i % 2:
                disk.append(File(int(c), id))
                id += 1
            else:
                disk.append(File(int(c)))



fid = 1
sid = 0
while fid > sid:
    for f in reversed(disk):
        if f.id and not f.processed:
            fid = f.id
            f.processed = True
            break

    for f in disk:
        if not f.id:
            if f.size >= disk[fid].size:
                sid = f.id
                break
    if fid > sid:
        if disk[fid].size == disk[sid].size:
            disk[sid].id = disk[fid].id
            disk[fid].id = False
        elif disk[fid].size > disk[sid].size:
            disk[sid].size -= disk[fid].size
            disk.insert(sid, disk[fid])
            disk[fid].id = False
    print(fid, sid)
    print(disk)
    time.sleep(5)


    # period = file = None
    # length = len(disk)
    # for l, i in enumerate(disk):
    #     r = length - l - 1
    #     if period is None and disk[l] == ".":
    #         period = l
    #     if file is None and disk[r] != ".":
    #         file = r
    #     if period is not None and file is not None:
    #         break
    # if period < file:
    #     disk[period] = disk[file]
    #     disk[file] = "."
    # else:
    #     break

total = 0
for n, i in enumerate(disk):
    if i != ".":
        total += i * n
print(total)