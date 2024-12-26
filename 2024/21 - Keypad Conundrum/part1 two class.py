import sys

inputcodes = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        inputcodes.append(line)

class numpad:
    def __init__(self, p):
        self.pad = p
        self.reset()
    
    def reset(self):
        self.current = self.pad["A"]

    def instructions(self, s):
        ret = ""
        for c in s:
            ret += self.move(c)
        return ret
    
    def move(self, to):
        dirs = {(0,-1):"^",(1,0):">",(0,1):"v",(-1,0):"<"}
        start = self.current
        q = []
        q.append(start)
        came_from = dict()
        came_from[start] = None
        while q:
            current = q.pop(0)
            if current == self.pad[to]:
                self.current = current
                break
            for d in dirs:
                next = (current[0] + d[0], current[1] + d[1])
                try:
                    if next in self.pad.values() and next not in came_from:
                        q.append(next)
                        came_from[next] = current
                except:
                    pass
        current = self.pad[to]
        path = []
        while current != start:
            cf = came_from[current]
            for d in dirs:
                if (cf[0] + d[0], cf[1] + d[1]) == current:
                    path.append(dirs[d])
            current = came_from[current]
        path.reverse()
        path.append("A")
        path = "".join(path)
        return path

class dirpad:
    def __init__(self, p):
        self.pad = p
        self.reset()
    
    def reset(self):
        self.current = self.pad["A"]

    def sortstring(self, s):
        l = s.split("A")
        # print(l)
        sortedlist = []
        for lils in l:
            sortedstr = ""
            for c in (">v<^"):
                for _ in range(0, lils.count(c)):
                    sortedstr += c
            sortedlist.append(sortedstr)
        # print(sortedlist)
        return "A".join(sortedlist)

    def instructions(self, s):
        ret = ""
        s = self.sortstring(s)
        # print(s)
        for c in s:
            ret += self.move(c)
        return ret
    
    def move(self, to):
        dirs = {(0,-1):"^",(1,0):">",(0,1):"v",(-1,0):"<"}
        start = self.current
        q = []
        q.append(start)
        came_from = dict()
        came_from[start] = None
        while q:
            current = q.pop(0)
            if current == self.pad[to]:
                self.current = current
                break
            for d in dirs:
                next = (current[0] + d[0], current[1] + d[1])
                try:
                    if next in self.pad.values() and next not in came_from:
                        q.append(next)
                        came_from[next] = current
                except:
                    pass
        current = self.pad[to]
        path = []
        while current != start:
            cf = came_from[current]
            for d in dirs:
                if (cf[0] + d[0], cf[1] + d[1]) == current:
                    path.append(dirs[d])
            current = came_from[current]
        path.reverse()
        path.append("A")
        path = "".join(path)
        path = self.sortstring(path)
        return path

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
numpad = numpad(p)
#print(numpad.instructions("029A"))


p = {"^": (1,0),
     "A": (2,0),
     "<": (0,1),
     "v": (1,1),
     ">": (2,1)}
robot1 = dirpad(p)
robot2 = dirpad(p)

total = 0

for code in inputcodes:
    num = int(code.replace('A', ''))
    numpadinstructions = numpad.instructions(code)
    print("n: ", numpadinstructions)
    robot1instructions = robot1.instructions(numpadinstructions)
    print("r1:", robot1instructions)
    robot2instructions = robot2.instructions(robot1instructions)
    print("r2:", robot2instructions)

    print(len(robot2instructions), num)
    print()
    total += num * len(robot2instructions)

print(total)
# robot4 = pad(p)
# print()