import sys
import time

file = open(sys.argv[1], "r")

class Cart:

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        if char == "<":
            self.dir = "L"
        if char == ">":
            self.dir = "R"
        if char == "^":
            self.dir = "U"
        if char == "v":
            self.dir = "D"
        self.intersectionDir = "L"
        self.iteration = 0

    def arrow(self):
        if self.dir == "R":
            return ">"
        if self.dir == "L":
            return "<"
        if self.dir == "U":
            return "^"
        if self.dir == "D":
            return "v"

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + self.arrow() + ")"

    def nextIntersection(self):
        if self.intersectionDir == "L":
            self.intersectionDir = "S"
        elif self.intersectionDir == "S":
            self.intersectionDir = "R"
        elif self.intersectionDir == "R":
            self.intersectionDir = "L"

    def move(self, r):
        if self.dir == "L":
            self.x -= 1
        elif self.dir == "R":
            self.x += 1
        elif self.dir == "U":
            self.y -= 1
        elif self.dir == "D":
            self.y += 1
        if r[(self.x, self.y)] == "/":
            if self.dir == "L":
                self.dir = "D"
            elif self.dir == "R":
                self.dir = "U"
            elif self.dir == "U":
                self.dir = "R"
            elif self.dir == "D":
                self.dir = "L"
        elif r[(self.x, self.y)] == "\\":
            if self.dir == "L":
                self.dir = "U"
            elif self.dir == "R":
                self.dir = "D"
            elif self.dir == "U":
                self.dir = "L"
            elif self.dir == "D":
                self.dir = "R"
        elif r[(self.x, self.y)] == "+":
            if self.dir == "L":
                if self.intersectionDir == "L":
                    self.dir = "D"
                elif self.intersectionDir == "R":
                    self.dir = "U"
            elif self.dir == "R":
                if self.intersectionDir == "L":
                    self.dir = "U"
                elif self.intersectionDir == "R":
                    self.dir = "D"
            elif self.dir == "U":
                if self.intersectionDir == "L":
                    self.dir = "L"
                elif self.intersectionDir == "R":
                    self.dir = "R"
            elif self.dir == "D":
                if self.intersectionDir == "L":
                    self.dir = "R"
                elif self.intersectionDir == "R":
                    self.dir = "L"
            self.nextIntersection()

        self.iteration += 1

        return (self.x, self.y)

    def checkCollision(self, carts):
        collisions = 0
        for cart in carts:
            if cart.x == self.x and cart.y == self.y:
                collisions += 1
        if collisions == 2:
            return True
        else:
            return False



railsystem = dict()
carts = list()

linenum = 0
colnum = 0
for line in file:
    colnum = 0
    for c in line:
        c = c.rstrip()
        if c == "":
            c = " "
        if c == "<" or c == ">" or c == "^" or c == "v":
            carts.append(Cart(colnum, linenum, c))
            if c == "<" or c == ">":
                railsystem[(colnum, linenum)] = "-"
            else:
                railsystem[(colnum, linenum)] = "|"
        else:
            railsystem[(colnum, linenum)] = c
        colnum += 1
    linenum += 1


printrailsystem = False
x = None
y = None
iteration = 0
while True:
    if printrailsystem:
        for j in range(0, linenum):
            print
            for i in range(0, colnum):
                printed = False
                for cart in carts:
                    if cart.x == i and cart.y == j:
                        sys.stdout.write(cart.arrow())
                        printed = True
                if not printed:
                    sys.stdout.write(railsystem[(i, j)])

    for j in range(0, linenum):
        for i in range(0, colnum):
            collisions = list()
            for cart in carts:
                if cart.x == i and cart.y == j:
                    if cart.iteration == iteration:
                        cart.move(railsystem)
                        # check for colisions
                        if cart.checkCollision(carts):
                            collisions.append((cart.x, cart.y))
                            break
            if len(collisions) > 0:
                for (cx, cy) in collisions:
                    lesscarts = list()
                    for cart in carts:
                        if cart.x == cx and cart.y == cy:
                            pass
                        else:
                            lesscarts.append(cart)
                    carts = lesscarts
                    #print "len-carts: " + str(len(carts))
                    if len(carts) == 1:
                        x = carts[0].x
                        y = carts[0].y
                        print "(%s,%s)" % (x, y)
                        sys.exit()
                        break
        else:
            continue
        break
    else:
        if printrailsystem:
            print
        iteration += 1
        continue
    break

if printrailsystem:
    print    
print "(" + str(x) + ", " + str(y) + ")"
