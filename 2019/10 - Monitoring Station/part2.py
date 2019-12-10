import sys
import math
from itertools import combinations
map = {}

def is_line(a, b, c):
    # if area of triangle is 0 then it's a line
    if a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]):
        return False
    else:
        return True

def get_middle(a, b, c):
    if a[0] == b[0] == c[0]:
        xy = 1
    else:
        xy = 0
    if a[xy] < b[xy] < c[xy]:
        return b
    elif c[xy] < b[xy] < a[xy]:
        return b
    elif b[xy] < a[xy] < c[xy]:
        return a
    elif c[xy] < a[xy] < b[xy]:
        return a
    elif a[xy] < c[xy] < b[xy]:
        return c
    elif b[xy] < c[xy] < a[xy]:
        return c

def get_distance(a, b):
    # print(a, b)
    xsquared = (a[0] - b[0]) * (a[0] - b[0])
    ysquared = (a[1] - b[1]) * (a[1] - b[1])
    return math.sqrt(abs(xsquared + ysquared))


asteroids = []

asteroidblindspots = {}

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            if c == "#":
                asteroids.append((x,y))
            x += 1
        y += 1


# set asteroid blind spots
for ast in combinations(asteroids, 3):
    if is_line(ast[0], ast[1], ast[2]):
        mid = get_middle(ast[0], ast[1], ast[2])
        if mid == ast[0]:
            if ast[1] not in asteroidblindspots:
                asteroidblindspots[ast[1]] = {}
            asteroidblindspots[ast[1]][ast[2]] = True
            if ast[2] not in asteroidblindspots:
                asteroidblindspots[ast[2]] = {}
            asteroidblindspots[ast[2]][ast[1]] = True
        elif mid == ast[1]:
            if ast[0] not in asteroidblindspots:
                asteroidblindspots[ast[0]] = {}
            asteroidblindspots[ast[0]][ast[2]] = True
            if ast[2] not in asteroidblindspots:
                asteroidblindspots[ast[2]] = {}
            asteroidblindspots[ast[2]][ast[0]] = True
        elif mid == ast[2]:
            if ast[1] not in asteroidblindspots:
                asteroidblindspots[ast[1]] = {}
            asteroidblindspots[ast[1]][ast[0]] = True
            if ast[0] not in asteroidblindspots:
                asteroidblindspots[ast[0]] = {}
            asteroidblindspots[ast[0]][ast[1]] = True

asteroidcount = len(asteroidblindspots)
bestasteroidcount = 0
bestasteroid = None

for k, v in asteroidblindspots.items():
    if asteroidcount - len(v) > bestasteroidcount:
        bestasteroidcount = asteroidcount - len(v) - 1
        bestasteroid = k

rasteroidsbyangle = {}
lasteroidsbyangle = {}
uasteroidsbyangle = []
dasteroidsbyangle = []
rinlineasteroidsbyangle = []
linlineasteroidsbyangle = []
for asteroid in asteroids:
    if asteroid != bestasteroid:
        # print(asteroid, bestasteroid, end="")
        try:
            angle = (asteroid[0] - bestasteroid[0]) / (asteroid[1] - bestasteroid[1])
            if angle == 0:
                if asteroid[1] < bestasteroid[1]:
                    uasteroidsbyangle.append(asteroid)
                else:
                    dasteroidsbyangle.append(asteroid)
        except:
            if asteroid[0] < bestasteroid[0]:
                linlineasteroidsbyangle.append(asteroid)
            else:
                rinlineasteroidsbyangle.append(asteroid)
            # print()
            continue
        if asteroid[0] < bestasteroid[0]:
            if angle not in lasteroidsbyangle:
                lasteroidsbyangle[angle] = []
            lasteroidsbyangle[angle].append(asteroid)
        if asteroid[0] > bestasteroid[0]:
            if angle not in rasteroidsbyangle:
                rasteroidsbyangle[angle] = []
            rasteroidsbyangle[angle].append(asteroid)
        
        # print(" ", angle)

lastremoved = None

asteroidsleft = asteroids

asteroidsdestroyed = 0

