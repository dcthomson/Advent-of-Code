import sys

class WaterBoard:

    def __init__(self, file):
        self.rightbound = False
        self.leftbound = False
        self.topbound = False
        self.bottombound = False
        self.board = dict()
        self.streams = [WaterStream(500, 0)]
        for line in file:
            line = line.rstrip()
            (l, r) = line.split(", ")
            if l.startswith("x"):
                x = int(l.split("x=")[1])
                if not self.rightbound or x > self.rightbound:
                    self.rightbound = x
                if not self.leftbound or x < self.leftbound:
                    self.leftbound = x
                y = r.split("y=")[1]
                (y1, y2) = y.split("..")
                for y in range(int(y1), int(y2) + 1):
                    if not self.bottombound or y > self.bottombound:
                        self.bottombound = y
                    if not self.topbound or y < self.topbound:
                        self.topbound = y
                    self.board[(x, y)] = "#"
            else:
                y = int(l.split("y=")[1])
                if not self.bottombound or y > self.bottombound:
                    self.bottombound = y
                if not self.topbound or y < self.topbound:
                    self.topbound = y
                x = r.split("x=")[1]
                (x1, x2) = x.split("..")
                for x in range(int(x1), int(x2) + 1):
                    if not self.rightbound or x > self.rightbound:
                        self.rightbound = x
                    if not self.leftbound or x < self.leftbound:
                        self.leftbound = x
                    self.board[(x, y)] = "#"
    def go(self):
        for stream in self.streams:
            self.board = stream.go(self.board)

    def __str__(self):
        retstr = ""   
        watercount = 0   
        for y in range(self.topbound - 1, self.bottombound + 1):
            linestr = ""
            for x in range(self.leftbound - 1, self.rightbound + 2):
                if y == self.topbound - 1 and x == 500:
                    linestr += "+"
                elif (x, y) in self.board:
                    linestr += self.board[(x,y)]
                    if self.board[(x,y)] in "~":
                        watercount += 1                        
                else:
                    linestr += "."
            if "~" in linestr or "|" in linestr or "+" in linestr:
                retstr += linestr
                retstr += "\n"
            else:
                retstr += linestr
                retstr += "\n"
                break
        retstr = "\n Water Count: %s" % (watercount)
        return retstr

class WaterStream:
    
    def __init__(self, x, y, direction='down'):
        self.x = x
        self.y = y
        self.dir = direction

        self.buddy = None
        self.rstream = False
        self.lstream = False
        self.complete = False
        self.crashed = False
        
    def setBuddy(self, buddysream):
        self.buddy = buddystream
        
    def go(self, board):
        if self.complete:
            return board
        if self.lstream and self.rstream:
            if self.lstream:
                if not self.lstream.complete:
                    board = self.lstream.go(board)
            if self.rstream:
                if not self.rstream.complete:
                    board = self.rstream.go(board)
            if self.lstream.crashed and self.rstream.crashed:
                x = self.lstream.x
                while (x, self.y) not in board or board[(x, self.y)] != "#":
                    board[(x, self.y)] = "~"
                    x += 1
                x = self.rstream.x
                while (x, self.y) not in board or board[(x, self.y)] != "#":
                    board[(x, self.y)] = "~"
                    x -= 1
                self.y = self.y - 1
                board[(self.x, self.y)] = "|"
                self.lstream = False
                self.rstream = False
        else:
            if self.dir == "down":
                if (self.x, self.y + 1) not in board or board[(self.x, self.y + 1)] == "|":
                    board[(self.x, self.y + 1)] = "|"
                    self.y += 1
                elif board[(self.x, self.y + 1)] in "#~":
                    self.lstream = WaterStream(self.x, self.y, "left")
                    self.rstream = WaterStream(self.x, self.y, "right")
            else:
                if self.dir == "right":
                    x = 1
                elif self.dir == "left":
                    x = -1
                if (self.x + x, self.y) not in board or board[(self.x + x, self.y)] == "|":
                    board[(self.x + x, self.y)] = "|"
                    self.x = self.x + x
                    if (self.x, self.y + 1) not in board or board[(self.x, self.y + 1)] == "|":
                        self.dir = "down"
                else:
                    if board[(self.x + x, self.y)] in "#":
                        self.crashed = True
                        self.complete = True
                    
        return board
        
    def __str__(self):
        return "(%s, %s) %s" % (self.x, self.y, self.dir)
                    

file = open(sys.argv[1], "r")

wb = WaterBoard(file)

while not wb.go():
    print wb
#    stuff = raw_input()
    
