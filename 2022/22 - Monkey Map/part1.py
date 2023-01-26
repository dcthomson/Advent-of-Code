import sys

class Board:

    def __init__(self, board):
        self.board = board
        self.dir = 0
        self.maxx = self.maxy = 0
        self.y = 1
        i = 1
        while True:
            if (i,self.y) in self.board:
                self.x = i
                break
            i += 1
        for coord in self.board:
            if coord[0] > self.maxx:
                self.maxx = coord[0]
            if coord[1] > self.maxy:
                self.maxy = coord[1]

    def turnright(self):
        self.dir += 1
        if self.dir == 4:
            self.dir = 0
    
    def turnleft(self):
        self.dir -= 1
        if self.dir == -1:
            self.dir = 3

    def move(self, num):
        for i in range(num):
            nextcoord = False
            if self.dir == 0:
                if (self.x + 1, self.y) in self.board:
                    nextcoord = (self.x + 1, self.y)
                else:
                    for x in range(self.maxx + 1):
                        if (x, self.y) in self.board:
                            nextcoord = (x, self.y)
                            break

            elif self.dir == 1:
                if (self.x, self.y + 1) in self.board:
                    nextcoord = (self.x, self.y + 1)
                else:
                    for y in range(self.maxy + 1):
                        if (self.x, y) in self.board:
                            nextcoord = (self.x, y)
                            break

            elif self.dir == 2:
                if (self.x - 1, self.y) in self.board:
                    nextcoord = (self.x - 1, self.y)
                else:
                    for x in range(self.maxx, 0, -1):
                        if (x, self.y) in self.board:
                            nextcoord = (x, self.y)
                            break

            elif self.dir == 3:
                if (self.x, self.y - 1) in self.board:
                    nextcoord = (self.x, self.y - 1)
                else:
                    for y in range(self.maxy, 0, -1):
                        if (self.x, y) in self.board:
                            nextcoord = (self.x, y)
                            break

            if self.board[nextcoord] == "#":
                return
            elif self.board[nextcoord] == ".":
                self.x = nextcoord[0]
                self.y = nextcoord[1]

    def getpassword(self):
        return (self.y * 1000) + (self.x * 4) + self.dir

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.dir)

b = {}
dirs = []

with open(sys.argv[1], "r") as f:

    y = 1

    boardinput = True

    for line in f:
        line = line.rstrip()

        if line == "":
            boardinput = False

        if boardinput:
            x = 1

            for c in line:
                if c in ".#":
                    b[(x,y)] = c
                x += 1
            y += 1
        else:
            if line != "":
                dir = ""
                for c in line:
                    if c in "RL":
                        dirs.append(int(dir))
                        dirs.append(c)
                        dir = ""
                    else:
                        dir += c
                if dir != "":
                    dirs.append(int(dir))

board = Board(b)

for d in dirs:
    if d == "R":
        board.turnright()
    elif d == "L":
        board.turnleft()
    else:
        board.move(d)

print(board.getpassword())