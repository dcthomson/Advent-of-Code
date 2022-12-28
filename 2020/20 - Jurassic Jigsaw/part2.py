import sys

class Tile:
    pic = ""

    def __init__(self, num, tile):
        self.num = num
        self.tile = tile
        self.matches = 0

    def checksides(self, t):
        for side in (self.gettop(), self.getleft(), self.getright(), self.getbottom()):
            for tside in (t.gettop(), t.getleft(), t.getright(), t.getbottom()):
                if side == tside:
                    self.matches += 1
                revtside = tside.copy()
                revtside.reverse()
                if side == revtside:
                    self.matches += 1

    def gettop(self):
        return self.tile[0]
    def getright(self):
        retlist = []
        for line in self.tile:
            retlist.append(line[-1])
        return retlist
    def getleft(self):
        retlist = []
        for line in self.tile:
            retlist.append(line[0])
        return retlist
    def getbottom(self):
        return self.tile[-1]
    
    def __str__(self):
        retstr = ""
        for r in self.tile:
            for c in r:
                retstr += c
            retstr += "\n"
        return retstr

tile = []
tiles = {}
num = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("Tile"):
            tile = []
            num = int(line.split(" ")[1].split(":")[0])
        elif "." in line or "#" in line:
            l = []
            l[:0] = line
            tile.append(l)
        else:
            tiles[num] = Tile(num, tile)
    tiles[num] = Tile(num, tile)

for t in tiles:
    for t2 in tiles:
        if t != t2:
            tiles[t].checksides(tiles[t2])

total = 1

for t in tiles:
    if tiles[t].matches == 2:
        total *= tiles[t].num

print(total)