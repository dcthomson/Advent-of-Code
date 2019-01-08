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

    def getPowerSquare(self, grid, sqsize):
        if not self.totalPower:
            p = 0
            for x in range(0, sqsize):
                for y in range(0, sqsize):
                    p += grid[(self.x + x, self.y + y)]
        return p

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
        return "(%d, %d) pl: %d   sq: %d   tp: %d" % (self.x, self.y, self.plevel, self.sqsize, self.totalPower)


serial = 18

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
        tp = 0
        sqsize = 1
        breakflag = False
        for sqsize in range(1,301):
            grid[(x,y)].getPowerSquare(grid, sqsize)



#        for x2 in range(x, x + sqsize - 1):
#            for y2 in range(y, y + sqsize - 1):
#                tp += grid[(xsqsize,ysqsize)]
#            sqsize += 1
#        if not largestpower:
#            largestpower = tp
#            lpcoord = (x,y)
#            lpsize = 
        

#        (tp, sqsize) = grid[(x,y)].getPower(grid)
#        print grid[key]
#        if tp > largestPower[2]:
#            largestPower = (x, y, sqsize, tp)

print largestPower
