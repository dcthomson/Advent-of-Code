import sys

aim = 0
horizontalpos = 0
depth = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        (direction, dist) = line.split(" ")
        dist = int(dist)
        if direction == "forward":
            horizontalpos += dist
            depth += aim * dist
        elif direction == "up":
            aim -= dist
        elif direction == "down":
            aim += dist

print(horizontalpos * depth)