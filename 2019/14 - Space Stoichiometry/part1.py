import sys

class Chemical:
    def __init__(self, name, num, chems):
        self.name = name
        self.count = 0
        self.num = num
        self.chems = chems

    def __str__(self):
        ret = self.num + " " + self.name
        ret += ":\n  "
        for k, v in self.chems.items():
            ret += v + " " + k + "  "
        return ret

    def make(self, num):
        


        

chemicals = {}

with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        (left, right) = line.split(" => ")
        (num, name) = right.split()
        lefts = left.split(", ")
        chems = {}
        for l in lefts:
            (lnum, lname) = l.split()
            chems[lname] = lnum
        chemicals[name] = Chemical(name, num, chems)



for k, v in chemicals.items():
    print(v)

# names.sort()

# for i in names:
#     print(i)
