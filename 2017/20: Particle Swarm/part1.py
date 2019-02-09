import sys

totalaccel = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        accel = line.strip().split(", ")[2]
        accel = accel.strip("a=<").strip(">").split(",")
        ta = abs(int(accel[0])) + abs(int(accel[1])) + abs(int(accel[2]))
        totalaccel.append(ta)
print(min(totalaccel))
print(totalaccel.index(min(totalaccel)))