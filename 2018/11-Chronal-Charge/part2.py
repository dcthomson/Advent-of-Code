import sys

class fuelCell:
    def __init__(self, x, y, serial):
        self.x = x
        self.y = y
        rackid = x + 10
        plevel = rackid * y
        plevel += serial
        plevel *= rackid
        if plevel < 100:
            plevel = 0
        else:
            plevel = int(str(plevel)[-3])
        self.plevel = plevel - 5
        self.totalPower = False

    def getPowerSquares(self, grid):
        p = 0
        sqsize = 1
        squares = dict()
        while True:
            for x in range(self.x, self.x + sqsize):
                try:
                    p += grid[(x, self.y + sqsize - 1)].plevel
#                    print "sqsize: %s -- (%s, %s)" % (sqsize, x, self.y + sqsize - 1)
                except KeyError:
                    return squares
            for y in range(self.y, self.y + sqsize):
                try:
                    last = grid[(self.x + sqsize - 1, y)].plevel
                    p += last
#                    print "sqsize: %s -- (%s, %s)" % (sqsize, self.x + sqsize - 1, y)
                except KeyError:
                    return squares
            p -= last
#            print "(%s, %s, %s): %s" % (self.x, self.y, sqsize, p)
            squares[sqsize] = p
            sqsize += 1

    def getPower(self, grid):
        if not self.totalPower:
            p = 0
            for x in range(0, 3):
                for y in range(0, 3):
                    gridx = str(self.x + x)
                    gridy = str(self.y + y)
                    key = gridx + "-" + gridy
                    if key in grid:
                        p += grid[key].plevel
            self.totalPower = p
        return self.totalPower

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)


serial = int(sys.argv[1])

grid = dict()
# build grid
for x in range(1, 301):
    for y in range(1, 301):
        grid[(x,y)] = fuelCell(x, y, serial)

# build 

largestpower = False
lpcoord = False
lpsize = False
for x in range(1, 301):
    for y in range(1,301):
        power = grid[(x,y)].getPowerSquares(grid)
        try:
            maxpower = max(power.values())
            if not largestpower or maxpower > largestpower:
                largestpower = maxpower
                lpcoord = (x,y)
                lpsize = max(power, key=power.get)
                print("%s,%s,%s: %s" % (lpcoord[0], lpcoord[1], lpsize, largestpower))
        except ValueError:
            pass
                    
print(largestpower)
print("%s,%s,%s" % (lpcoord[0], lpcoord[1], lpsize))