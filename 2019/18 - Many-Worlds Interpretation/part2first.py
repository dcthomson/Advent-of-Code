import sys
import string
import time
import queue

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
                keys[(x, y)] = c
            elif c in string.ascii_uppercase:
                doors[(x,y)] = c
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
        if smallx is None:
            smallx = robot[0]
        else:
            if robot[0] < smallx:
                smallx = robot[0]
        if smally is None:
            smally = robot[1]
        else:
            if robot[1] < smally:
                smally = robot[1]
    mid = (smallx + 1, smally + 1)
        

r1 = robots[0]
r2 = robots[1]
r3 = robots[2]
r4 = robots[3]

keylen = len(keys)

longest = 0

t0 = time.time()

visited = {}
Q = queue.Queue()
Q.put((r1, r2, r3, r4, "", 0))
while True:
    node = Q.get()
    # print("Q, visited:", Q.qsize(), len(visited))
    # print("node:", node)
    steps = node[5]
    keys = node[4]
    # order = node[6]
    r = [node[0], node[1], node[2], node[3]]
    for i in (0, 1, 2, 3):
        if (r[i], keys) not in visited or steps <= visited[(r[i], keys)]:
            visited[(r[i], keys)] = steps

            neighbors = []
            for coord in ((r[i][0] + 1, r[i][1]),
                          (r[i][0] - 1, r[i][1]),
                          (r[i][0], r[i][1] + 1),
                          (r[i][0], r[i][1] - 1)):
                newkeys = False
                if coord in maze:
                    if maze[coord] != "#":
                        if maze[coord] in string.ascii_lowercase:
                            if maze[coord] not in keys:

                                # keys = ''.join(sorted(keys))

                                newkeys = keys + maze[coord]

                                # check if done
                                newkeylen = len(newkeys)
                                if newkeylen > longest:
                                    missing = ""
                                    for c in string.ascii_lowercase:
                                        if c not in newkeys:
                                            missing += c
                                    print(round(time.time() - t0, 2), steps, newkeys, missing, Q.qsize(), len(visited))
                                    longest = len(newkeys)

                                if newkeylen == keylen:
                                    print("DONE:", steps + 1)
                                    sys.exit()
                        elif maze[coord] in string.ascii_uppercase:
                            if maze[coord].lower() not in keys:
                                # found door without key :(
                                continue
                        if newkeys:
                            if i == 0:
                                neighbors.append((coord, r[1], r[2], r[3], newkeys))
                            elif i == 1:
                                neighbors.append((r[0], coord, r[2], r[3], newkeys))
                            elif i == 2:
                                neighbors.append((r[0], r[1], coord, r[3], newkeys))
                            elif i == 3:
                                neighbors.append((r[0], r[1], r[2], coord, newkeys))
                        else:
                            if i == 0:
                                neighbors.append((coord, r[1], r[2], r[3], keys))
                            elif i == 1:
                                neighbors.append((r[0], coord, r[2], r[3], keys))
                            elif i == 2:
                                neighbors.append((r[0], r[1], coord, r[3], keys))
                            elif i == 3:
                                neighbors.append((r[0], r[1], r[2], coord, keys))
        
                # print(neighbors)
            for n in neighbors:
                # print("neighbor:", neighbor)
                Q.put((n[0], n[1], n[2], n[3], n[4], steps + 1))