import sys

with open(sys.argv[1], "r") as f:

    lines = []

    for line in f:
        lines.append(line.strip())

    timelines = 0

    def step(lines, linenum, beam=-1):

        global timelines
        
        # print(linenum, beam)

        if linenum == len(lines):
            timelines += 1
            print(timelines)
            return
        if beam == -1:
            for i, c in enumerate(lines[0]):
                if c == "S":
                    step(lines, linenum + 1, i)
        else:
            if lines[linenum][beam] == ".":
                step(lines, linenum + 1, beam)
            if lines[linenum][beam] == "^":
                step(lines, linenum + 1, beam - 1)
                step(lines, linenum + 1, beam + 1)

    step(lines, 0)

    print(timelines) 