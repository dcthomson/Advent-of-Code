import sys

did = 0

directories = {}
files = {}

class Directory:
    def __init__(self, path, name):
        self.name = name
        self.size = 0
        self.dirs = []
        self.files = {}

    def getsize(self):
        for i in self.items:
            self.size += i.getsize()


with open(sys.argv[1], "r") as f:

    directories = {}
 
    directories["/"] = Directory("/", "/")

    cwd = "/"

    for line in f:
        line = line.rstrip()

        if line.startswith("$ cd"):
            (_,_,d) = line.split()
            if d == "/":
                cwd = "/"
            elif d == "..":
                dlist = cwd.split(" - ")
                dlist.pop()
                cwd = " - ".join(dlist)
            else:
                cwd += " - "
                cwd += d
                if cwd not in directories:
                    directories[cwd] = Directory(cwd, d)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            dirname = line.split()[1]
            dwd = cwd + " - "
            dwd += dirname
            directories[dwd] = Directory(dwd, dirname)
            directories[cwd].dirs.append(dwd)
        elif line[0].isdigit():
            (size, fname) = line.split()
            directories[cwd].files[fname] = int(size)

sum = 0

def getsize(d):
    global sum
    for dirs in directories[d].dirs:
        directories[d].size += getsize(dirs)
    
    for f in directories[d].files:
        directories[d].size += directories[d].files[f]

    if directories[d].size <= 100000:
        sum += directories[d].size

    return directories[d].size

totalsize = getsize("/")

freespace = 70000000 - totalsize

bestdir = None

for d in directories:
    if directories[d].size > 30000000 - freespace:
        if bestdir is None or directories[d].size < directories[bestdir].size:
            bestdir = d

print(directories[bestdir].size)