import sys
import string

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

print(keys)
print(doors)
print(maze)
            

visited = {}
Q = [current]
while Q:
    node = Q.pop(0)
    if node not in visited:
        print(node)
        visited[node] 
        nodecoord = node[0]
        newkeys = False
        neighbors = []
        for coord in ((nodecoord[0] + 1, nodecoord[1]),
                      (nodecoord[0] - 1, nodecoord[1]),
                      (nodecoord[0], nodecoord[1] + 1),
                      (nodecoord[0], nodecoord[1] - 1)):
            if coord in maze:
                if maze[coord] != "#":
                    if maze[coord] == ".":
                        pass
                    if maze[coord] in string.ascii_lowercase:
                        if maze[coord] not in node[1]:
                            newkeys = node[1].copy()
                            newkeys.append(maze[coord])
                            newkeys.sort()
                    elif maze[coord] in string.ascii_uppercase:
                        if maze[coord].lower() not in node[1]:
                            # found door without key :(
                            continue
                if newkeys:
                    neighbors.append((coord, newkeys))
                else:
                    neighbors.append((coord, node[1]))
        for neighbor in neighbors:
            Q.append(neighbor)