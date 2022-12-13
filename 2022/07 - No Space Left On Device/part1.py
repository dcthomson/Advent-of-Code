import sys

did = 0

directories = {}
files = {}

class Directory:
    def __init__(self, name, parentindex=None):
        self.name = name
        self.did = did
        did += 1
        self.parent = parentindex
        self.size = 0
        self.items = []

    def getsize(self):
        for i in self.items:
            self.size += i.getsize()

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getsize(self):
        return self.size

with open(sys.argv[1], "r") as f:

    cwd = ""

    directories = []
    files = []

    directories["/"] = Directory("/")

    for line in f:
        line = line.rstrip()

        if line.startswith("$ cd"):
            (_,_,newdir) = line.split()
            if newdir == "/":
                cwd = "/"
            elif newdir == "..":
                cwd = directories[cwd].parent
            else:
                directories["newdir"] = Directory("newdir")
                directories["newdir"].parent = cwd
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):