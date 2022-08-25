import sys

xmin = xmax = ymin = ymax = None

with open(sys.argv[1], "r") as f:
    for line in f:
        (_,_,x,y) = line.rstrip().split()
        x = x.rstrip(",")
        (xmin, xmax) = x.split("=")[1].split("..")
        (ymin, ymax) = y.split("=")[1].split("..")
        xmin = int(xmin)
        xmax = int(xmax)
        ymin = int(ymin)
        ymax = int(ymax)

maxheight = 0

# z will = the lowest x that will reach the target area
t = z = 0
while t < xmin:
    z += 1
    t += z

for x in range(z,xmax + 1):
    y = ymin
    posx = 0
    posy = 0
    bottomlefthit = False
    bottomrighthit = False
    while True:
        if bottomrighthit and bottomlefthit:
            break
        hit = False
        curmaxheight = 0
        dx = x
        dy = y
        posx = 0
        posy = 0
        while posy >= ymin and posx <= xmax:
            posx += dx
            posy += dy
            print(x,y,posx,posy)
            if dy > curmaxheight:
                curmaxheight = dy
            if posx >= xmin and posx <= xmax:
                if posy >= ymin and posy <= ymax:
                    hit = True
                    break
            if dx > 1:
                dx -= 1
            dy -= 1
            if posx < xmin:
                if posy < ymin:
                    bottomlethit = True
                elif posy > ymax:
                    bottomrighthit = True
        y += 1
        if hit:
            print("HIT!",x,y)
            if curmaxheight > maxheight:
                maxheight = curmaxheight
            dy += 1

print(maxheight)