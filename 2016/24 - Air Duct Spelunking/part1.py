import sys

class Coord:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

map = {}

found = []

start = None
tofind = []

beenthere = {}

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            map[(x,y)] = c
            try:
                num = int(c)
                if num == 0:
                    start = (x,y)
                tofind.append((x,y))
                print(x, y, c)
            except:
                pass
            x += 1
        y += 1
    

steps = 0
beenthere = {}
found = []

queue = [(start, steps)]

while len(queue) > 0:
    coord, steps = queue.pop(0)

    try:
        if int(map[coord]) not in found:
            print(found)
            print(tofind)
            if len(tofind) == len(found):
                print("found last num at ", coord, "in", steps, "steps")
                break
    except:
        pass
    
    adj_coords = [(coord[0] + 1, coord[1]),
                  (coord[0] - 1, coord[1]),
                  (coord[0], coord[1] + 1),
                  (coord[0], coord[1] - 1)]
    for coord in adj_coords:
        queue.append((coord, steps + 1))