import sys

class Gridcomputingcluster:

    def __init__(self, f):
        self.grid = dict()
        with open(f, 'r') as f:
            y = 0
            xmax = -1
            ymax = -1
            for line in f:
                line = line.strip()
                x = 0
                for c in line:
                    self.grid[(x, y)] = c
                    x += 1
                    if x > xmax:
                        xmax = x
                y += 1
                if y > ymax:
                    ymax = y
        xmid = (xmax - 1) / 2
        ymid = (ymax - 1) / 2
        self.vc = Viruscarrier((int(xmid), int(ymid)), 'U')

    def run(self):
        self.vc.burst(self.grid)

    def getinfections(self):
        return self.vc.infections

    def printgrid(self):
        sx = None
        bx = None
        sy = None
        by = None
        for k in self.grid:
            if sx is None or k[0] < sx:
                sx = k[0]
            if bx is None or k[0] > bx:
                bx = k[0]
            if sy is None or k[1] < sy:
                sy = k[1]
            if by is None or k[1] > by:
                by = k[1]


        print(self.vc.loc, self.vc.dir)
        for y in range(sy, by + 1):
            for x in range(sx, bx + 1):
                if (x, y) not in self.grid:
                    print(".", end="")
                else:
                    print(self.grid[(x, y)], end="")
            print()

class Viruscarrier:

    def __init__(self, loc, dir='U'):
        self.loc = loc
        self.dir = dir
        self.dirs = "URDL"
        self.infections = 0
        self.clensings = 0

    def burst(self, grid):
        self.turn(grid)
        self.change(grid)
        self.move()

    def turn(self, grid):
        if self.loc not in grid:
            grid[self.loc] = "."
        if grid[self.loc] == "#":
            try:
                self.dir = self.dirs[self.dirs.find(self.dir) + 1]
            except IndexError:
                self.dir = self.dirs[0]
        elif grid[self.loc] == ".":
            self.dir = self.dirs[self.dirs.find(self.dir) - 1]
        elif grid[self.loc] == "F":
            self.dir = self.dirs[self.dirs.find(self.dir) - 2]

    def change(self, grid):
        if grid[self.loc] == "#":
            grid[self.loc] = "F"
        elif grid[self.loc] == "F":
            grid[self.loc] = "."
        elif grid[self.loc] == ".":
            grid[self.loc] = "W"
        elif grid[self.loc] == "W":
            grid[self.loc] = "#"
            self.infections += 1

    def move(self):
        if self.dir == 'U':
            self.loc = (self.loc[0], self.loc[1] - 1)
        if self.dir == 'R':
            self.loc = (self.loc[0] + 1, self.loc[1])
        if self.dir == 'D':
            self.loc = (self.loc[0], self.loc[1] + 1)
        if self.dir == 'L':
            self.loc = (self.loc[0] - 1, self.loc[1])

gcc = Gridcomputingcluster(sys.argv[1])

for i in range(10000000):
#    gcc.printgrid()
#    print()
    gcc.run()
print(gcc.getinfections())