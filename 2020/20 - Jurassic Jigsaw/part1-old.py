import sys

class Tile:
    pic = ""

    def __init__(self, num, tile):
        self.num = num
        self.tile = False
        self.tiles = []
        self.tiles.append(tile)
        self.tiles.append(self.rotatecw(tile))
        self.tiles.append(self.rotatecw(self.tiles[1]))
        self.tiles.append(self.rotatecw(self.tiles[2]))

        self.up = False
        self.right = False
        self.down = False
        self.left = False

    def rotatecw(self, t):
        newtile = []
        for _ in range(0, 10):
            newtile.append([None] * 10)
        for y in range(0, 10):
            for x in range(0, 10):
                newtile[x][9-y] = t[y][x]
        return newtile

    def settile(self, n):
        self.tile = self.tiles[n]

    def checkifneighbor(self, t):
        currenttile = 0
        attached = False
        for i in range(0, 4):
            currenttile = i
            # check if above
            if not self.up:
                if self.tile[0] == t.tiles[i][9]:
                    self.up = t.num
                    attached = True
                    break
            # check if below
            if not self.down:
                if self.tile[9] == t.tiles[i][0]:
                    self.down = t.num
                    attached = True
                    break
            # check if right and left
            right = True
            left = True
            for j in range(0, 10):
                if self.tile[j][0] != t.tiles[i][j][9]:
                    left == False
                if self.tile[j][9] != t.tiles[i][j][0]:
                    right == False
                if not right and not left:
                    break
            if right:
                self.right = t.num
                attached = True
                break
            if left:
                self.left = t.num
                attached = True
                break
        if attached:
            t.settile(currenttile)
            

    def printtile(self, t):
        for r in t:
            for c in r:
                print(c, end="")
            print()

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
            tile.append(line)
        else:
            tiles[num] = Tile(num, tile)


tileset = []
allset = False
orientation = False
currenttile = False

while not allset:
    for tnum in toset:
        if not orientation:
            currenttile = tnum
            orientation = True
        elif tiles[tnum].tile:
            currenttile = tnum
        for 