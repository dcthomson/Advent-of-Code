import sys

with open(sys.argv[1], "r") as f:

    groups = []
    group = []

    for line in f:
        line = line.rstrip()
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)
    groups.append(group)

    total = 0

    for g in groups:
        first = True
        newquestions = ""
        for q in g:
            newquestions = ""
            if first:
                questions = q
                first = False
            else:
                for c in q:
                    if c in questions:
                        newquestions += c
                questions = newquestions
        total += len(questions)

    print(total)