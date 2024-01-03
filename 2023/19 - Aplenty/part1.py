import sys

workflows = {}

class Workflow:

    def __init__(self, s):
        (self.name, rules) = s.split("{")
        self.rules = []
        rules = rules[:-1]
        rules = rules.split(',')
        for rule in rules:
            c = rn = ""
            if ":" in rule:
                (c, rn) = rule.split(":")
            else:
                c = False
                rn = rule
            self.rules.append({'condition': c, 'dest': rn})
    
    def parseworkflow(self, s, workflows):
        mystr = s[1:-1]
        vlist = mystr.split(",")
        vars = {}
        for v in vlist:
            (name,val) = v.split("=")
            vars[name] = int(val)
        

    def check(self, s, workflows):
        mystr = s[1:-1]
        vlist = mystr.split(",")
        vars = {}
        for v in vlist:
            (name,val) = v.split("=")
            vars[name] = int(val)
        for rule in self.rules:
            if rule['condition']:
                if '<' in rule['condition']:
                    (v, num) = rule['condition'].split('<')
                    if vars[v] < int(num):
                        if rule['dest'] == 'A':
                            total = 0
                            for value in vars.values():
                                total += int(value)
                            return total
                        elif rule['dest'] == 'R':
                            return 0
                        return workflows[rule['dest']].check(s, workflows)
                elif '>' in rule['condition']:
                    (v, num) = rule['condition'].split('>')
                    if vars[v] > int(num):
                        if rule['dest'] == 'A':
                            total = 0
                            for value in vars.values():
                                total += int(value)
                            return total
                        elif rule['dest'] == 'R':
                            return 0
                        return workflows[rule['dest']].check(s, workflows)
            else:
                if rule['dest'] == 'A':
                    total = 0
                    for value in vars.values():
                        total += int(value)
                    return total
                elif rule['dest'] == 'R':
                    return 0
                else:
                    return workflows[rule['dest']].check(s, workflows)

total = 0

with open(sys.argv[1], "r") as f:

    rules = True

    for line in f:
        line = line.strip()

        if line == "":
            rules = False
        elif rules:
            (name, _) = line.split("{")
            workflows[name] = Workflow(line)
        else:
            total += workflows['in'].check(line, workflows)
print(total)