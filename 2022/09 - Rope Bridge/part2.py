import sys

def printrope(rope):

    minx = maxx = miny = maxy = 0

    for segment in rope:
        x = segment[0]
        y = segment[1]
        if x > maxx:
            maxx = x
        elif x < minx:
            minx = x
        elif y > maxy:
            maxy = y
        elif y < miny:
            miny = y

        for y in range(miny, maxy+1):
            for x in range(minx, maxx+1):
                for i in range(0, 10):
                    if rope[i] == (x,y):
                        if i == 0:
                            print("H", end="")
                            break
                        else:
                            print(i, end="")
                            break
            print()

with open(sys.argv[1], "r") as f:

    rope = []
    for i in range(0, 10):
        rope.append((0,0))

    dirs = {"R": (1,0),
            "L": (-1,0),
            "U": (0,1),
            "D": (0,-1)}

    x = y = 0

    visited = {}

    for line in f:
        line = line.strip()

        (dir, steps) = line.split()

        for _ in range(0, int(steps)):
            for i in range(0,9):
                if i == 0:
                    x = rope[i][0] + dirs[dir][0]
                    y = rope[i][1] + dirs[dir][1]
                else:
                    x = rope[i][0]
                    y = rope[i][1]
                print(x,y,rope)
                if abs(x - rope[i + 1][0]) >= 2 or abs(y - rope[i + 1][1]) >= 2:
                    rope[i + 1] = rope[i]
                rope[i] = (x,y)
            if rope[9] not in visited:
                visited[rope[9]] = True
            printrope(rope)

print(len(visited))