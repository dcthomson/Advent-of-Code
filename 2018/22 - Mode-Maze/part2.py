import sys

f = open(sys.argv[1], "r")

class Coord:

    def __init__(self, coord, target, depth, minute, caveEL, tool=False):
        self.targetx = target[0]
        self.targety = target[1]
        self.target = target
        self.depth = depth
        x = coord[0]
        y = coord[1]
        self.x = x
        self.y = y
        self.minute = minute
        self.tool = tool
        self.el = False
        self.caveEL = caveEL
        if self.setGI():
            self.el = (self.gi + depth) % 20183
             
            self.type = self.el % 3
            # 0 . rocky
            # 1 = wet
            # 2 | narrow
            if self.tool:
                if self.type == 0 and self.tool == "N":
                    raise Exception("Can't use Nothing when rocky")
                if self.type == 1 and self.tool == "T":
                    raise Exception("Can't use Torch when wet")
                if self.type == 2 and self.tool == "C":
                    raise Exception("Can't use Climbing gear when narrow")
        else:
            raise Exception("Couldn't set Geologic Index")

    def getneighbors(self):
        neighbors = []
        for dir in ((self.x - 1, self.y),
                    (self.x + 1, self.y),
                    (self.x, self.y - 1),
                    (self.x, self.y + 1)):
            c = None
            # print(dir)
            if -1 not in dir:
                try:
                    c = Coord(dir, 
                            self.target, 
                            self.depth, 
                            self.minute + 1, 
                            self.caveEL,
                            self.tool)
                except:
                    # print(s)
                    c = Coord((self.x, self.y), 
                            self.target, 
                            self.depth, 
                            self.minute + 7,
                            self.caveEL,
                            self.getothertool())
                if c is not None:
                    neighbors.append(c)
        # if self.x == 9 and self.y == 11 and self.tool == "T":
            # for n in neighbors:
            #     print("NEIGHBOR:", n)
        return neighbors
                    
    def getothertool(self):
        if self.type == 0:
            if self.tool == "T":
                return "C"
            else:
                return "T"
        elif self.type == 1:
            if self.tool == "C":
                return "N"
            else:
                return "C"
        elif self.type == 2:
            if self.tool == "T":
                return "N"
            else:
                return "T"

    def amithetarget(self):
        if self.targetx == self.x and self.targety == self.y:
            print("TARGET AQUIRED")
            return True
        return False

    def stringify(self):
        return str(self.x) + "-" + str(self.y) + "-" + self.tool

    def __key(self):
        return (self.x, self.y, self.tool, self.minute)

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return str(self.x) + "," + str(self.y) + " " + self.tool + " " + str(self.minute) + " " + self.getChar()

    # def __eq__(self, other):
    #     if isinstance(other, ):
    #         return self.__key() == other.__key()
    #     return NotImplemented


    def setGI(self):
#       print "t: %s, d: %s" % (target, depth)
        if self.x == 0 and self.y == 0:
            self.gi = 0
        elif self.x == self.targetx and self.y == self.targety:
            self.gi = 0
        elif self.y == 0:
            self.gi = self.x * 16807
        elif self.x == 0:
            self.gi = self.y * 48271
        else:
            for coord in ((self.x - 1, self.y), (self.x, self.y - 1)):
                if coord not in self.caveEL:
                    try:
                        c = Coord(coord, 
                                self.target, 
                                self.depth,
                                self.minute,
                                self.caveEL)
                        self.caveEL[coord] = c.el
                    except:
                        return False
            self.gi = self.caveEL[(self.x - 1, self.y)] * self.caveEL[(self.x, self.y - 1)]

        return True


    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False
        else:
            if self.x < other.x:
                return True
            else:
                return False    

    def getChar(self):
        if self.type == 0:
            return "."
        elif self.type == 1:
            return "="
        elif self.type == 2:
            return "|"
        else:
            return "E"

with open(sys.argv[1], "r") as f:
     for line in f:
          line = line.rstrip()
          if line.startswith("depth"):
               depth = line.lstrip("depth: ")
          if line.startswith("target"):
               target = line.lstrip("target: ")

(targetx, targety) = target.split(",")
targetx = int(targetx)
targety = int(targety)
depth = int(depth)

target = (targetx, targety)

caveEL = {}

c = Coord((0, 0), target, depth, 0, caveEL, "T")

Q = [c]
visited = {c.stringify(): c.minute}

minutefound = False

while Q:
    Q.sort(key=lambda x: x.minute)
    node = Q.pop(0)
    # print(node)
    if minutefound:
        # print("minutefound: ", minutefound)
        if node.minute > minutefound:
            continue
    if node.amithetarget():
        if node.tool == "T":
            if not minutefound:
                minutefound = node.minute
            elif node.minute < minutefound:
                minutefound = node.minute
        else:
            Q.append(Coord((node.x, node.y), 
                            target, 
                            depth, 
                            node.minute + 7, 
                            caveEL, 
                            "T"))
    for neighbor in node.getneighbors():
        s = neighbor.stringify()
        # print(s)
        if s not in visited or neighbor.minute < visited[s]:
            # print("  N2:", neighbor)
            Q.append(neighbor)
            visited[neighbor.stringify()] = neighbor.minute
print(minutefound)