while len(asteroidsleft) >= 1 and asteroidsdestroyed < 200:
    # print("ASTEROIDSLEFT: ", len(asteroidsleft))
    # print("U:", uasteroidsbyangle)
    # print()
    # print("R:", rasteroidsbyangle)
    # print()
    # print("RIN", rinlineasteroidsbyangle)
    # print()
    # print("D:", dasteroidsbyangle)
    # print()
    # print("L:", lasteroidsbyangle)
    # print()
    # print("LIN", linlineasteroidsbyangle)
    # print("\n")

    # STRAIGHT UP
    # print(uasteroidsbyangle)
    if len(uasteroidsbyangle):
        closest = None
        closestdist = None
        for asteroid in uasteroidsbyangle:
            dist = get_distance(asteroid, bestasteroid)
            # print(asteroid, dist)
            if closest is None:
                closest = asteroid
                closestdist = dist
            elif dist < closestdist:
                closest = asteroid
                closestdist = dist
        lastremoved = closest
        uasteroidsbyangle.remove(closest)
        asteroidsdestroyed += 1
        if asteroidsdestroyed == 200:
            print(lastremoved[0] * 100 + lastremoved[1])
        # print(lastremoved)

    # UP RIGHT
    for k in sorted(rasteroidsbyangle, reverse=True):
        if k < 0:
            if len(rasteroidsbyangle[k]):
                closest = None
                closestdist = None
                for asteroid in rasteroidsbyangle[k]:
                    dist = get_distance(asteroid, bestasteroid)
                    if closest is None:
                        closest = asteroid
                        closestdist = dist
                    elif dist < closestdist:
                        closest = asteroid
                        closestdist = dist
                lastremoved = closest
                # print("\n")
                # print(k, rasteroidsbyangle)
                rasteroidsbyangle[k].remove(closest)
                asteroidsdestroyed += 1
                if asteroidsdestroyed == 200:
                    print(lastremoved[0] * 100 + lastremoved[1])
    
    # RIGHT
    if len(rinlineasteroidsbyangle):
        closest = None
        closestdist = None
        for asteroid in rinlineasteroidsbyangle:
            dist = get_distance(asteroid, bestasteroid)
            # print(asteroid, dist)
            if closest is None:
                closest = asteroid
                closestdist = dist
            elif dist < closestdist:
                closest = asteroid
                closestdist = dist
        lastremoved = closest
        rinlineasteroidsbyangle.remove(closest)
        asteroidsdestroyed += 1
        if asteroidsdestroyed == 200:
            print(lastremoved[0] * 100 + lastremoved[1])

    # DOWN RIGHT
    for k in sorted(rasteroidsbyangle, reverse=True):
        if k > 0:
            if len(rasteroidsbyangle[k]):
                closest = None
                closestdist = None
                for asteroid in rasteroidsbyangle[k]:
                    dist = get_distance(asteroid, bestasteroid)
                    if closest is None:
                        closest = asteroid
                        closestdist = dist
                    elif dist < closestdist:
                        closest = asteroid
                        closestdist = dist
                lastremoved = closest
                rasteroidsbyangle[k].remove(closest)
                asteroidsdestroyed += 1
                if asteroidsdestroyed == 200:
                    print(lastremoved[0] * 100 + lastremoved[1])


    # STRAIGHT DOWN
    if len(dasteroidsbyangle):
        closest = None
        closestdist = None
        for asteroid in dasteroidsbyangle:
            dist = get_distance(asteroid, bestasteroid)
            if closest is None:
                closest = asteroid
                closestdist = dist
            elif dist < closestdist:
                closest = asteroid
                closestdist = dist
        lastremoved = closest
        dasteroidsbyangle.remove(closest)
        asteroidsdestroyed += 1
        print(lastremoved[0] * 100 + lastremoved[1])

    # DOWN LEFT
    for k in sorted(lasteroidsbyangle, reverse=True):
        if k < 0:
            if len(lasteroidsbyangle[k]):
                closest = None
                closestdist = None
                for asteroid in lasteroidsbyangle[k]:
                    dist = get_distance(asteroid, bestasteroid)
                    if closest is None:
                        closest = asteroid
                        closestdist = dist
                    elif dist < closestdist:
                        closest = asteroid
                        closestdist = dist
                lastremoved = closest
                lasteroidsbyangle[k].remove(closest)
                asteroidsdestroyed += 1
                if asteroidsdestroyed == 200:
                    print(lastremoved[0] * 100 + lastremoved[1])
    
    # LEFT
    if len(linlineasteroidsbyangle):
        closest = None
        closestdist = None
        for asteroid in linlineasteroidsbyangle:
            dist = get_distance(asteroid, bestasteroid)
            # print(asteroid, dist)
            if closest is None:
                closest = asteroid
                closestdist = dist
            elif dist < closestdist:
                closest = asteroid
                closestdist = dist
        lastremoved = closest
        linlineasteroidsbyangle.remove(closest)
        asteroidsdestroyed += 1
        if asteroidsdestroyed == 200:
            print(lastremoved[0] * 100 + lastremoved[1])

    # DOWN RIGHT
    for k in sorted(lasteroidsbyangle, reverse=True):
        if k > 0:
            if len(lasteroidsbyangle[k]):
                closest = None
                closestdist = None
                for asteroid in lasteroidsbyangle[k]:
                    dist = get_distance(asteroid, bestasteroid)
                    if closest is None:
                        closest = asteroid
                        closestdist = dist
                    elif dist < closestdist:
                        closest = asteroid
                        closestdist = dist
                lastremoved = closest
                lasteroidsbyangle[k].remove(closest)
                asteroidsdestroyed += 1
                if asteroidsdestroyed == 200:
                    print(lastremoved[0] * 100 + lastremoved[1])
    
    asteroidsleft = []
    for k in rasteroidsbyangle:
        for a in rasteroidsbyangle[k]:
            asteroidsleft.append(a)
    for k in lasteroidsbyangle:
        for a in lasteroidsbyangle[k]:
            asteroidsleft.append(a)
    asteroidsleft += uasteroidsbyangle
    asteroidsleft += dasteroidsbyangle
    asteroidsleft += linlineasteroidsbyangle
    asteroidsleft += rinlineasteroidsbyangle