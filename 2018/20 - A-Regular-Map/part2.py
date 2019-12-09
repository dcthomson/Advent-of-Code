import sys

class Room:

    def __init__(self, x, y, char, dist):
        self.x = x
        self.y = y
        self.char = char
        self.dist = dist

    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.x, self.y, self.char, self.dist)

def makeRooms(x, y, regex, rooms, dist = 0):
    startx = x
    starty = y
    startdist = dist
    while len(regex):
        c = regex.pop(0)
        if c in "NWES":
            dist += 1
            if c == "N":
                y -= 2
            elif c == "W":
                x -= 2
            elif c == "E":
                x += 2
            elif c == "S":
                y += 2
            if (x,y) not in rooms:
                rooms[(x, y)] = Room(x, y, ".", dist)
            else:
                if dist < rooms[(x,y)].dist:
                    rooms[(x,y)].dist = dist

        elif c == "(":
            rooms = makeRooms(x, y, regex, rooms, dist)
        elif c == "|":
            x = startx
            y = starty
            dist = startdist
        elif c == ")" or c == "$":
            return rooms

def printRooms(rooms):
    boundries = dict()
    for room in rooms:
        if "N" not in boundries:
            boundries["N"] = room[1]
        elif room[1] < boundries["N"]:
            boundries["N"] = room[1]
        if "W" not in boundries:
            boundries["W"] = room[0]
        elif room[0] < boundries["W"]:
            boundries["W"] = room[0]
        if "E" not in boundries:
            boundries["E"] = room[0]
        elif room[0] > boundries["E"]:
            boundries["E"] = room[0]
        if "S" not in boundries:
            boundries["S"] = room[1]
        elif room[1] > boundries["S"]:
            boundries["S"] = room[1]
    for y in range(boundries["N"] - 1, boundries["S"] + 2):
        for x in range(boundries["W"] - 1, boundries["E"] + 2):
            if (x, y) not in rooms:
                sys.stdout.write("#")
            else:
                sys.stdout.write(rooms[(x, y)].char)

        print

def roomDistance(x, y, distance, rooms, roomDist):
    distance += 1
    for coord in ((x,x,y-1,y-2),(x,x,y+1,y+2),(x+1,x+2,y,y),(x-1,x-2,y,y)):
        if (coord[0], coord[2]) in rooms:
            if rooms[(coord[0], coord[2])] == "-" or rooms[(coord[0], coord[2])] == "|":
                if (coord[1], coord[3]) not in roomDist or distance < roomDist[(coord[1], coord[3])]:
                    roomDist[(coord[1], coord[3])] = distance
                    roomDist = roomDistance(coord[1], coord[3], distance, rooms, roomDist)
#    if (x, y - 1) in rooms:
#        if rooms[(x, y - 1)] == "-":
#            if (x, y - 2) not in roomDist or distance < roomDist[(x, y - 2)]:
#                roomDist[(x, y - 2)] = distance
#                roomDist = roomDistance(x, y - 2, distance, rooms, roomDist)
#    if (x, y + 1) in rooms:
#        if rooms[(x, y + 1)] == "-":
#            if (x, y + 2) not in roomDist or distance < roomDist[(x, y + 2)]:
#                roomDist[(x, y + 2)] = distance
#                roomDist = roomDistance(x, y + 2, distance, rooms, roomDist)
#    if (x - 1, y) in rooms:
#        if rooms[(x - 1, y)] == "|":
#            if (x - 2, y) not in roomDist or distance < roomDist[(x - 2, y)]:
#                roomDist[(x - 2, y)] = distance
#                roomDist = roomDistance(x - 2, y, distance, rooms, roomDist)
#    if (x + 1, y) in rooms:
#        if rooms[(x + 1, y)] == "|":
#            if (x + 2, y) not in roomDist or distance < roomDist[(x + 2, y)]:
#                roomDist[(x + 2, y)] = distance
#                roomDist = roomDistance(x + 2, y, distance, rooms, roomDist)
    return roomDist

file = open(sys.argv[1], "r")

regex = list()
rooms = dict()

for line in file:
    line = line.rstrip()
    for c in line:
        if c == '^' or c == '$':
            pass
        regex.append(c)

rooms[(0, 0)] = Room(0, 0, "X", 0)
rooms = makeRooms(0, 0, regex, rooms)
roomDist = dict()
distance = 0
#roomDist = roomDistance(0, 0, distance, rooms, roomDist)

count = 0
for room in rooms:
    if rooms[room].dist >= 1000: 
        count += 1
    

print str(count)
