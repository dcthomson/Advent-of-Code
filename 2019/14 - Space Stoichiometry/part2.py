import sys

chemicals = {}
ore = 1000000000000

class Chemical:
    def __init__(self, name, num, chems):
        self.name = name
        self.count = 0
        self.producenum = int(num)
        self.chems = chems

    def __str__(self):
        ret = str(self.producenum) + " " + self.name
        ret += ": " + str(self.count) + "\n  "
        for k, v in self.chems.items():
            ret += str(v) + " " + k + "  "
        return ret

    def make(self, num):
        global ore
        for ingredientname, ingredientnum in self.chems.items():
            while chemicals[ingredientname].count < ingredientnum:
                if ingredientname == "ORE":
                    ore -= ingredientnum
                    break
                else:
                    chemicals[ingredientname].make(ingredientnum)
            if ingredientname != "ORE":
                chemicals[ingredientname].count -= ingredientnum
        self.count += self.producenum
    

with open(sys.argv[1]) as f:
    chemicals["ORE"] = Chemical("ORE", 0, {})
    for line in f:
        line = line.rstrip()
        (left, right) = line.split(" => ")
        (num, name) = right.split()
        lefts = left.split(", ")
        chems = {}
        for l in lefts:
            (lnum, lname) = l.split()
            chems[lname] = int(lnum)
        chemicals[name] = Chemical(name, int(num), chems)

fuelcount = 0
while ore > 0:
    chemicals["FUEL"].make(1)
    fuelcount += 1
    allzero = True
    for k, v in chemicals.items():
        # print(k + ":", v.count)
        if k != "ORE" and k != "FUEL":
            if v.count != 0:
                allzero = False
                break
    if allzero:
        print(fuelcount, ":", ore)


print(fuelcount)