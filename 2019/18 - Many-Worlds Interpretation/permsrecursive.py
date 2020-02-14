import string

import sys
import string
import queue
from itertools import combinations

maze = {}
doors = {}
keys = {}
current = None

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            maze[(x, y)] = c
            if c in string.ascii_lowercase:
                keys[c] = (x, y)
            elif c in string.ascii_uppercase:
                doors[c] = (x, y)
            x += 1
        y += 1

current = "@"

numkeys = len(keys)

lowers = list(keys.keys())
lowers.append("@")

routes = {}

def stringify(coord, steps=0, intheway=list()):
    if intheway:
        return ("%s-%s-%s-%s") % (coord[0], coord[1], steps, intheway)
    else:
        return ("%s-%s-%s-") % (coord[0], coord[1], steps)

farthestdistance = 0

for letter in string.ascii_lowercase:
    if letter in keys:
        routes[letter] = {}
        Q = [stringify(keys[letter])]
        visited = [keys[letter]]
        while Q and len(routes[letter]) < len(keys):
            node = Q.pop(0)
            (x, y, steps, intheway) = node.split("-")
            x = int(x)
            y = int(y)
            steps = int(steps)
            neighbors = []
            for coord in ((x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1)):
                if coord in maze and coord not in visited:
                    if maze[coord] != "#":
                        if maze[coord] in string.ascii_lowercase or maze[coord] == "@":
                            if maze[coord] != letter:
                                alreadyhave = False
                                for v in routes[letter].values():
                                    if maze[coord] in v[1]:
                                        alreadyhave = True
                                        break
                                if not alreadyhave:
                                    if steps + 1 > farthestdistance:
                                        farthestdistance = steps + 1
                                    routes[letter][maze[coord]] = (steps + 1, intheway)
                                    if maze[coord] not in routes:
                                        routes[maze[coord]] = {}
                                    routes[maze[coord]][letter] = (steps + 1, intheway)
                                newintheway = intheway + maze[coord]
                        elif maze[coord] in string.ascii_uppercase:
                            newintheway = intheway + maze[coord]
                        else:
                            newintheway = intheway

                        neighbors.append(stringify(coord, steps + 1, newintheway))
            for neighbor in neighbors:
                Q.append(neighbor)
                (x, y, steps, intheway) = neighbor.split("-")
                x = int(x)
                y = int(y)
                visited.append((x, y))

for k, v in routes.items():
    print()
    print(k)
    for k2, v2 in v.items():
        print("  ", k2 + ": ", end='')
        print(v2)



loweststeps = False

keys = "@"

def addletter(keys, steps, loweststeps):
    if not loweststeps or steps < loweststeps:
        if len(keys) == len(lowers):
            print(keys, steps)
            return steps
        else:
            current = keys[-1]
            for destination in lowers:
                if destination not in keys:
                    # let's check if anything is in the way
                    somethinginway = False
                    for intheway in routes[current][destination][1]:
                        if intheway.lower() not in keys:
                            somethinginway = True
                            break

                    if not somethinginway:
                        newsteps = steps + routes[current][destination][0]
                        loweststeps = addletter(keys + destination, 
                                                newsteps, 
                                                loweststeps)
    return loweststeps

print(addletter("@", 0, loweststeps))