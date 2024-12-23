import sys
from collections import defaultdict

class lan:
    def __init__(self):
        self.computers = []

    def addcomputer(self, computer, pairs):

        addcomputer = True
        for c in self.computers:
            if c not in pairs[computer]:
                addcomputer = False
                break
        if addcomputer:
            self.computers.append(computer)

    def getcomputers(self):
        self.computers.sort()
        return ",".join(self.computers)
    

pairs = defaultdict(list)

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (l,r) = line.split("-")
        pairs[l].append(r)
        pairs[r].append(l)

largestlan = ""

for primarycomputer in pairs:
    l = lan()
    l.addcomputer(primarycomputer, pairs)
    for comp in pairs:
        l.addcomputer(comp, pairs)
    lanstr = l.getcomputers()
    if len(lanstr) > len(largestlan):
        largestlan = lanstr

print(largestlan)