import sys

totalaccel = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        accel = line.split(", ")[2]
        accel = accel.strip("a=<").strip(">").split(",")
        ta = abs(int(accel[0])) + abs(int(accel[1])) + abs(int(accel[2]))
        totalaccel.append(ta)

print([index for index, value in enumerate(totalaccel) if value == min(totalaccel)])