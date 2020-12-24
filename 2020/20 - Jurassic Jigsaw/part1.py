import sys

class Tile:
    pic = ""

    def __init__(self, num, tiles):
        self.num = num
        self.top = tiles[0]
        self.bottom = tiles[9]
        self.left = []
        self.right = []
        for i in range(0,10):
            self.left.append(tiles[i][0])
            self.right.append(tiles[i][9])

tile = []
tiles = []
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
            tiles.append(Tile(num, tile))