import sys
import string
from itertools import combinations, permutations

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

lowers = list(keys.values())
lowers.append("@")

routes = {}

def stringify(coord, steps=0, doors=list()):
    if doors:
        return ("%s-%s-%s-%s") % (coord[0], coord[1], steps, doors)
    else:
        return ("%s-%s-%s-") % (coord[0], coord[1], steps)

for letter in string.ascii_lowercase:
    if letter in keys:
        routes[letter] = {}
        Q = [stringify(keys[letter])]
        visited = [keys[letter]]
        while Q and len(routes[letter]) < len(keys):
            node = Q.pop(0)
            (x, y, steps, doors) = node.split("-")
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
                                for k, v in routes[letter].items():
                                    if maze[coord] in v[1]:
                                        alreadyhave = True
                                        break
                                if not alreadyhave:
                                    routes[letter][maze[coord]] = (steps + 1, doors)
                                    if maze[coord] not in routes:
                                        routes[maze[coord]] = {}
                                    routes[maze[coord]][letter] = (steps + 1, doors)
                        if maze[coord] in string.ascii_uppercase:
                            newdoors = doors + maze[coord]
                        else:
                            newdoors = doors
                        neighbors.append(stringify(coord, steps + 1, newdoors))
            for neighbor in neighbors:
                Q.append(neighbor)
                (x, y, steps, doors) = neighbor.split("-")
                x = int(x)
                y = int(y)
                visited.append((x, y))


shortest = False

