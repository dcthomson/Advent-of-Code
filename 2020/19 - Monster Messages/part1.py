import sys

rules = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if line == "":
            break
        rulenum, rule = line.split(": ")
        rules[int(rulenum)] = rule

strings = []

print(rules)
print()

def runrule(currentruleset, strarr=[]):

    print(currentruleset, ":", s, " ", end="")
    if "a" in currentruleset or "b" in currentruleset:
        s += currentruleset.replace('"', '')
        s = [s]
    elif "|" in currentruleset:
        l, r = currentruleset.split("|")
        s1 = s2 = s
        s1 = runrule(l.strip(), s1)
        strings.append(s1)
        print("s1: ", s1)
        s2 = runrule(r.strip(), s2)
        print("s2: ", s2)
        strings.append(s2)
    else:
        for rnum in currentruleset.split():
            s = runrule(rules[int(rnum)], s)
    print(s)
    return s



print(runrule(rules[0]))

print(strings)

# longest = 0
# for s in strings:
#     if len(s) > longest:
#         longest = len(s)

# for s in strings:
#     if len(s) == longest:
#         print(s)