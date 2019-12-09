import sys

def getcoords(dirs):
    coords = {}
    x = 0
    y = 0
    for d in dirs:
        dir = d[0]
        count = int(d[1:])
        if dir == "R":
            for _ in range(0, count):
                x += 1
                coords[x,y] = True
        elif dir == "L":
            for _ in range(0, count):
                x -= 1
                coords[x,y] = True
        elif dir == "U":
            for _ in range(0, count):
                y += 1
                coords[x,y] = True
        elif dir == "D":
            for _ in range(0, count):
                y -= 1
                coords[x,y] = True
    return coords


with open(sys.argv[1]) as f:
    wire1dirs = f.readline().rstrip().split(',')
    wire2dirs = f.readline().rstrip().split(',')

    wire1coords = getcoords(wire1dirs)
    wire2coords = getcoords(wire2dirs)

    intersections = {}

    for k in wire1coords:
        if k in wire2coords:
            intersections[k] = abs(k[0]) + abs(k[1])

    print(sorted(intersections.items(), key=lambda x: x[1])[0][1])