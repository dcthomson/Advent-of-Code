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

def findxmas(coord, dir):
    try:
        if grid[(coord[0] + dir[0], coord[1] + dir[1])] == "M":
            if grid[(coord[0] + dir[0] * 2, coord[1] + dir[1] * 2)] == "A":
                if grid[(coord[0] + dir[0] * 3, coord[1] + dir[1] * 3)] == "S":
                    return True
    except:
        pass
    return False

xmascount = 0

dirs = ((0, -1),(1, -1),(1, 0),(1, 1),(0, 1),(-1, 1),(-1,0),(-1,-1))

for y in range(0, ymax):
    for x in range(0, xmax):
        if grid[(x,y)] == "X":
            for dir in dirs:
                if findxmas((x,y), dir):
                    xmascount += 1    
                
print(xmascount)