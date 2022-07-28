import sys

pairs = {"}": "{",
         "]": "[",
         ">": "<",
         ")": "("}

pointsdict = {"(": 1,
              "[": 2,
              "{": 3,
              "<": 4,
             }
points = 0

scores = list()

with open(sys.argv[1], "r") as f:
    for line in f:
        broken = False
        linestack = ""
        for c in line.rstrip():
            if c in pairs:
                if linestack[-1] != pairs[c]:
                    broken = True
                    break
                else:
                    linestack = linestack[:-1]      
            else:
                linestack += c
        if linestack != "" and not broken:
            linescore = 0
            for c in linestack[::-1]:
                linescore *= 5
                linescore += pointsdict[c]
            scores.append(linescore)
scores = sorted(scores)
print(scores[len(scores)//2])