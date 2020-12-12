import sys

currmap = []
newmap = []

with open(sys.argv[1], "r") as f:
    for line in f:
        newmap.append(list(line.rstrip()))
        currmap.append("")

def samemap(m1, m2):
    if len(m1) != len(m2):
        return False
    for i in range(0, len(m1)):
        if m1[i] != m2[i]:
            return False
    return True

while not samemap(currmap, newmap):
    for i in range(0, len(newmap)):
        currmap[i] = newmap[i].copy()

    for y in range(0, len(currmap)):
        for x in range(0, len(line)):
            if currmap[y][x] != ".":
                occupied = 0
                for x2 in range( -1, 2):
                    for y2 in range(-1, 2):
                        x3 = x
                        y3 = y
                        if x2 == 0 and y2 == 0:
                            continue
                        while True:
                            x3 += x2
                            y3 += y2
                            if x3 < 0 or y3 < 0:
                                break
                            else:
                                try:
                                    if currmap[y3][x3] == "#":
                                        occupied += 1
                                        break
                                    elif currmap[y3][x3] == "L":
                                        break
                                except:
                                    break
                if currmap[y][x] == "L" and occupied == 0:
                    newmap[y][x] = "#"
                elif currmap[y][x] == "#" and occupied >= 5:
                    newmap[y][x] = "L"

occupied = 0
for line in newmap:
    for x in line:
        if x == "#":
            occupied += 1

print(occupied)