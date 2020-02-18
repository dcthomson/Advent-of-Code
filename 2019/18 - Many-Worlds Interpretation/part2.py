import sys
import string
from collections import deque

maze = {}
doors = {}
keys = {}
current = None
robots = []


with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            maze[(x, y)] = c
            if c in string.ascii_lowercase:
                keys[c] = (x, y)
            elif c in string.ascii_uppercase:
                doors[c] = (x,y)
            elif c == "@":
                robots.append((x, y))
            x += 1
        y += 1

mid = False

if len(robots) == 1:
    mid = robots[0]
    maze[mid] = "#"
    maze[(mid[0] + 1, mid[1])] = "#"
    maze[(mid[0] - 1, mid[1])] = "#"
    maze[(mid[0], mid[1] + 1)] = "#"
    maze[(mid[0], mid[1] - 1)] = "#"
    maze[(mid[0] + 1, mid[1] + 1)] = "."
    maze[(mid[0] - 1, mid[1] + 1)] = "."
    maze[(mid[0] + 1, mid[1] - 1)] = "."
    maze[(mid[0] - 1, mid[1] - 1)] = "."
    robots.pop()
    robots.append((mid[0] - 1, mid[1] - 1))
    robots.append((mid[0] + 1, mid[1] - 1))
    robots.append((mid[0] - 1, mid[1] + 1))
    robots.append((mid[0] + 1, mid[1] + 1))
else:
    smallx = None
    smally = None
    for robot in robots:
        if smallx is None or robot[0] < smallx:
            smallx = robot[0]
        if smally is None or robot[1] < smally:
            smally = robot[1]

    mid = (smallx + 1, smally + 1)

r1 = robots[0]
r2 = robots[1]
r3 = robots[2]
r4 = robots[3]

maze[r1] = "r1"
maze[r2] = "r2"
maze[r3] = "r3"
maze[r4] = "r4"

keys["r1"] = r1
keys["r2"] = r2
keys["r3"] = r3
keys["r4"] = r4

numkeys = len(keys)

# lowers = list(keys.values())
# lowers.append("@")

routes = {}

def stringify(coord, steps=0, intheway=list()):
    if intheway:
        return ("%s-%s-%s-%s") % (coord[0], coord[1], steps, intheway)
    else:
        return ("%s-%s-%s-") % (coord[0], coord[1], steps)

for letter in keys:
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

# for k, v in routes.items():
#     print()
#     print(k)
#     for k2, v2 in v.items():
#         print("  ", k2 + ": ", end='')
#         print(v2)

# for k, v in sorted(routes[current].items(), key=lambda x:x[1][0], reverse=True):
#     print(k, v)


keycoords = keys

shortest = False
longest = 0
Q = deque()
Q.append((0, ["r1", "r2", "r3", "r4"], ["r1", "r2", "r3", "r4"]))
visited = {}
while Q:
    node = Q.pop()
    
    steps = int(node[0])
    keys = node[1]
    current = node[2]
    if shortest and steps > shortest:
        continue

    justmoved = keys[-1]
    found = False
    for v in routes.values():
        if justmoved in v:
            for i in (0, 1, 2, 3):
                if current[i] in v:
                    current[i] = justmoved
                    found = True
                    break
            if found:
                break
    # print("\n", len(Q), current, node)

    # keysstr = ''.join(keys)
    keysstr = ''.join(sorted(keys))

    if (current[0], current[1], current[2], current[3], keysstr) in visited:
        if steps >= visited[(current[0], current[1], current[2], current[3], keysstr)]:
            continue
    visited[(current[0], current[1], current[2], current[3], keysstr)] = steps

    if len(keys) == numkeys:
        if not shortest or steps < shortest:
            shortest = steps
            # print(shortest, keys)

    for i in (0, 1, 2, 3):
        # for k, v in sorted(routes[curr].items(), key=lambda x:x[1][0], reverse=True):
            # print(k, v)
        for k, v in routes[current[i]].items():
            if k in keys:
                continue
            somethinginway = False
            for intheway in v[1]:
                if intheway.lower() not in keys:
                    somethinginway = True
                    break
                    
            if not somethinginway:
                newkeys = keys + [k]
                # print("appending:", newkeys)
                newcurrent = current.copy()
                newcurrent[i] = k
                Q.append(((steps + int(v[0]), newkeys, newcurrent)))


print(shortest)