import sys

grid = {}

x = y = xmax = ymax = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            grid[(x,y)] = c
            x += 1
            if x > xmax:
                xmax = x
        y += 1
        if y > ymax:
            ymax = y

xmascount = 0

for y in range(0, ymax):
    for x in range(0, xmax):
        if grid[(x,y)] == "A":
            try:
                bslash = grid[(x-1,y-1)] + "A" + grid[(x+1,y+1)]
                slash = grid[(x+1,y-1)] + "A" + grid[(x-1,y+1)]
                if slash == "MAS" or slash == "SAM":
                    if bslash == "MAS" or bslash == "SAM":
                        xmascount += 1
            except:
                pass
                
print(xmascount)