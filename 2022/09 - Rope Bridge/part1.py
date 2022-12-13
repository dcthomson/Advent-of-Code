import sys

with open(sys.argv[1], "r") as f:

    head = tail = (0,0)

    dirs = {"R": (1,0),
            "L": (-1,0),
            "U": (0,1),
            "D": (0,-1)}

    x = y = 0

    visited = {}

    for line in f:
        line = line.strip()

        (dir, steps) = line.split()

        for i in range(0, int(steps)):
            x = head[0] + dirs[dir][0]
            y = head[1] + dirs[dir][1]
            if abs(x - tail[0]) >= 2 or abs(y - tail[1]) >= 2:
                tail = head
            head = (x,y)
            if tail not in visited:
                visited[tail] = True

print(len(visited))