import sys

pairs = {"}": "{",
         "]": "[",
         ">": "<",
         ")": "("}

pointsdict = {")": 3,
              "]": 57,
              "}": 1197,
              ">": 25137,
             }
points = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        linestack = ""
        for c in line:
            if c in pairs:
                if linestack[-1] != pairs[c]:
                    points += pointsdict[c]
                    break
                else:
                    linestack = linestack[:-1]      
            else:
                linestack += c

print(points)