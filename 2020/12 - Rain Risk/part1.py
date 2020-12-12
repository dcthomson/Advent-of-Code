import sys

direction = "E"
instructions = []

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
    # print(loc)
    # print(direction)
    # print(i)
    # print()
    if i['direction'] == "L":
        if direction == "E":
            if i['num'] == 90:
                direction = "N"
            elif i['num'] == 180:
                direction = "W"
            elif i['num'] == 270:
                direction = "S"
        elif direction == "N":
            if i['num'] == 90:
                direction =  "W"
            elif i['num'] == 180:
                direction = "S"
            elif i['num'] == 270:
                direction = "E"
        elif direction == "W":
            if i['num'] == 90:
                direction = "S"
            elif i['num'] == 180:
                direction = "E"
            elif i['num'] == 270:
                direction = "N"
        elif direction == "S":
            if i['num'] == 90:
                direction = "E"
            elif i['num'] == 180:
                direction = "N"
            elif i['num'] == 270:
                direction = "W"
    if i['direction'] == "R":
        if direction == "E":
            if i['num'] == 90:
                direction = "S"
            elif i['num'] == 180:
                direction = "W"
            elif i['num'] == 270:
                direction = "N"
        elif direction == "N":
            if i['num'] == 90:
                direction =  "E"
            elif i['num'] == 180:
                direction = "S"
            elif i['num'] == 270:
                direction = "W"
        elif direction == "W":
            if i['num'] == 90:
                direction = "N"
            elif i['num'] == 180:
                direction = "E"
            elif i['num'] == 270:
                direction = "S"
        elif direction == "S":
            if i['num'] == 90:
                direction = "W"
            elif i['num'] == 180:
                direction = "N"
            elif i['num'] == 270:
                direction = "E"
    if i['direction'] == "F":
        if direction == "E":
            loc[0] += i['num']
        elif direction == "W":
            loc[0] -= i['num']
        elif direction == "N":
            loc[1] += i['num']
        elif direction == "S":
            loc[1] -= i['num']
    if i['direction'] == "E":
        loc[0] += i['num']
    elif i['direction'] == "W":
        loc[0] -= i['num']
    elif i['direction'] == "N":
        loc[1] += i['num']
    elif i['direction'] == "S":
        loc[1] -= i['num']

print(abs(loc[0] + abs(loc[1])))