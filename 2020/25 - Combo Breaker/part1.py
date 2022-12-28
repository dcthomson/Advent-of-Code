import sys

tiles = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        north = False
        south = False
        x = y = z = 0
        for c in line:
            if c == "n":
                north = True
            elif c == "s":
                south = True
            elif c == "e":
                if north:
                    x += 1
                    z -= 1
                    north = False
                elif south:
                    y -= 1
                    z += 1
                    south = False
                else:
                    x += 1
                    y -= 1
            elif c == "w":
                if north:
                    y += 1
                    z -= 1
                    north = False
                elif south:
                    x -= 1
                    z += 1
                    south = False
                else:
                    x -= 1
                    y += 1
        
        if (x, y, z) in tiles:
            if tiles[(x, y, z)] == "W":
                tiles[(x, y, z)] = "B"
            else:
                tiles[(x, y, z)] = "W"
        else:
            tiles[(x, y, z)] = "B"

blacktiles = 0
for k in tiles:
    if tiles[k] == "B":
        blacktiles += 1

print(blacktiles)