import sys

count = 0

triangles = [[],[],[]]

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        sides = line.split()
        for i in range(0, 3):
            sides[i] = int(sides[i])
            triangles[i].append(sides[i])

        if len(triangles[0]) == 3:
            for i in range(0, 3):
                triangle = True
                if triangles[i][0] + triangles[i][1] <= triangles[i][2]:
                    triangle = False
                elif triangles[i][1] + triangles[i][2] <= triangles[i][0]:
                    triangle = False
                elif triangles[i][0] + triangles[i][2] <= triangles[i][1]:
                    triangle = False
                if triangle:
                    count += 1
                triangles[i] = []

print(count)