import sys

bricks = {}

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
        
        bricks[line] = brick

print(bricks)
print()

somethingmoved = True

while somethingmoved:
    somethingmoved = False

    for currentkey in bricks:
        letsmove = True
        for checkkey in bricks:
            if currentkey != checkkey:
                for currentcoord in bricks[currentkey]:
                    # check if coord is on the ground
                    if currentcoord['x'] == 1:
                        letsmove = False
                        break
                    for checkcoord in bricks[checkkey]:
                        if currentcoord['x'] == checkcoord['x']:
                            if currentcoord['y'] == checkcoord['y']:
                                if currentcoord['z'] - 1 == checkcoord['z']:
                                    letsmove = False
                                    break
                    if letsmove == False:
                        break
        if letsmove:
            somethingmoved = True
            print(bricks[currentkey])
            print()
            for coord in bricks[currentkey]:
                coord['z'] -= 1
            print(bricks[currentkey])