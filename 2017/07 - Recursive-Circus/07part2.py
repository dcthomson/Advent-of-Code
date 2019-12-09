import sys

class Program:

    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.children = list()
        self.parent = False

    def setParent(self, p):
        self.parent = p

    def addChild(self, c):
        if c not in self.children:
            self.children.append(c)

    def getTotal(self):
        total = self.num
        for c in self.children:
            total += c.num
#        print(total)
        return total

    def checkChildren(self):
        num = False
        ret = True
#        print()
        for c in self.children:
            if not num:
                num = c.getTotal()
            else:
                if c.getTotal() != num:
                    ret = False
#                    print(c.name, c.getTotal())

        return ret


lines = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        lines.append(line.strip())

#print(lines)

programs = dict()

for line in lines:
    if "->" in line:
        line = line.split(" -> ")[0]
    (pname, num) = line.split(" ")
    num = int(num.rstrip(")").lstrip("("))
    programs[pname] = Program(pname, num)

for line in lines:
    if "->" in line:
        (line, children) = line.strip().split(" -> ")
        p = line.split()[0]
        children = children.split(", ")
        for c in children:
            programs[p].addChild(programs[c])
            programs[c].setParent(programs[p])

for k in programs:
    if not programs[k].checkChildren():
        for c in programs[k].children:
            print(c.name, c.getTotal())
        print()