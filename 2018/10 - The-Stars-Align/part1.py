import sys

file = open(sys.argv[1], "r")

class Star:
    def __init__(self, px, py, vx, vy):
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)

    def move_forward(self):
        self.px += self.vx
        self.py += self.vy

    def move_backward(self):
        self.px -= self.vx
        self.py -= self.vy

    def __str__(self):
        pos = "(" + str(self.px) + ", " + str(self.py) + ")"
        vel = "(" + str(self.vx) + ", " + str(self.vy) + ")"
        return pos + "-" + vel


def getStars(stars):
    for line in file:
        (_, p, v) = line.split("<")
        p = p.split(">")[0]
        (px, py) = p.split(",")
        v = v.split(">")[0]
        (vx, vy) = v.split(",")

        stars.append(Star(int(px), int(py), int(vx), int(vy)))

    return stars

def printStars(stars):
    leftboundry = None
    rightboundry = None
    topboundry = None
    bottomboundry = None


    for star in stars:
        if leftboundry is None or star.px < leftboundry:
            leftboundry = star.px
        if rightboundry is None or star.px > rightboundry:
            rightboundry = star.px
        if topboundry is None or star.py < topboundry:
            topboundry = star.py
        if bottomboundry is None or star.py > bottomboundry:
            bottomboundry = star.py

    stars = sorted(stars, key=lambda star: star.px)
    stars = sorted(stars, key=lambda star: star.py)

    print

    print "lb: %s, rb: %s, tb: %s, bb: %s" % (leftboundry, rightboundry, topboundry, bottomboundry)

    for y in range(topboundry, bottomboundry + 1):
        for x in range(leftboundry, rightboundry + 1):
            printed = False
            for star in stars:
                if star.px == x and star.py == y:
                    sys.stdout.write("#")
                    printed = True
                    break
            if not printed:
                sys.stdout.write(".")
        print


#    print "lb: %s, rb: %s, tb: %s, bb: %s" % (leftboundry, rightboundry, topboundry, bottomboundry)

#    x = leftboundry
#    y = topboundry
#    for star in stars:
#        if star.py > y:
#            # newline
#            for _ in range (y, star.py):
#                print
#            x = leftboundry
#            y = star.py
#        for i in range(x, star.px):
#            sys.stdout.write(" ")
#            sys.stdout.flush()
#        x = star.px + 1
#        sys.stdout.write("#")
#        sys.stdout.flush()
    print

def listStars(stars):
    for star in stars:
        print str(star.px) + " " + str(star.py) + " " + str(star.vx) + " " + str(star.vy)

stars = list()
stars = getStars(stars)

# listStars(stars)

lastu = False
lastd = False
lastl = False
lastr = False

seconds = 0

while 1:
#    c = "f"
#    if printStars(stars):
#        c = raw_input("direction: ")
#    if c == "f":
#        for s in stars:
#            s.move_forward()
#    if c == "b":
#        for s in stars:
#            s.move_backward()
    up = False
    down = False
    left = False
    right = False
    for star in stars:
        if not up:
            up = star.py
            down = star.py
            left = star.px
            right = star.px
        else:
            if star.py < up:
                up = star.py
            if star.py > down:
                down = star.py
            if star.px < left:
                left = star.px
            if star.px > right:
                right = star.px
        star.move_forward()

    if lastd:
        if down - up > lastd - lastu:
            if right - left > lastr - lastl:
                print "r: %s - l: %s - d: %s - u: %s" % (right, left, down, up)
                print "x: %s - y: %s" % (right - left, down - up)
                print
                for star in stars:
                    star.move_backward()
                    star.move_backward()
                print "seconds: %s" % (seconds - 1)
                print "printing stars..."
                direction = ""
                while True:
                    printStars(stars)
                    ri = raw_input('b: back\nf: forward\nq: quit:  ')
                    if ri == "b":
                        direction = "b"
                    elif ri == "q":
                        sys.exit()
                    elif ri == "f":
                        direction = "f"
                    if direction == "b":
                        for star in stars:
                            star.move_backward()
                    if direction == "f":
                        for star in stars:
                            star.move_forward()
                    

    lastu = up
    lastd = down
    lastl = left
    lastr = right

    seconds += 1
