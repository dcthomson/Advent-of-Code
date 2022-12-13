import sys
import string

emap = {}
start = None
end = None

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            emap[(x,y)] = c
            if c == "S":
                start = (x,y)
                emap[(x,y)] = "a"
            if c == "E":
                end = (x,y)
                emap[(x,y)] = "z"
            x += 1

        y += 1

paths = {}

def bfs(visited, emap, node):
    visited.append(node)
    queue = []
    queue.append(node)
    lowcase = string.ascii_lowercase
    paths[node] = []

    steps = 0

    while queue:
        s = queue.pop(0)

        if s == end:
            return len(paths[s])

        x = s[0]
        y = s[1]

        for neighbor in ((x+1,y), (x-1,y), (x,y-1), (x,y+1)):
            if neighbor not in visited:
                if neighbor in emap:
                    if (lowcase.index(emap[neighbor]) <= lowcase.index(emap[s]) + 1):
                        visited.append(neighbor)
                        paths[neighbor] = paths[s].copy()
                        paths[neighbor].append(s)
                        queue.append(neighbor)

        steps += 1

print(bfs([], emap, start))