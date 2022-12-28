import sys

class Monkey:

    def __init__(self, name, oper):
        self.name = name
        self.oper = False
        self.num = False
        if " " not in oper:
            self.num = int(oper)
        else:
            (self.m1, self.oper, self.m2) = oper.split()

    def job(self, m):
        if self.oper == "+":
            self.num = m[self.m1].num + m[self.m2].num
        elif self.oper == "-":
            self.num = m[self.m1].num - m[self.m2].num
        elif self.oper == "*":
            self.num = m[self.m1].num * m[self.m2].num
        elif self.oper == "/":
            self.num = int(m[self.m1].num / m[self.m2].num)

        if self.name == "root":
            return True
        return False

    def __str__(self):
        retstr = self.name + ": "
        if self.oper:
            retstr += self.m1 + " "
            retstr += self.oper + " " + self.m2
        else:
            retstr += "num: " + str(self.num)
        # retstr += "\n"
        return retstr 


monkeys = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (monkeyname, oper) = line.split(": ")
        monkeys[monkeyname] = Monkey(monkeyname, oper)

while True:
    for m in monkeys:
        if not monkeys[m].num:
            if monkeys[monkeys[m].m1].num and monkeys[monkeys[m].m2].num:
                if monkeys[m].job(monkeys):
                    print(monkeys[m].num)
                    exit()