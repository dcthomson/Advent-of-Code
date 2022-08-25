import sys

minx = miny = maxx = maxy = 0
image = dict()
enhancealg = ""

with open(sys.argv[1], "r") as f:
    blanklinefound = False
    y = 0
    for line in f:
        if not blanklinefound:
            if line[0] != "#" and line[0] != ".":
                blanklinefound = True
            else:
                enhancealg = line.rstrip()
        else:
            x = 0
            for c in line.rstrip():
                image[(x, y)] = c
                maxx = x
                x += 1
            maxy = y
            y += 1

#print(enhancealg)
#print(image)
#print(maxx, maxy)

def getboundries(image):
    minx = miny = maxx = maxy = None
    for coord in image:
        if minx is None:
            minx = coord[0]
        if miny is None:
            miny = coord[1]
        if maxx is None:
            maxx = coord[0]
        if maxy is None:
            maxy = coord[1]
        if coord[0] < minx:
            minx = coord[0]
        if coord[1] < miny:
            miny = coord[1]
        if coord[0] > maxx:
            maxx = coord[0]
        if coord[1] > maxy:
            maxy = coord[1]
    return (minx, miny, maxx, maxy)

def printimage(image):
    (minx, miny, maxx, maxy) = getboundries(image)
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(image[(x, y)], end="")
        print()

def countlit(image):
    count = 0
    for pixel in image.values():
        if pixel == "#":
            count += 1
    return count

printimage(image)
print(countlit(image))
print()

for _ in range(0,2):

    newimage = {}
    (minx, miny, maxx, maxy) = getboundries(image)
    newxmin = minx - 1
    newymin = miny - 1
    newxmax = maxx + 1
    newymax = maxy + 1
    for y in range(miny - 1, maxy + 2):
        for x in range(minx - 1, maxx + 2):
            pixel = ""
            for lily in range(-1, 2):
                for lilx in range(-1, 2):
                    if (x + lilx, y + lily) not in image:
                        pixel += "0"
                    else:
                        c = image[(x + lilx, y + lily)]
                        if c == "#":
                            pixel += "1"
                        elif c == ".":
                            pixel += "0"

            newimage[(x, y)] = enhancealg[int(pixel, 2)]

    image = newimage.copy()
    printimage(image)
    print(countlit(image))
    print()
    print(getboundries(image))
print(countlit(image))