import sys

conway = {}

with open(sys.argv[1], "r") as f:
    y = 0
    z = 0
    for line in f:
        line = line.rstrip()
        for x in range(0, len(line)):
            conway[(x,y,z)] = line[x]
        y += 1

for i in range(0, 6):

    # print("CYCLE: ", i, "\n")

    newconway = {}

    # print("CONWAY:    ", conway)
    # print("NEWCONWAY: ", newconway)

    xmin = xmax = ymin = ymax = zmin = zmax = None
    
    xs = []
    ys = []
    zs = []

    for k in conway:
        xs.append(k[0])
        ys.append(k[1])
        zs.append(k[2])

    xmin = min(xs)
    xmax = max(xs)
    ymin = min(ys)
    ymax = max(ys)
    zmin = min(zs)
    zmax = max(zs)

    # for z in range(zmin, zmax + 1):
    #     # print("z=", z)
    #     for y in range(ymin, ymax + 1):
    #         for x in range(xmin, xmax + 1):
    #             # print(conway[(x,y,z)], end="")
    #         # print()
    
    for x in range(xmin - 1, xmax + 2):
        for y in range(ymin - 1, ymax + 2):
            for z in range(zmin - 1, zmax + 2):
                # print(zmax)

                an = 0      # an = active neighbors

                for x2 in range(x - 1, x + 2):
                    for y2 in range(y - 1, y + 2):
                        for z2 in range(z - 1, z + 2):

                            if x == x2 and y == y2 and z == z2:
                                continue
                            try:
                                if conway[(x2, y2, z2)] == "#":
                                    an += 1
                            except:
                                pass

                newconway[(x,y,z)] = "."
                if (x,y,z) not in conway or conway[(x,y,z)] == ".":
                    # inactive
                    if an == 3:
                        newconway[(x,y,z)] = "#" 
                elif conway[(x,y,z)] == "#":
                    # active
                    if an == 2 or an == 3:
                        newconway[(x,y,z)] = "#"
    conway = newconway

    # print("\n")

active = 0

for k in conway:
    if conway[k] == "#":
        active += 1

print(active)