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

def runrule(currentruleset, l=[""]):
    print("FIRST:", currentruleset, ":", l)
    ll = l.copy()
    for i, s in enumerate(l):
        if "a" in currentruleset or "b" in currentruleset:
            ll[i] += currentruleset.replace('"', '')
        elif "|" in currentruleset:
            left, right = currentruleset.split("|")
            ll[i] = runrule(left.strip(), [s])
            ll.append(runrule(right.strip(), [s]))
        else:
            first = True
            for rnum in currentruleset.split():
                if first:
                    ll[i] = runrule(rules[int(rnum)], [s])
                    first = False
                else:
                    ll.append(runrule(rules[int(rnum)], [s]))
        print("LAST:", ll)
    l = ll
    return l

print(runrule(rules[0]))

# longest = 0
# for s in strings:
#     if len(s) > longest:
#         longest = len(s)

# for s in strings:
#     if len(s) == longest:
#         print(s)