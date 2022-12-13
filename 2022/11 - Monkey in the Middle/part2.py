import sys
import math

monkeys = []

class Monkey:
    def __init__(self, items, oper, opernum, divisby, t, f, monkeynum):
        self.inspectnum = 0
        self.num = monkeynum
        self.items = items
        self.oper = oper
        self.opernum = opernum
        self.divisby = divisby
        self.t = t
        self.f = f

    def __str__(self):
        retstr = "Monkey " + str(self.num) + "\n"
        retstr += "  Items:\n"
        for i in self.items:
            retstr += "    " + str(i) + "\n"
        return retstr

    def inspectnthrow(self):
#        print("Monkey ", self.num, ":", sep="")
        for i in self.items:
            # inspect
            self.inspectnum += 1
#            print("  Monkey inspects an item with a worry level of ", i, ".", sep="")
            if self.oper == "+":
#                print("    Worry level increases by ", self.opernum, end="", sep="")
                i += self.opernum
            elif self.oper == "*":
#                print("    Worry level is multiplied by ", i, end="", sep="")
                i *= self.opernum
            elif self.oper == "squared":
#                print("    Worry level is multiplied by itself", end="", sep="")
                i *= i
#            print(" to ", i, ".", sep="")

            # no damage worry level drop
#            i = i // 3
#            print("    Monkey gets bored with item. Worry level is divided by 3 to ", i, ".", sep="")
            
            # throw
#            print("    Current worry level is ", end="")
            if not i % self.divisby:
#                print("divisible by ", self.divisby, ".", sep="")
#                print("    Item with worry level ", i, " is thrown to monkey ", self.t, ".", sep="")
                monkeys[self.t].catch(i)
            else:
#                print("not divisible by ", self.divisby, ".", sep="")
#                print("    Item with worry level ", i, " is thrown to monkey ", self.f, ".", sep="")
                monkeys[self.f].catch(i)
            self.items = []

    def catch(self, wl):
        self.items.append(wl)

with open(sys.argv[1], "r") as f:

    monkey = 0
    items = []
    oper = ""
    opernum = 0
    divisby = 0
    divisbyfalse = 0
    divisbytrue = 0
    monkeynum = 0

    for line in f:
        line = line.strip()

        if line.startswith("Monkey"):
            monkey = int(line.split()[1].rstrip(":"))
            items = []

        elif line.startswith("Starting items:"):
            right = line.split("items: ")[1]
            cnums = right.split(", ")

            for cnum in cnums:
                items.append(int(cnum))
        
        elif line.startswith("Operation"):
            right = line.split("old ")[1]
            (oper, opernum) = right.split()
            if opernum == "old":
                oper = "squared"
                opernum = 0
            else:
                opernum = int(opernum)

        elif line.startswith("Test:"):
            divisby = int(line.split("by ")[1])

        elif line.startswith("If true"):
            divisbytrue = int(line.split("monkey ")[1])

        elif line.startswith("If false"):
            divisbyfalse = int(line.split("monkey ")[1])
            monkeys.append(Monkey(items, oper, opernum, divisby, divisbytrue, divisbyfalse, monkeynum))
            monkeynum += 1

for i in range(0,10000):
    print(i)
    for m in monkeys:
        print(m)
        m.inspectnthrow()

inspectnums = []

for m in monkeys:
    inspectnums.append(m.inspectnum)

inspectnums.sort(reverse=True)

print(inspectnums[0] * inspectnums[1])