import sys
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



for ast in combinations(asteroids, 3):
    if is_line(ast[0], ast[1], ast[2]):
        # print(ast[0], ast[1], ast[2])
        # print(get_middle(ast[0], ast[1], ast[2]))
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
# print(asteroidcount)
bestasteroidcount = 0
bestasteroid = (-1,-1)

for k, v in asteroidblindspots.items():
    if asteroidcount - len(v) > bestasteroidcount:
        bestasteroidcount = asteroidcount - len(v) - 1
        bestasteroid = k

print(bestasteroid, bestasteroidcount)