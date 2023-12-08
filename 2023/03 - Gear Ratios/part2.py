import sys

class Num():

    def __init__(self, r, c, n):
        self.row = r
        self.colstart = c
        self.num = n
        self.colend = c

    def concatnum(self, n):
        self.colend += 1
        self.num += n

    def __str__(self):
        retstr = ""
        retstr += self.num
        retstr += ": "
        retstr += str(self.row)
        retstr += ","
        retstr += str(self.colstart)
        retstr += "-"
        retstr += str(self.colend)
        return retstr

grid = {}

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:

    y = 0
    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            grid[(x,y)] = c
            x += 1
            if x > maxx:
                maxx = x
        
        y += 1
        if y > maxy:
            maxy = y

numbers = []

creatingnum = False

for y in range(0, maxy):
    for x in range(0, maxx):
        if grid[(x, y)].isdigit():
            if not creatingnum:
                n = Num(y, x, grid[(x, y)])
                creatingnum = True
            else:
                n.concatnum(grid[(x, y)])
        else:
            if creatingnum:
                numbers.append(n)
                creatingnum = False

total = 0

for y in range(0, maxy):
    for x in range(0, maxx):
        if grid[(x,y)] == "*":
            numsadjacent = []
            for n in numbers:
                ny = n.row
                if y - 1 <= ny <= y + 1:
                    for nx in range(n.colstart, n.colend + 1):
                        if x - 1 <= nx <= x + 1:
                            numsadjacent.append(int(n.num))
                            break
            if len(numsadjacent) == 2:
                total += numsadjacent[0] * numsadjacent[1]

print(total)