import sys

instructions = []
waypoint = [10, 1]

loc = [0,0]

with open(sys.argv[1], "r") as f:
    for line in f:
        d = {}
        line = line.rstrip()
        d["direction"] = line[:1]
        d["num"] = int(line[1:])
        instructions.append(d)   

rotations = {}
for i in instructions:
    if i['direction'] == "L":
        if i['num'] == 180:
            waypoint[0] *= -1
            waypoint[1] *= -1
        elif i['num'] == 90:
            newy = waypoint[0]
            waypoint[0] = waypoint[1] * -1
            waypoint[1] = newy
        elif i['num'] == 270:
            newy = waypoint[0] * -1
            waypoint[0] = waypoint[1]
            waypoint[1] = newy
    if i['direction'] == "R":
        if i['num'] == 180:
            waypoint[0] *= -1
            waypoint[1] *= -1
        elif i['num'] == 90:
            newy = waypoint[0] * -1
            waypoint[0] = waypoint[1]
            waypoint[1] = newy
        elif i['num'] == 270:
            newy = waypoint[0]
            waypoint[0] = waypoint[1] * -1
            waypoint[1] = newy
    if i['direction'] == "F":
        loc[0] += i['num'] * waypoint[0]
        loc[1] += i['num'] * waypoint[1]
    if i['direction'] == "E":
        waypoint[0] += i['num']
    elif i['direction'] == "W":
        waypoint[0] -= i['num']
    elif i['direction'] == "N":
        waypoint[1] += i['num']
    elif i['direction'] == "S":
        waypoint[1] -= i['num']

print(abs(loc[0] + abs(loc[1])))