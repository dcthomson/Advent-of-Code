import sys

mysquare = int(sys.argv[1])

class Coord:

    def __init__(self, x, y, memgrid):
        self.x = x
        self.y = y
        self.num = 0
        if x == 0 and y == 0:
            self.num += 1
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    pass
                else:
                    try:
                        self.num += memgrid[(self.x + x, self.y + y)].num
                    except KeyError:
                        pass


sq = 1

memgrid = dict()

coordval = 0

x = 0
y = 0

while coordval <= mysquare:
    memgrid[(x,y)] = Coord(x,y,memgrid)
    coordval = memgrid[(x,y)].num
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

print(coordval)
