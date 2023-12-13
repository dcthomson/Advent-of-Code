import sys

leftright = ""
dirs = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if "=" not in line:
            if line != "":
                leftright = line
        else:
            (d, lr) = line.split(" = ")
            lr = lr.replace("(", "")
            lr = lr.replace(")", "")
            (l, r) = lr.split(", ")
            dirs[d] = {}
            dirs[d]['L'] = l
            dirs[d]['R'] = r

steps = 0
pos = "AAA"

while True:
    for lr in leftright:
        steps += 1
        pos = dirs[pos][lr]
        if pos == "ZZZ":
            print(steps)
            exit()