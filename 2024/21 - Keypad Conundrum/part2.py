import sys
from itertools import product

inputcodes = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        inputcodes.append(line)

class pad:
    def __init__(self, p):
        self.pad = p
        self.dirs = {(0,-1):"^",(1,0):">",(0,1):"v",(-1,0):"<"}
        self.reset()
    
    def reset(self):
        self.current = self.pad["A"]

    def instructions(self, s):
        paths = []
        for c in s:
            paths.append(self.move(c))
        return list(product(*paths))
    
    def move(self, to):
        start = (self.current, [])
        q = []
        q.append(start)
        shortest = False
        paths = []
        while q:
            (current, path) = q.pop(0)
            path.append(current)
            if shortest and len(path) > shortest:
                break
            if current == self.pad[to]:
                paths.append(path)
                self.current = current
                if not shortest:
                    shortest = len(path)
            for d in self.dirs:
                next = (current[0] + d[0], current[1] + d[1])
                try:
                    if next in self.pad.values() and next not in path:
                        q.append((next, path.copy()))
                except:
                    pass
        current = self.pad[to]
        spaths = []
        for path in paths:
            spaths.append(self.coordstodirs(path))
        return spaths
    
    def coordstodirs(self, p):
        prev = False
        s = ""
        for current in p:
            if prev:
                for d in self.dirs:
                    if (prev[0] + d[0], prev[1] + d[1]) == current:
                        s += self.dirs[d]
            prev = current
        return s + "A"

p = {"7": (0,0),
     "8": (1,0),
     "9": (2,0),
     "4": (0,1),
     "5": (1,1),
     "6": (2,1),
     "1": (0,2),
     "2": (1,2),
     "3": (2,2),
     "0": (1,3),
     "A": (2,3)}

numpad = pad(p)
#print(numpad.instructions("029A"))

p = {"^": (1,0),
     "A": (2,0),
     "<": (0,1),
     "v": (1,1),
     ">": (2,1)}

robot1 = pad(p)
robot2 = pad(p)

total = 0

for code in inputcodes:
    # print(code, " ",  end="")
    shortest = False
    num = int(code.replace('A', ''))
    numpadinstructions = numpad.instructions(code)
    # print("n: ", numpadinstructions)
    for ilist in numpadinstructions:
        istr = "".join(ilist)
        # print(istr)
        robot1instructions = robot1.instructions(istr)
        for ilist2 in robot1instructions:
            istr2 = "".join(ilist2)
            # print(istr2)
            robot2instructions = robot2.instructions(istr2)
            # print("r1:", robot1instructions)
            for ilist3 in robot2instructions:
                istr3 = "".join(ilist3)
                # print(istr3)
                if not shortest or len(istr3) < shortest:
                    shortest = len(istr3)
    total += shortest * num
#     robot2instructions = robot2.instructions(robot1instructions)
#     print("r2:", robot2instructions)

#     print(len(robot2instructions), num)
#     print()
#     total += num * len(robot2instructions)

print(total)
# # robot4 = pad(p)
# # print()