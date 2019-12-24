import sys

grid = {}

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line.rstrip():
            grid[(x, y)] = c
            x += 1
        y += 1

gridstrs = {}

while True:
    gridstr = ""
    newgrid = {}
    for y in range(0,5):
        for x in range(0,5):
            gridstr += grid[(x,y)]
            bugcount = 0
            try:
                if grid[(x + 1, y)] == "#":
                    bugcount += 1
            except:
                pass
            try:
                if grid[(x - 1, y)] == "#":
                    bugcount += 1
            except:
                pass
            try:
                if grid[(x, y + 1)] == "#":
                    bugcount += 1
            except:
                pass
            try:
                if grid[(x, y - 1)] == "#":
                    bugcount += 1
            except:
                pass
            if grid[(x, y)] == "#":
                if bugcount == 1:
                    newgrid[(x,y)] = "#"
                else:
                    newgrid[(x,y)] = "."
            elif grid[(x, y)] == ".":
                if bugcount == 1 or bugcount == 2:
                    newgrid[(x,y)] = "#"
                else:
                    newgrid[(x,y)] = "."

    if gridstr not in gridstrs:
        gridstrs[gridstr] = True
    else:
        break

    # for line in [gridstr[i:i+5] for i in range(0, len(gridstr), 5)]:
    #     print("".join(line))

    grid = newgrid

    # print(gridstr)
    # print()
# for line in [gridstr[i:i+5] for i in range(0, len(gridstr), 5)]:
#     print("".join(line))
print(gridstr)
i = 1
biodiv = 0  
for c in gridstr:
    if c == "#":
        biodiv += i
    i *= 2
print(biodiv)