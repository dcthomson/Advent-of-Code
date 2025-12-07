import sys

with open(sys.argv[1], "r") as f:

    y = xmax = ymax = 0

    grid = {}

    for line in f:
        x = 0
        for c in line.strip():
            grid[(x,y)] = c
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y
        y += 1

    for y in range(ymax, 0 - 1, -1):
        for x in range(0, xmax):
            if grid[(x,y)] in  "^S":
                l = r = False
                linenum = y + 1
                while linenum <= ymax:
                    if not l:
                        if isinstance(grid[(x-1, linenum)], int):
                            l = grid[(x-1, linenum)]
                    if not r:
                        if isinstance(grid[(x+1, linenum)], int):
                            r = grid[(x+1, linenum)]
                    linenum += 1
                if not l:
                    l = 1
                if not r:
                    r = 1
                num = l + r
                if grid[(x,y)] == "S":
                    print(num)
                else:
                    grid[(x, y)] = num