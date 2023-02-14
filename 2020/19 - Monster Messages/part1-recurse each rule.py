import sys

rules = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        rulenum, rule = line.split(": ")
        rules[int(rulenum)] = rule

print(rules)

def runrule(currentrule, s=""):
    print("rule:", currentrule)
    print("   s:", s)
    if "a" in rules[currentrule] or "b" in rules[currentrule]:
        s += rules[currentrule].replace('"', '')
        #print(s)
    else:
        for r in rules[currentrule].split("|"):
            news = s
            r = r.strip()
            for n in r.split():
                news += runrule(int(n), news)
            print(news)
    return s

runrule(0)