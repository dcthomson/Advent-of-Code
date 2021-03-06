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

lowers = list(keys.values())
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

# for k, v in sorted(routes[current].items(), key=lambda x:x[1][0], reverse=True):
#     print(k, v)

# exit()

shortest = False
longest = 0
Q = [(0, ["@"])]
totalsteps = 0
while Q:
    totalsteps += 1
    print(totalsteps, len(Q))
    Q.sort()
    toremove = []
    i = 0
    for node in Q:
        steps = int(node[0])
        keys = node[1]
        if steps > totalsteps + farthestdistance:
            break
        if steps < totalsteps - farthestdistance:
            toremove.append(i)
        # print(shortest, len(Q), len(keys), steps)
        # if shortest:
        #     if steps >= shortest:
        #         continue
        if len(keys) > longest:
            print("longest:", steps, keys)
            longest = len(keys)
        if len(keys) == numkeys + 1:
            if shortest:
                if steps <= shortest:
                    shortest = steps
                    print(shortest, keys)
            else:
                shortest = steps
                print(shortest, keys)
            print("totalsteps:", totalsteps)
            sys.exit()
        current = keys[-1]
        # for k, v in sorted(routes[current].items(), key=lambda x:x[1][0], reverse=True):
            # print(k, v)
        for k, v in routes[current].items():
            # if shortest:
            #     if int(v[0]) >= shortest:
            #         continue
            if int(v[0]) + steps != totalsteps:
                continue
            if k in keys:
                # print("Continuing")
                continue
            doorinway = False
            untraversedkey = False
            for intheway in v[1]:
                if intheway.isupper():
                    # door
                    if intheway.lower() not in keys:
                        doorinway = True
                        break
                else:
                    # key or start
                    if intheway not in keys:
                        untraversedkey = True
                        break
                    
            if not doorinway and not untraversedkey:
                # print("keys:", keys)
                newkeys = keys + [k]
                # print("newkeys:", newkeys)
                Q.append(((steps + int(v[0]), newkeys)))
        i += 1
    for i in sorted(toremove, reverse=True):
        del Q[i]


print(shortest)
print(totalsteps)