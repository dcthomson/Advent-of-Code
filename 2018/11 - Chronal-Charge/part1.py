class fuelCell:
    totalPower = -10
    def __init__(self, x, y, serial):
        self.x = x
        self.y = y
        rackid = x + 10
        plevel = rackid * y
        plevel += serial
        plevel *= rackid
        self.totalPower = False
        if plevel < 100:
            plevel = 0
        else:
            plevel = int(str(plevel)[-3])
        self.plevel = plevel - 5

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
        return "(%s, %s)-pl: %s --tp: %s" % (self.x, self.y, self.plevel, self.totalPower)

serial = 6303

grid = dict()
# build grid
for x in range(1, 301):
    for y in range(1, 301):
        grid[(x,y)] = fuelCell(x, y, serial)

largestPower = (-1, -1, -10)
for x in range(1, 301):
    for y in range(1,301):
        tp = grid[(x,y)].getPower(grid)
        if tp > largestPower[2]:
            largestPower = (x, y, tp)

print(largestPower)