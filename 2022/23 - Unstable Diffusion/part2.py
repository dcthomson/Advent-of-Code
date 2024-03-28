import sys

grove = {}
proposed = {}
dirs = "NSWE"

def printgrove(g):

    count = minx = miny = maxx = maxy = 0

    for coord in g:
        x = coord[0]
        y = coord[1]
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x,y) in g:
                pass
                # print("#", end="")
            else:
                # print(".", end="")
                count += 1
        # print()
    print(count)
    # print()




with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            if c == "#":
                grove[(x, y)] = True
            x += 1
        
        y += 1

dir = 0

# printgrove(grove)

round = 0
elfmoved = True

while elfmoved:

    for c in grove:
        # is anyone near me?
        nearme = False
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x != 0 or y != 0:
                    if (c[0] + x, c[1] + y) in grove:
                        nearme = True
        
        if nearme:
            thisdir = dir
            count = 0
            propose = False
            while not propose:
                if count > 4:
                    break
                thisdir = thisdir % 4
                propose = True
                if dirs[thisdir] == "N":
                    for x in (-1, 0, 1):
                        if (c[0] + x,c[1] - 1) in grove:
                            propose = False
                elif dirs[thisdir] == "S":
                    for x in (-1, 0, 1):
                        if (c[0] + x,c[1] + 1) in grove:
                            propose = False
                elif dirs[thisdir] == "W":
                    for y in (-1, 0, 1):
                        if (c[0] - 1,c[1] + y) in grove:
                            propose = False
                elif dirs[thisdir] == "E":
                    for y in (-1, 0, 1):
                        if (c[0] + 1,c[1] + y) in grove:
                            propose = False
                
                if propose:
                    if dirs[thisdir] == "N":
                        proposed[c] = (c[0],c[1] - 1)
                    elif dirs[thisdir] == "S":
                        proposed[c] = (c[0],c[1] + 1)
                    elif dirs[thisdir] == "W":
                        proposed[c] = (c[0] - 1,c[1])
                    elif dirs[thisdir] == "E":
                        proposed[c] = (c[0] + 1,c[1])
                thisdir += 1
                count += 1


    # check proposals and move them
    elfmoved = False
    for orig, p in proposed.items():
        count = 0
        for p2 in proposed.values():
            if p2 == p:
                count += 1
        if count == 1:
            elfmoved = True
            del grove[orig]
            grove[p] = True

    proposed = {}

    # printgrove(grove)

    dir += 1
    dir = dir % 4
    round += 1
print(round)