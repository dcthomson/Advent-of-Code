# Change to queue
# remove stringify
# remove string funcs

import sys
import string
import collections
import time

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
                keys[(x, y)] = c
            elif c in string.ascii_uppercase:
                doors[(x,y)] = c
            elif c == "@":
                current = ((x, y), [])
            x += 1
        y += 1

# print(keys)
# print(doors)
# print(maze)

def stringify(node):
    return "%s-%s-%s" % (node[0][0], node[0][1], "".join(node[1]))

longest = 0

t0 = time.time()

visited = []
Q = collections.OrderedDict()
Q[stringify(current)] = 1
while Q:
    node = Q.popitem(last=False)
    steps = node[1]
    node = node[0]
    if node not in visited:
        # print(steps, node)
        visited.append(node)
        nodelist = node.split("-") 
        nodecoord = (int(nodelist[0]), int(nodelist[1]))
        nodekeys = list(nodelist[2])
        neighbors = []
        for coord in ((nodecoord[0] + 1, nodecoord[1]),
                      (nodecoord[0] - 1, nodecoord[1]),
                      (nodecoord[0], nodecoord[1] + 1),
                      (nodecoord[0], nodecoord[1] - 1)):
            newkeys = False
            if coord in maze:
                if maze[coord] != "#":
                    if maze[coord] in string.ascii_lowercase:
                        if maze[coord] not in nodekeys:
                            newkeys = nodekeys.copy()
                            newkeys.append(maze[coord])
                            newkeys.sort()
                            # check if done
                            if len(newkeys) == len(keys):
                                print("DONE:", steps)
                                exit()
                            if len(newkeys) > longest:
                                print(round(time.time() - t0, 2), steps, newkeys)
                                longest = len(newkeys)
                    elif maze[coord] in string.ascii_uppercase:
                        if maze[coord].lower() not in nodekeys:
                            # found door without key :(
                            continue
                    if newkeys:
                        neighbors.append((coord, newkeys))
                    else:
                        neighbors.append((coord, nodekeys))
        for neighbor in neighbors:
            Q[stringify(neighbor)] = steps + 1