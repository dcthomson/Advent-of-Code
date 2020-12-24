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

for i in range(1, 101):

    tocheck = {}
    for k in tiles:
        if k not in tocheck:
            tocheck[k] = tiles[k]
        for coord in [(k[0] + 1, k[1], k[2] - 1),
                      (k[0] + 1, k[1] - 1, k[2]),
                      (k[0], k[1] - 1, k[2] + 1),
                      (k[0] - 1, k[1], k[2] + 1),
                      (k[0] - 1, k[1] + 1, k[2]),
                      (k[0], k[1] + 1, k[2] - 1)]:
            try:
                tocheck[coord] = tiles[coord]
            except:
                tocheck[coord] = "W"
    
    tiles = {}
    
    for k in tocheck:
        blackadj = 0
        for coord in [(k[0] + 1, k[1], k[2] - 1),
                      (k[0] + 1, k[1] - 1, k[2]),
                      (k[0], k[1] - 1, k[2] + 1),
                      (k[0] - 1, k[1], k[2] + 1),
                      (k[0] - 1, k[1] + 1, k[2]),
                      (k[0], k[1] + 1, k[2] - 1)]:
            try:
                if tocheck[coord] == "B":
                    blackadj += 1
            except:
                pass
        if tocheck[k] == "B":
            if blackadj == 0 or blackadj > 2:
                tiles[k] = "W"
            else:
                tiles[k] = "B"
        elif tocheck[k] == "W":
            if blackadj == 2:
                tiles[k] = "B"
            else:
                tiles[k] = "W"

blacktiles = 0
for k in tiles:
    if tiles[k] == "B":
        blacktiles += 1

print(blacktiles)