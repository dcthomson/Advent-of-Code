import sys

rules = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if line == "":
            break
        rulenum, rule = line.split(": ")
        rules[int(rulenum)] = rule

print(rules)

strings = []

def runrule(currentruleset, s=""):
    if "a" in currentruleset or "b" in currentruleset:
        s += currentruleset.replace('"', '')
        # strings.append(s)
    elif "|" in currentruleset:
        for r in currentruleset.split("|"):
            s = runrule(r.strip(), s)
    else:
        for rnum in currentruleset.split():
            s = runrule(rules[int(rnum)], s)
    print(s)
    return s

runrule(rules[0])

# longest = 0
# for s in strings:
#     if len(s) > longest:
#         longest = len(s)

# for s in strings:
#     if len(s) == longest:
#         print(s)