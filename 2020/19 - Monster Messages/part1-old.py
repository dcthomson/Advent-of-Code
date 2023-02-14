import sys

class Rule:

    def __init__(self, num, rule):
        self.num = num
        rule = rule.replace('"', '')
        rules = rule.split("|")
        self.rules = []
        for r in rules:
            r = r.strip()
            self.rules.append(r.split())
        self.distributed = False

    def __str__(self):
        retstr = ""
        retstr += str(self.num)
        retstr += ": " + str(self.rules)
        return retstr

    def done(self):
        for r in self.rules:
            for i in r:
                if str(i).isdigit():
                    return False
        return True

    def update(self, num, chars):
        for 

rules = {}
inputtingrules = True
recvmsg = []

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if line == "":
            inputtingrules = False
        elif inputtingrules:
            num, rule = line.split(": ")
            num = int(num)
            rules[num] = Rule(num, rule)
        else:
            recvmsg.append(line)

while not rules[0].done():

    for r in rules:
        print(rules[r])
        print(rules[r].done())

        if rules[r].done():
            for r2 in rules:
                for r3 in rules[r2].rules:
                    for element in r3:

    break


