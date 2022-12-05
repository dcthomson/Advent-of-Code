import sys
import string

with open(sys.argv[1], "r") as f:

    stacks = {}
    correctstacks = {}

    firstpart = True

    for line in f:
        line = line.rstrip()

        pos = 0

        if firstpart:

            if line == "":
                firstpart = False
            elif "[" in line:
                for c in line:
                    #print("#", c, "#", pos)
                    if firstpart:
                        if c in string.ascii_uppercase:
                            if pos not in stacks:
                                stacks[pos] = ""
                            stacks[pos] += c
                        pos += 1
            else:
                for c in line:
                    if c != " ":
                        correctstacks[int(c)] = stacks[pos]
                    pos += 1

        else:
            (_,num,_,fro,_,to) = line.split()

            s = correctstacks[int(fro)][0:int(num)] + correctstacks[int(to)]
            correctstacks[int(to)] = s
            s = correctstacks[int(fro)][int(num):]
            correctstacks[int(fro)] = s
    
    for k in sorted(correctstacks):
        print(correctstacks[k][0], end="")