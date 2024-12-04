import sys

grid = dict()

maxx = 0
maxy = 0

aroom = [(3,2), (3,3)]
broom = [(5,2), (5,3)]
croom = [(7,2), (7,3)]
droom = [(9,2), (9,3)]
porch = [(3,1), (5,1), (7,1), (9,1)]

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = c
            if c in ['ABCD']:
                
            x += 1
        maxx = x
        y += 1
    maxy = y



print(grid)