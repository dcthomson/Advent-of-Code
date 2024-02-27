import sys

def printrope(rope):

    minx = maxx = miny = maxy = 0
    print()
    print(rope)

    for segment in rope:
        x = segment[0]
        y = segment[1]
        if x > maxx:
            maxx = x
        if x < minx:
            minx = x
        if y > maxy:
            maxy = y
        if y < miny:
            miny = y

    print(minx, maxx, miny, maxy)

    for y in range(maxy, miny - 1, -1):
        for x in range(minx, maxx+1):
            for i in range(0, 10):
                if rope[i] == (x,y):
                    if i == 0:
                        print("H", end="")
                        break
                    else:
                        print(i, end="")
                        break
            else:
                print('.', end="")
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

        print("==", dir, steps, "==")

        for _ in range(0, int(steps)):
            # oldrope = rope.copy()
            for i in range(0,9):
                x = rope[i][0]
                y = rope[i][1]
                if i == 0:
                    x += dirs[dir][0]
                    y += dirs[dir][1]

                #print(x,y,rope)
                if abs(x - rope[i + 1][0]) == 2:
                    newx = (rope[i + 1][0] + x) / 2
                    # if rope[i + 1][0] < x:
                    #     newx = rope[i + 1][0] + 1
                    # else:
                    #     newx = rope[i + 1][0] - 1
                else:
                    newx = x
                if abs(y - rope[i + 1][1]) >= 2:
                    newy = (rope[i + 1][1] + y) / 2
                    # if rope[i + 1][1] < y:
                    #     newy = rope[i + 1][1] + 1
                    # else:
                    #     newy = rope[i + 1][1] - 1
                else:
                    newy = y
                rope[i + 1] = (newx, newy)
                # elif rope[i + 1][0] == x or rope[i + 1][1] == y:
                        # rope[i + 1] = oldrope[i]

                rope[i] = (x,y)
            if rope[9] not in visited:
                visited[rope[9]] = True
            printrope(rope)

print(len(visited))