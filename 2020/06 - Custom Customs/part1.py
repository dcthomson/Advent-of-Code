import sys

with open(sys.argv[1], "r") as f:

    highest = 0

    questions = {}

    total = 0

    for line in f:
        line = line.rstrip()
        if line == "":
            total += len(questions)
            questions = {}
        else:
            for c in line:
                questions[c] = 1
    total += len(questions)
    print(total)