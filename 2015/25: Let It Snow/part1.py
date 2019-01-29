import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

curx = 1
cury = 1
grid = dict()

grid[(curx, cury)] = 20151125

while curx != x or cury != y:
    nextnum = grid[(curx, cury)] * 252533 % 33554393
    if cury == 1:
        cury = curx + 1
        curx = 1
    else:
        cury -= 1
        curx += 1
    grid[(curx, cury)] = nextnum

print(grid[(curx, cury)])