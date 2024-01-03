import sys

x = 0
y = 0
xmin = xmax = ymin = ymax = 0

grid = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (direction, distance, _) = line.split()

        distance = int(distance)

        if direction == "R":
            for i in range(0, distance):
                x += 1
                if x < xmin:
                    xmin = x
                elif x > xmax:
                    xmax = x
                grid[x,y] = "#"
        elif direction == "L":
            for i in range(0, distance):
                x -= 1
                if x < xmin:
                    xmin = x
                elif x > xmax:
                    xmax = x
                grid[x,y] = "#"
        elif direction == "U":
            for i in range(0, distance):
                y -= 1
                if y < ymin:
                    ymin = y
                elif y > ymax:
                    ymax = y
                grid[x,y] = "#"
        elif direction == "D":
            for i in range(0, distance):
                y += 1
                if y < ymin:
                    ymin = y
                elif y > ymax:
                    ymax = y
                grid[x,y] = "#"

for y in range(ymin, ymax + 1):
    for x in range(xmin, xmax + 1):
        if (x,y) in grid:
            print(grid[x,y], end="")
        else:
            print(".", end="")
    print()
print(len(grid))