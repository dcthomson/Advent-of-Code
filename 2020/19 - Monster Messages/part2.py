import sys

rules = {}
messages = []
longestmatch = 0

with open(sys.argv[1], "r") as f:
    matching = False
    for line in f:
        if not matching:
            line = line.rstrip()
            if line == "":
                matching = True
            else:
                rulenum, rule = line.split(": ")
                rules[int(rulenum)] = rule
        else:
            line = line.rstrip()
            messages.append(line)
            if len(line) > longestmatch:
                longestmatch = len(line)

# print(longestmatch)

# rules[8] = "42 | 42 8"
# rules[11] = "42 31 | 42 11 31"

tab = ""

def bfs(rules, queue = [0], matches = [], s = ""):

    while queue:
        # print("Q:", queue)
        m = queue.pop(0)
        # print("Q:", queue)
        rule = rules[int(m)]
        # print("s:", s)
        # print("rule:", rule)
        # print()
        if "|" in rule:
            queuecopy = queue.copy()
            (first, second) = rule.split(" | ")
            queue = first.split() + queue
            queuecopy = second.split() + queuecopy
            # if len(s) > longestmatch:
                # break
            matches = bfs(rules, queuecopy, matches, s)
        elif '"' in rule:
            if "a" in rule:
                s += "a"
            else:
                s += "b"
        else:
            queue = rule.split() + queue

    # print(s)

    matches.append(s)
    return matches

print(bfs(rules, [31]))

print(bfs(rules, [42]))

count = 0

for s in bfs(rules):
    if s in messages:
        print(s)
        count += 1

print(count)