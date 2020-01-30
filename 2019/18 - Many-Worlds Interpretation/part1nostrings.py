# Change to queue
# remove stringify
# remove string funcs

import sys
import string
import collections
import time
import queue

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
                current = (x, y)
            x += 1
        y += 1

keylen = len(keys)

# print(keys)
# print(doors)
# print(maze)

def stringify(node):
    return "%s-%s-%s" % (node[0][0], node[0][1], "".join(node[1]))

longest = 0

t0 = time.time()

visited = {}
Q = queue.Queue()
Q.put((current, "", 0))
while True:
    node = Q.get()
    # print("node:", node)
    steps = node[2]
    keys = node[1]
    coord = node[0]
    # print(steps, coord, keys)
    if (coord, keys) not in visited:
        # print(steps, node)
        visited[(coord, keys)] = steps
        neighbors = []
        for coord in ((coord[0] + 1, coord[1]),
                      (coord[0] - 1, coord[1]),
                      (coord[0], coord[1] + 1),
                      (coord[0], coord[1] - 1)):
            newkeys = False
            if coord in maze:
                if maze[coord] != "#":
                    if maze[coord] in string.ascii_lowercase:
                        if maze[coord] not in keys:
                            newkeys = keys + maze[coord]
                            newkeys = ''.join(sorted(newkeys))
                            # check if done
                            newkeylen = len(newkeys)
                            if newkeylen == keylen:
                                print("DONE:", steps + 1)
                                exit()
                            if newkeylen > longest:
                                print(round(time.time() - t0, 2), steps, newkeys)
                                longest = len(newkeys)
                    elif maze[coord] in string.ascii_uppercase:
                        if maze[coord].lower() not in keys:
                            # found door without key :(
                            continue
                    if newkeys:
                        neighbors.append((coord, newkeys))
                    else:
                        neighbors.append((coord, keys))
        for neighbor in neighbors:
            # print("neighbor:", neighbor)
            Q.put((neighbor[0], neighbor[1], steps + 1))