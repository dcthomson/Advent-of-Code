import sys

leftright = ""
dirs = {}
pos = []

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
            if d.endswith("A"):
                pos.append(d)
            dirs[d] = {}
            dirs[d]['L'] = l
            dirs[d]['R'] = r

steps = 0

while True:
    for lr in leftright:
        end = True
        newpos = []
        steps += 1
        for p in pos:
            newpos.append(dirs[p][lr])
            if not dirs[p][lr].endswith("Z"):
                end = False
        if end:
            print(steps)
            exit()
        pos = newpos