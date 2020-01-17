import sys
import copy
import math

file = open(sys.argv[1], "r")


class Coord:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


class Nanobot:
    def __init__(self, x, y, z, r):
        self.c = Coord(x, y, z)
        self.radius = int(r)
        self.vertices = False

    def lineintersects(self, c1, c2):
        # find if a line with endpoints c1 and c2 intersect nanobot radius
        if c1.x != c2.x:
            if c1.x > c2.x:
                tmp = c2
                c2 = c1
                c1 = tmp
            if c1.x < self.c.x < c2.x:
                if abs(c1.y - self.c.y) + abs(c1.z - self.c.z) < self.radius:
                    return True
        if c1.y != c2.y:
            if c1.y > c2.y:
                tmp = c2
                c2 = c1
                c1 = tmp
            if c1.y < self.c.y < c2.y:
                if abs(c1.x - self.c.x) + c1.z - abs(self.c.z) < self.radius:
                    return True
        if c1.z != c2.z:
            if c1.z > c2.z:
                tmp = c2
                c2 = c1
                c1 = tmp
            if c1.z < self.c.z < c2.z:
                if abs(c1.x - self.c.x) + abs(c1.y - self.c.y) < self.radius:
                    return True
        return False


    def __str__(self):
        return "x: %s, y: %s, z: %s, r: %s" % (self.c.x, self.c.y, self.c.z, self.radius)

    def getvertices(self):
        if not self.vertices:
            self.vertices = []
            self.vertices.append(Coord(self.c.x + self.radius, self.c.y, self.c.z))
            self.vertices.append(Coord(self.c.x - self.radius, self.c.y, self.c.z))
            self.vertices.append(Coord(self.c.x, self.c.y + self.radius, self.c.z))
            self.vertices.append(Coord(self.c.x, self.c.y - self.radius, self.c.z))
            self.vertices.append(Coord(self.c.x, self.c.y, self.c.z + self.radius))
            self.vertices.append(Coord(self.c.x, self.c.y, self.c.z - self.radius))
        return self.vertices

    def inradius(self, c):
        x = abs(self.c.x - c.x)
        y = abs(self.c.y - c.y)
        z = abs(self.c.z - c.z)
        if x + y + z <= self.radius:
            return True
        else:
            return False


