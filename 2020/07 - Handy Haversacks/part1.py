import sys

class Bag:
    def __init__(self, s):
        s = s.strip()
        if s.endswith("."):
            s = s[:-1]
        s = s.replace(" bags", "")
        s = s.replace(" bag", "")
        name, contents = s.split(" contain ")
        self.name = name
        if contents == "no other":
            self.contents = False
        else:
            self.contents = {}
            bags = contents.split(", ")
            for bag in bags:
                num, name = bag.split(" ", 1)
                self.contents[name] = num

    def isin(self, b):
        if self.contents:
            if b in self.contents:
                return True
        return False

    def __str__(self):
        retstr = self.name + "\n"
        if self.contents:
            for b in self.contents:
                retstr += "  " + b + ": " + self.contents[b] + "\n"
        return retstr

bags = []

with open(sys.argv[1], "r") as f:
    for line in f:
        bags.append(Bag(line))

bagstofind = ["shiny gold"]
found = {}

while bagstofind:
    tofind = bagstofind.pop(0)
    found[tofind] = 1
    for bag in bags:
        if bag.isin(tofind):
            if not bag.name in found:
                bagstofind.append(bag.name)

print(len(found) - 1)