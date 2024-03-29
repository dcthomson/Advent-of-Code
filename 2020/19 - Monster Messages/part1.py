import sys

rules = {}
matches = []

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
            matches.append(line.rstrip())

tab = ""

def bfs(queue, rules, tab, count = 0, s = ""):

    while queue:
        # print(tab, "Q:", queue)
        m = queue.pop(0)
        # print(tab, "Q:", queue)
        rule = rules[int(m)]
        # print(tab, "s:", s)
        # print(tab, "rule:", rule)
        # print()
        if "|" in rule:
            queuecopy = queue.copy()
            (first, second) = rule.split(" | ")
            queue = first.split() + queue
            queuecopy = second.split() + queuecopy
            count = bfs(queuecopy, rules, tab + "  ", count, s)
        elif '"' in rule:
            if "a" in rule:
                s += "a"
            else:
                s += "b"
        else:
            queue = rule.split() + queue

    # print(s)

    if s in matches:
        count += 1
    return count

queue = [0]

count = bfs(queue, rules, tab)

print(count)