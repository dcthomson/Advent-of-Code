import sys

def getcoords(dirs):
    coords = {}
    x = 0
    y = 0
    counter = 1
    for d in dirs:
        dir = d[0]
        count = int(d[1:])
        if dir == "R":
            for _ in range(0, count):
                x += 1
                if not (x,y) in coords:
                    coords[x,y] = counter
                counter += 1
        elif dir == "L":
            for _ in range(0, count):
                x -= 1
                if not (x,y) in coords:
                    coords[x,y] = counter
                counter += 1
        elif dir == "U":
            for _ in range(0, count):
                y += 1
                if not (x,y) in coords:
                    coords[x,y] = counter
                counter += 1
        elif dir == "D":
            for _ in range(0, count):
                y -= 1
                if not (x,y) in coords:
                    coords[x,y] = counter
                counter += 1

    return coords


with open(sys.argv[1]) as f:
    wire1dirs = f.readline().rstrip().split(',')
    wire2dirs = f.readline().rstrip().split(',')

    wire1coords = getcoords(wire1dirs)
    wire2coords = getcoords(wire2dirs)

    intersections = {}

    for k in wire1coords:
        if k in wire2coords:
            intersections[k] = wire1coords[k] + wire2coords[k]

    print(sorted(intersections.items(), key=lambda x: x[1])[0][1])