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
        

    def check(self, vars, workflows):
        for rule in self.rules:
            if rule['condition']:
                if '<' in rule['condition']:
                    (v, num) = rule['condition'].split('<')
                    if vars[v] < int(num):
                        if rule['dest'] == 'A':
                            return True
                        elif rule['dest'] == 'R':
                            return False
                        return workflows[rule['dest']].check(vars, workflows)
                elif '>' in rule['condition']:
                    (v, num) = rule['condition'].split('>')
                    if vars[v] > int(num):
                        if rule['dest'] == 'A':
                            return True
                        elif rule['dest'] == 'R':
                            return False
                        return workflows[rule['dest']].check(vars, workflows)
            else:
                if rule['dest'] == 'A':
                    return True
                elif rule['dest'] == 'R':
                    return False
                else:
                    return workflows[rule['dest']].check(vars, workflows)

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

for x in range(1, 4001):
    for m in range(1, 4001):
        print(x,m, total)
        for a in range(1, 4001):
            for s in range(1, 4001):
                v = {'x': x, 'm': m, 'a': a, 's': s}
                if workflows['in'].check(v, workflows):
                    total += 1
print(total)