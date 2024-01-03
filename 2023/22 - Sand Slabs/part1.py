import sys

bricks = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (s,e) = line.split("~")
        (sx, sy, sz) = [int(i) for i in s.split(",")]
        (ex, ey, ez) = [int(i) for i in e.split(",")]

        brick = []

        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    brick.append({'x': x, 'y': y, 'z': z})
        
        bricks.append(brick)

print(bricks)

somethingmoved = True

while somethingmoved:
    somethingmoved = False

    for b in bricks:
        vertical = False
        # check if vertical
        for c in b:
            for c2 in b:
                if c == c2:
                    next
                tc = c2
                tc['z'] = c2['z'] - 1
                if c == tc:
                    vertical = True
                    break
                tc = c
                tc['z'] = c['z'] - 1
                if c2 == tc:
                    vertical = True
                    break
        if vertical:
            # find lowest brick
            z = None
            for c in b:
                if z is None:
                    z = c['z']
                elif c['z'] < z:
                    z = c['z']
                    
                
        # if brick is vertical
            # check lowest brick
        # else
            # check all bricks
        nothingbelow = True
        for coord in b:
            if 
