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
    # print()
    for i in range(0, len(newmap)):
        currmap[i] = newmap[i].copy()

    for y in range(0, len(currmap)):
        # print()
        for x in range(0, len(line)):
            # print(currmap[y][x], end="")
            if currmap[y][x] != ".":
                occupied = 0
                # print("\n", x, y)
                for x2 in range(x - 1, x + 2):
                    for y2 in range(y - 1, y + 2):
                        # print("  ", x2, y2)
                        if x == x2 and y == y2:
                            continue
                        if x2 < 0 or y2 < 0:
                            continue
                        else:
                            try:
                                if currmap[y2][x2] == "#":
                                    # print("occupied + 1")
                                    occupied += 1
                            except:
                                pass
                # print("occupied: ", occupied)
                if currmap[y][x] == "L" and occupied == 0:
                    newmap[y][x] = "#"
                elif currmap[y][x] == "#" and occupied >= 4:
                    newmap[y][x] = "L"

occupied = 0
for line in newmap:
    for x in line:
        if x == "#":
            occupied += 1

print(occupied)