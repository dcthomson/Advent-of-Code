import sys

class Tile:
    pic = ""

    def __init__(self, tile, num=None):
        self.num = num
        self.tile = tile
        self.coord = False

    def removeedge(self):
        newtile = []

        i = 1
        while i < len(self.tile) - 1:
            newtile.append(self.tile[i][1:-1])
            i += 1

        self.tile = newtile


    def findpattern(self, pattern):

        tilesize = len(self.tile[0])
        patwidth = len(pattern[0])
        patheight = len(pattern)

        x = y = 0
        seamonstercoords = {}
        while y < tilesize:
            x = 0
            while x < tilesize:
                patx = paty = 0
                match = True
                tmpcoords = {}
                while match and paty < patheight:
                    patx = 0
                    while match and patx < patwidth:
                        if pattern[paty][patx] == "#":
                            try:
                                if self.tile[y+paty][x+patx] == "#":
                                    tmpcoords[(x+patx,y+paty)] = True
                                else:
                                    match = False
                            except:
                                match = False
                        patx += 1
                    paty += 1
                if match:
                    for coord in tmpcoords:
                        seamonstercoords[coord] = True
                x += 1
            y += 1

        if len(seamonstercoords) > 0:
            total = 0
            x = y = 0
            while y < tilesize:
                x = 0
                while x < tilesize:
                    if (self.tile[y][x] == "#"):
                        if (x,y) not in seamonstercoords:
                            total += 1
                    x += 1
                y += 1
            print(total)


    def findmatches(self, t):
        for _ in range(0,3):
            if self.gettop() == t.getbottom():
                t.coord = (self.coord[0], self.coord[1] - 1)
                return
            elif self.getleft() == t.getright():
                t.coord = (self.coord[0] - 1, self.coord[1])
                return
            elif self.getright() == t.getleft():
                t.coord = (self.coord[0] + 1, self.coord[1])
                return
            elif self.getbottom() == t.gettop():
                t.coord = (self.coord[0], self.coord[1] + 1)
                return
            t.rotateCW()
        t.flip()
        for _ in range(0,3):
            if self.gettop() == t.getbottom():
                t.coord = (self.coord[0], self.coord[1] - 1)
                return
            elif self.getleft() == t.getright():
                t.coord = (self.coord[0] - 1, self.coord[1])
                return
            elif self.getright() == t.getleft():
                t.coord = (self.coord[0] + 1, self.coord[1])
                return
            elif self.getbottom() == t.gettop():
                t.coord = (self.coord[0], self.coord[1] + 1)
                return
            t.rotateCW()
            

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
        retstr += "ID: " + str(self.num)
        retstr += "  coord: "
        if self.coord:
            retstr += "(" + str(self.coord[0]) + ", "
            retstr += str(self.coord[1]) + ")"
        retstr += "\n"
        
        for r in self.tile:
            for c in r:
                retstr += c
            retstr += "\n"
        return retstr

    def rotateCW(self):

        newtile = []

        for line in reversed(self.tile):
            i = 0
            while i < len(line):
                if i >= len(newtile):
                    newtile.append([])
                newtile[i].append(line[i])
                i += 1

        self.tile = newtile

    def flip(self):
        newtile = []
        for line in reversed(self.tile):
            newtile.append(line)
        self.tile = newtile

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
            tiles[num] = Tile(tile, num)
    tiles[num] = Tile(tile, num)

first = True
allmapped = False
while not allmapped:
    for t in tiles:
        if first:
            tiles[t].coord = (0,0)
            first = False
        for t2 in tiles:
            if tiles[t].coord and not(tiles[t2].coord) and t != t2:
                tiles[t].findmatches(tiles[t2])
    allmapped = True
    for t in tiles:
        if not tiles[t].coord:
            allmapped = False

minx = None
miny = None
maxx = None
maxy = None
tilesize = 0
for t in tiles.values():
    t.removeedge()
    if minx is None:
        minx = t.coord[0]
    elif t.coord[0] < minx:
        minx = t.coord[0]
    if maxx is None:
        maxx = t.coord[0]
    elif t.coord[0] > maxx:
        maxx = t.coord[0]
    if miny is None:
        miny = t.coord[1]
    elif t.coord[1] < miny:
        miny = t.coord[1]
    if maxy is None:
        maxy = t.coord[1]
    elif t.coord[1] > maxy:
        maxy = t.coord[1]
    tilesize = len(t.tile[0])

# stitch it all together
bigtilelists = []
for y in range(miny, maxy + 1): 
    for z in range(0, tilesize):
        bigtilelists.append([])
        for x in range(minx, maxx + 1):
            for t in tiles.values():
                if t.coord == (x,y):
                    zindex = z + (tilesize * (y - miny))
                    bigtilelists[zindex] += t.tile[z]

bigtile = Tile(bigtilelists)

seamonsterstring = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

seamonster = []
for line in seamonsterstring.split("\n"):
    line = line.rstrip("\n")
    seamonster.append(list(line))

bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)
bigtile.flip()
bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)
bigtile.rotateCW()
bigtile.findpattern(seamonster)