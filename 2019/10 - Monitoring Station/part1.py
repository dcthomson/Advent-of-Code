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
        if a[1] < b[1] < c[1]:
            return b
        elif c[1] < b[1] < a[1]:
            return b
        elif b[1] < a[1] < c[1]:
            return a
        elif c[1] < a[1] < b[1]:
            return a
        elif a[1] < c[1] < b[1]:
            return c
        elif b[1] < c[1] < a[1]:
            return c
    else:
        if a[0] < b[0] < c[0]:
            return b
        elif c[0] < b[0] < a[0]:
            return b
        elif b[0] < a[0] < c[0]:
            return a
        elif c[0] < a[0] < b[0]:
            return a
        elif a[0] < c[0] < b[0]:
            return c
        elif b[0] < c[0] < a[0]:
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
        print(ast[0], ast[1], ast[2])
        print(get_middle(ast[0], ast[1], ast[2]))
        mid = get_middle(ast[0], ast[1], ast[2])
        if mid == ast[0]:
            if ast[1] not in asteroidblindspots:
                asteroidblindspots[ast[1]] = []
            asteroidblindspots[ast[1]].append(ast[2])
            if ast[2] not in asteroidblindspots:
                asteroidblindspots[ast[2]] = []
            asteroidblindspots[ast[2]].append(ast[1])
        elif mid == ast[1]:
            if ast[0] not in asteroidblindspots:
                asteroidblindspots[ast[0]] = []
            asteroidblindspots[ast[0]].append(ast[2])
            if ast[2] not in asteroidblindspots:
                asteroidblindspots[ast[2]] = []
            asteroidblindspots[ast[2]].append(ast[0])
        elif mid == ast[2]:
            if ast[1] not in asteroidblindspots:
                asteroidblindspots[ast[1]] = []
            asteroidblindspots[ast[1]].append(ast[0])
            if ast[0] not in asteroidblindspots:
                asteroidblindspots[ast[0]] = []
            asteroidblindspots[ast[0]].append(ast[1])

asteroidcount = len(asteroidblindspots)
bestasteroidcount = 0

for k, v in asteroidblindspots.items():
    if asteroidcount - len(v) > bestasteroidcount:
        bestasteroidcount = asteroidcount - len(v)

print(bestasteroidcount)