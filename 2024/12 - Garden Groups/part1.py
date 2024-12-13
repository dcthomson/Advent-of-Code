import sys
from collections import defaultdict

grid = {}

x = y = xmax = ymax = 0

class Area:

    def __init__(self, grid, coord):
        self.name = grid[coord]
        self.area = 0
        self.perimeter = 0
        self.coords = []

        visited = []

        dirs = ((0,-1),(1,0),(0,1),(-1,0))
        q = [coord]
        while q:
            coord = q.pop(0)
            if coord not in visited:
                self.coords.append(coord)
                visited.append(coord)
                for d in dirs:
                    neighbor = (coord[0] + d[0], coord[1] + d[1])
                    try:
                        if grid[coord] == grid[neighbor]:
                            q.append(neighbor)
                        else:
                            self.perimeter += 1
                    except:
                        self.perimeter += 1
        
    def __repr__(self):
        ret = self.name + "\n"
        ret += "  perimeter: " + str(self.perimeter) + "\n"
        ret += "  coords: "
        for c in self.coords:
            ret += "(" + str(c[0]) + "," + str(c[1]) + ") "
        ret += "\n"
        return ret

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

# print(areas)

total = 0
for key in areas:
    for area in areas[key]:
        # print(area)
        total += len(area.coords) * area.perimeter
print(total)