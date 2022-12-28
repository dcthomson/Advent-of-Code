import sys

class Monkey:

    def __init__(self, name, oper):
        self.name = name
        self.oper = False
        self.num = None
        if " " not in oper:
            self.num = int(oper)
        else:
            (self.m1, self.oper, self.m2) = oper.split()

    def job(self, m):
        if self.name == "root":
            self.num = 2
            if m[self.m1].num == m[self.m2].num:
                return True
            else:
                return False
        elif self.oper == "+":
            self.num = m[self.m1].num + m[self.m2].num
        elif self.oper == "-":
            self.num = m[self.m1].num - m[self.m2].num
        elif self.oper == "*":
            self.num = m[self.m1].num * m[self.m2].num
        elif self.oper == "/":
            self.num = int(m[self.m1].num / m[self.m2].num)

        return False

    def __str__(self):
        retstr = self.name + ": "
        if self.oper:
            retstr += self.m1 + " "
            retstr += self.oper + " " + self.m2 + " "
        if self.num is not None:
            retstr += "num: " + str(self.num)
        # retstr += "\n"
        return retstr 


monkeys = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (monkeyname, oper) = line.split(": ")
        monkeys[monkeyname] = Monkey(monkeyname, oper)

i = 3876907167001
while True:
    # print()
    # print(i)
    monkeys['humn'].num = i
    while monkeys['root'].num is None:
        # print(monkeys[monkeys['root'].m1].num, monkeys[monkeys['root'].m2].num)
        for m in monkeys:
            # print("all", monkeys[m])
            if monkeys[m].num is None:
                if monkeys[monkeys[m].m1].num is not None and monkeys[monkeys[m].m2].num is not None:

                    if monkeys[m].job(monkeys):
                        print(i)
                        exit()
                    elif (monkeys[m].name == 'root'):
                        print(i, monkeys[monkeys[m].m1].num, end="")
                        if monkeys[monkeys[m].m1].num > monkeys[monkeys[m].m2].num:
                            print(" > ", end="")
                        else:
                            print(" < ", end="")
                        print(monkeys[monkeys[m].m2].num)
                        break
    
    for m in monkeys:
        if monkeys[m].oper:
            monkeys[m].num = None
    i += 1