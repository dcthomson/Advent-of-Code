import sys

lightgrid = dict()

for x in range(0, 1000):
    for y in range(0, 1000):
        lightgrid[(x,y)] = False

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        (first, second) = line.split(" through ")
        first = first.split(" ")[-1]
        (fx, fy) = list(map(int, first.split(",")))
        (sx, sy) = list(map(int, second.split(",")))
        if line.startswith("turn"):
            if line.split(" ")[1] == "on":
                for x in range(fx, sx + 1):
                    for y in range(fy, sy + 1):
                        lightgrid[(x, y)] = True
            else:
                for x in range(fx, sx + 1):
                    for y in range(fy, sy + 1):
                        lightgrid[(x, y)] = False
        if line.startswith("toggle"):
            for x in range(fx, sx + 1):
                for y in range(fy, sy + 1):
                    if lightgrid[(x, y)]:
                        lightgrid[(x, y)] = False
                    else:
                        lightgrid[(x, y)] = True

lit = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if lightgrid[(x,y)]:
            lit += 1

print(lit)