class Cube:
    def __init__(self, origin, size, id=0):
        self.o = origin               # Coord: bottom left closest
        self.size = int(size)
        self.nbcount = 0
        self.id = id
        self.vertices = False
        self.edges = False

    def __str__(self):
        return "Cube: %s  origin: %s  count: %s" % (self.id, self.o, self.nbcount)

    def getvertices(self):
        #     6----7
        #    /|   /|
        #   2-+--4 |
        #   | 3--+-5
        #   |/   |/
        #   0----1
        if not self.vertices:
            self.vertices = []
            self.vertices.append(self.o)    # 0
            x = Coord(self.o.x + self.size, self.o.y, self.o.z)
            self.vertices.append(x)         # 1
            y = Coord(self.o.x, self.o.y + self.size, self.o.z)
            self.vertices.append(y)         # 2
            z = Coord(self.o.x, self.o.y, self.o.z + self.size)
            self.vertices.append(z)         # 3
            xy = Coord(self.o.x + self.size, self.o.y + self.size, self.o.z)
            self.vertices.append(xy)        # 4
            xz = Coord(self.o.x + self.size, self.o.y, self.o.z + self.size)
            self.vertices.append(xz)        # 5
            yz = Coord(self.o.x, self.o.y + self.size, self.o.z + self.size)
            self.vertices.append(yz)        # 6
            xyz = Coord(self.o.x + self.size, self.o.y + self.size, self.o.z + self.size)
            self.vertices.append(xyz)       # 7
        return self.vertices

    def nanobotinside(self, nb):
        if nb.c.x + nb.radius < self.o.x:
            return False
        if nb.c.x - nb.radius > self.o.x + self.size:
            return False
        if nb.c.y + nb.radius < self.o.y:
            return False
        if nb.c.y - nb.radius > self.o.y + self.size:
            return False
        if nb.c.z + nb.radius < self.o.z:
            return False
        if nb.c.z - nb.radius > self.o.z + self.size:
            return False

        # check if any of the 8 cube vertices are in the nanobot radius
        for vertex in self.getvertices():
            if nb.inradius(vertex):
                return True

        # check if any of the nanobot octahedron vertices are in cube
        for vertex in nb.getvertices():
            if self.coordinside(vertex):
                return True

        # check if cube edge intersects with octahedron
        for coords in self.getedges():
            #      shouldn't need to check all 12
            if nb.lineintersects(coords[0], coords[1]):
                return True

        return False

    def getedges(self):
        # get edges defined by 2 coords
        if not self.edges:
            self.edges = []
            v = self.getvertices() # see getvertices() for cube diagram
            self.edges.append((v[0], v[1]))
            self.edges.append((v[0], v[2]))
            self.edges.append((v[0], v[3]))
            self.edges.append((v[1], v[4]))
            self.edges.append((v[1], v[5]))
            self.edges.append((v[2], v[4]))
            self.edges.append((v[2], v[6]))
            self.edges.append((v[3], v[5]))
            self.edges.append((v[3], v[6]))
            self.edges.append((v[4], v[7]))
            self.edges.append((v[5], v[7]))
            self.edges.append((v[6], v[7]))

        return self.edges

    def coordinside(self, c):
        if c.x > self.o.x and c.x < self.o.x + self.size:
            if c.y > self.o.y and c.y < self.o.y + self.size:
                if c.z > self.o.z and c.z < self.o.z + self.size:
                    return True
        return False

    def outside(self, nb):
        if nb.c.x + nb.radius < self.o.x:
            return True
        if nb.c.x - nb.radius > self.o.x + self.size:
            return True
        if nb.c.y + nb.radius < self.o.y:
            return True
        if nb.c.y - nb.radius > self.o.y + self.size:
            return True
        if nb.c.z + nb.radius < self.o.z:
            return True
        if nb.c.z - nb.radius > self.o.z + self.size:
            return True
        return False

    def intersects(self, nb):    # check if nanobot intersects cube
        dist_squared = nb.radius * nb.radius
        if nb.c.x < self.o.x:
            dist_squared -= abs(nb.c.x - self.o.x) ** 2
        elif nb.c.x > self.o.x + self.size:
            dist_squared -= abs(nb.c.x - self.o.x + self.size) ** 2
        if nb.c.y < self.o.y:
            dist_squared -= abs(nb.c.y - self.o.y) ** 2
        elif nb.c.y > self.o.y + self.size:
            dist_squared -= abs(nb.c.y - self.o.y + self.size) ** 2
        if nb.c.z < self.o.z:
            dist_squared -= abs(nb.c.z - self.o.z) ** 2
        elif nb.c.z > self.o.z + self.size:
            dist_squared -= abs(nb.c.z - self.o.z + self.size) ** 2
        return dist_squared > 0

    def divideintoeight(self):
        cubes = []
        if self.size == 1:
            size = 0
            offset = 1
        else:
            size = self.size / 2

            if self.size % 2 == 0:
                # even size
                offset = size
            else:
                # odd size
                offset = math.floor(size)
                size = math.ceil(size)

        # Front cubes
        # F00
        # F10
        cubes.append(Cube(self.o, size, 1))

        # F00
        # F01
        o = copy.deepcopy(self.o)
        o.x += offset
        cubes.append(Cube(o, size, 2))

        # F10
        # F00
        o = copy.deepcopy(self.o)
        o.y += offset
        cubes.append(Cube(o, size, 3))

        # F01
        # F00
        o = copy.deepcopy(self.o)
        o.y += offset
        o.x += offset
        cubes.append(Cube(o, size, 4))

        # Rear cubes
        ro = copy.deepcopy(self.o)
        ro.z += offset
        # R00
        # R10
        cubes.append(Cube(ro, size, 5))

        # R00
        # R01
        o = copy.deepcopy(ro)
        o.x += offset
        cubes.append(Cube(o, size, 6))

        # R10
        # R00
        o = copy.deepcopy(ro)
        o.y += offset
        cubes.append(Cube(o, size, 7))

        # R01
        # R00
        o = copy.deepcopy(ro)
        o.y += offset
        o.x += offset
        cubes.append(Cube(o, size, 8))

        return cubes # 8 cubes


nanobots = list()

for line in file:
    (x, y, z, r) = line.split(",")
    x = x.lstrip("pos=<")
    z = z.rstrip(">")
    (_, r) = r.split("=")
    nanobots.append(Nanobot(x, y, z, r))

max = 0
for nanobot in nanobots:
    if abs(nanobot.c.x) > max:
        max = abs(nanobot.c.x)
    if abs(nanobot.c.y) > max:
        max = abs(nanobot.c.y)
    if abs(nanobot.c.z) > max:
        max = abs(nanobot.c.z)

i = 1
while i < max:
    i *= 2

max = i #lets make the squares all powers of 2 :)

newcubes = [Cube(Coord(-max, -max, -max), max * 2)]

while newcubes[0].size >= 1:
    dividedcubes = []
    for nc in newcubes:
        dividedcubes += nc.divideintoeight()
    for c in dividedcubes:
        for nanobot in nanobots:
            if c.nanobotinside(nanobot):
                c.nbcount += 1

    newcubes = []
    nccount = 0
    for c in dividedcubes:
        if not newcubes:
            newcubes.append(c)
            nccount = c.nbcount
        elif c.nbcount == nccount:
            newcubes.append(c)
        elif c.nbcount > nccount:
            newcubes = []
            newcubes.append(c)
            nccount = c.nbcount

n = newcubes[0]
print(int(abs(n.o.x) + abs(n.o.y) + abs(n.o.z)))  