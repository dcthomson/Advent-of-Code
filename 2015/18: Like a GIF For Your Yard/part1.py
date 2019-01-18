import sys

lights = dict()

with open(sys.argv[1], 'r') as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            lights[(x, y)] = c
            x += 1
        y += 1

for i in range(0, 100):
    nextlights = dict()
    y = 0
    while y < 100:
        x = 0
        while x < 100:
            on = 0
            for y2 in range(-1, 2):
                for x2 in range(-1, 2):
                    if x2 != 0 or y2 != 0:
                        try:
                            if lights[(x + x2, y + y2)] == "#":
                                on += 1
                        except KeyError:
                            pass
            if on == 3:
                nextlights[(x, y)] = "#"
            elif on == 2 and lights[(x, y)] == "#":
                nextlights[(x, y)] = "#"
            else:
                nextlights[(x, y)] = "."
            x += 1
        y += 1
    lights = nextlights

totalon = 0
for coord in lights:
    if lights[coord] == "#":
        totalon += 1
print(totalon)