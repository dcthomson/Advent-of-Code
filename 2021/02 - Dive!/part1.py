import sys

horizontalpos = 0
depth = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        (direction, dist) = line.split(" ")
        dist = int(dist)
        if direction == "forward":
            horizontalpos += dist
        elif direction == "up":
            depth -= dist
        elif direction == "down":
            depth += dist

print(horizontalpos * depth)