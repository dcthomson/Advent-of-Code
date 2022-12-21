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

        if minx is None or sx < minx:
            minx = sx
        if bx < minx:
            minx = bx
        if miny is None or sy < miny:
            miny = sy
        if by < miny:
            miny = by
        if maxx is None or sx > maxx:
            maxx = sx
        if bx > maxx:
            maxx = bx
        if maxy is None or sy > maxy:
            maxy = sy
        if by > maxy:
            maxy = by

        dist = abs(sx - bx) + abs(sy - by)

        sensors[(sx,sy)] = dist

for s in sensors:
    print(s)
    x = s[0]
    y1 = s[1] - sensors[s]
    y2 = s[1] + sensors[s]
    growth = 0
    while y1 != s[1] + 1:
        left = x - growth
        right = x + growth
        if left < minx:
            minx = left
        if right > maxx:
            maxx = right
        for w in range(left, right+1):
            if (w,y1) not in grid:
                grid[(w,y1)] = "#"
            if (w,y2) not in grid:
                grid[(w,y2)] = "#"
        growth += 1
        y1 += 1
        y2 -= 1

# for y in range(miny, maxy+1):
#     for x in range(minx, maxx+1):
#         if (x,y) not in grid:
#             print(".", end="")
#         else:
#             print(grid[(x,y)], end="")
#     print()


total = 0

for c in grid:
    if c[1] == row:
        if grid[c] != "B":
            total += 1

print(total)