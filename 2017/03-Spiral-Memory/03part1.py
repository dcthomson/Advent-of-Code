import sys

mysquare = int(sys.argv[1])

sq = 1

memgrid = dict()

x = 0
y = 0

while sq < mysquare:
    memgrid[(x,y)] = sq
    if sq == 1:
        x += 1
    elif (x - 1, y) in memgrid and (x, y + 1) not in memgrid:
        # go up
        y += 1
    elif (x, y - 1) in memgrid:
        # go left
        x -= 1
    elif (x + 1, y) in memgrid:
        # go down
        y -= 1
    elif (x, y + 1) in memgrid:
        # go right
        x += 1
    sq += 1

print(abs(x) + abs(y))
