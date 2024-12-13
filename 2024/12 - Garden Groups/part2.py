import sys
from collections import defaultdict

grid = {}

x = y = xmax = ymax = 0

class Area:

    def __init__(self, grid, coord):
        self.name = grid[coord]
        self.area = 0
        self.pcoords = []
        self.psides = []
        self.coords = []

        visited = []

        dirs = {"N":(0,-1),"E":(1,0),"S":(0,1),"W":(-1,0)}

        q = [coord]
        while q:
            coord = q.pop(0)
            if coord not in visited:
                self.coords.append(coord)
                visited.append(coord)
                for k, v in dirs.items():
                    neighbor = (coord[0] + v[0], coord[1] + v[1])
                    try:
                        if grid[coord] == grid[neighbor]:
                            q.append(neighbor)
                        else:
                            self.pcoords.append((coord, k))
                    except:
                        self.pcoords.append((coord, k))

        # find perimeter sides
        for pc in self.pcoords:
            (coord, coorddir) = pc
            
            found = False
            for side in self.psides:
                if (coord, coorddir) in side:
                    found = True
            if not found:
                q = [(coord, coorddir)]
                side = []
                visited = []
                while q:
                    c = q.pop(0)
                    if c not in visited:
                        visited.append(c)
                        side.append(c)
                        (coord, coorddir) = c
                        for d, dcoord in dirs.items():
                            for (pcoord, pd) in self.pcoords:
                                if (pd == coorddir and
                                    (coord[0] + dcoord[0], coord[1] + dcoord[1]) == pcoord):
                                    q.append((pcoord, pd))

                self.psides.append(side)                    

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        x = 0
        for c in line:
            grid[(x,y)] = c
            x += 1
            xmax = x
        y +=1
        ymax = y

areas = defaultdict(list)

for y in range(0, ymax):
    for x in range(0, xmax):
        letter = grid[(x,y)]
        found = False
        for k in areas:
            for a in areas[k]:
                if (x,y) in a.coords:
                    found = True
        if not found:
            a = Area(grid, (x,y))
            areas[grid[(x,y)]].append(a)

total = 0
for key in areas:
    for area in areas[key]:
        # print(area)
        total += len(area.coords) * len(area.psides)
print(total)