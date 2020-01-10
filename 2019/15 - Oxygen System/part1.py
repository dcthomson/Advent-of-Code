import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import OpcodeComputer

# BFS - won't work cuz the robot can't jump to the next spot in queue

# check all possible directions and go the way that hasn't been traveled yet.
# if all traveled, go the way that was traveled the longest ago (keep track
# of coords and what step it was last traveled at)

line = ""

with open(sys.argv[1]) as f:
    line = f.readline()

opcode = OpcodeComputer.Opcode(line)

class Location:
    def __init__(self, coord, c=" "):
        self.x = coord[0]
        self.y = coord[1]
        self.commands = [1, 2, 3, 4]
        self.steps = False
        self.c = c

    def getdirandcoord(self):
        dir = self.commands.pop()
        if dir == 1:   # UP
            return (dir, (self.x, self.y + 1))
        elif dir == 2: # DOWN
            return (dir, (self.x, self.y - 1))
        elif dir == 3: # DOWN
            return (dir, (self.x - 1, self.y))
        elif dir == 4: # DOWN
            return (dir, (self.x + 1, self.y))

class omap:
    def __init__(self):
        self.omap = {(0,0): Location((0, 0), ".")}

    def printmap(self):
        # get map size
        smallx = None
        smally = None
        bigx = None
        bigy = None
        for k in self.omap:
            if smallx is None:
                smallx = k[1]
            elif k[1] < smallx:
                smallx = k[1]
            if smally is None:
                smally = k[0]
            elif k[0] < smally:
                smally = k[0]
            if bigx is None:
                bigx = k[1]
            elif k[1] > bigx:
                bigx = k[1]
            if bigy is None:
                bigy = k[0]
            elif k[0] > bigy:
                bigy = k[0]
        
        for y in range(smally, bigy):
            for x in range(smallx, bigx):
                if (x, y) in self.omap:
                    print(self.omap[(x, y)], end="")
                else:
                    print(" ", end="")
            print()
        
    def isvisited(self, coord):
        if coord in self.omap:
            return True
        



omap = omap()

visited = {}
steps = {}

loc = Location((0,0), ".")

Q = []
Q.append(loc)
visited[loc] = True
steps[loc] = 0
while ( Q ):
    loc = Q.pop()
    omap.printmap()
    print("\n")
    while loc.commands:
        command, nextloc = loc.getdirandcoord()
        robotout = opcode.runOpcode(command)
        if robotout == 0:
            omap.omap[(nextloc[0], nextloc[1])] = Location(nextloc, "#")
        elif robotout == 1:
            omap.omap[(nextloc[0], nextloc[1])] = Location(nextloc, ".")
            loc = omap.omap[nextloc]
        elif robotout == 2:
            print("FOUND IT:", steps[coord])
            exit()