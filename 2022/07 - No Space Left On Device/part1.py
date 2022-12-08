import sys

class Directory:
    def __init__(self, name, parentindex):
        self.name = name
        self.size = 0
        self.parent = parentindex
        self.items = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

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