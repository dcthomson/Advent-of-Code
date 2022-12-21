import sys

row = 2000000

sensors = {}
grid = {}

minx = miny = maxx = maxy = None

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (_,_,sx,sy,_,_,_,_,bx,by) = line.split()
        sx = sx.split("=")[1]
        sy = sy.split("=")[1]
        bx = bx.split("=")[1]
        by = int(by.split("=")[1])
        sx = int(sx[:-1])
        sy = int(sy[:-1])
        bx = int(bx[:-1])

        grid[(sx,sy)] = "S"
        grid[(bx,by)] = "B"

        dist = abs(sx - bx) + abs(sy - by)

        if minx is None or sx - dist < minx:
            minx = sx - dist
        if maxx is None or sx + dist > maxx:
            maxx = sx + dist

        sensors[(sx,sy)] = dist

y = row

count = 0

for x in range(minx, maxx+1):
    for s in sensors:
        if (abs(s[0] - x) + abs(s[1] - y)) <= sensors[s]:
            if (x,y) in grid and grid[(x,y)] == "B":
                pass
            else:
                count += 1
                break

print(count)