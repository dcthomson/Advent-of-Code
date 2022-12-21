import sys

cubegrid = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        (x,y,z) = line.split(",")
        cubegrid[(int(x),int(y),int(z))] = True

surfacearea = 0

for c in cubegrid:
    for s in range(0,3):
        myc = []
        myc.append(c[0])
        myc.append(c[1])
        myc.append(c[2])
        for i in (-1, 1):
            myc[s] = c[s] + i
            if (myc[0], myc[1], myc[2]) not in cubegrid:
                surfacearea += 1

print(surfacearea)