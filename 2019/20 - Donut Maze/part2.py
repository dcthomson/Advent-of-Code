import sys

donut = {}

def printdonut(donut):
    for k in sorted(donut):
        print(donut[k], end="")

outertopleft = None
outertopright = None
outerbottomleft = None
outerbottomright = None
innertopleft = None
innertopright = None
innerbottomleft = None
innerbottomright = None

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            if outertopleft is None and c == "#":
                outertopleft = (y, x)
            if outertopleft is not None and outertopright is None and c == " ":
                outertopright = (y, x - 1)
            if outertopleft is not None and outertopright is not None:
                if x > outertopleft[1] and x < outertopright[1]:
                    if c == " " and innertopleft is None:
                        innertopleft = (y - 1, x - 1)
                    if innertopleft is not None:
                        if innertopright is None and c == "#":
                            innertopright = (y - 1, x)
            if innertopleft is not None:
                if x == innertopleft[1] + 1 and innerbottomleft is None:
                    if c == "#":
                        innerbottomleft = (y, x - 1)
                        innerbottomright = (y, innertopright[1])
            if outertopleft is not None and outerbottomleft is None:
                if x == outertopleft[1] and c == " ":
                    outerbottomleft = (y - 1, outertopleft[1])
                    outerbottomright = (y - 1, outertopright[1])
                
            donut[(y, x)] = c
            x += 1
        y += 1

# FIND PORTALS
iportals = {}
oportals = {}
# OUTER

# TOP
y = outertopleft[0]
for x in range(outertopleft[1], outertopright[1]):
    if donut[(y, x)] == ".":
        oportals[(y, x)] = donut[(y - 2, x)] + donut[(y - 1, x)]
# BOTTOM
y = outerbottomleft[0]
for x in range(outerbottomleft[1], outerbottomright[1]):
    if donut[(y, x)] == ".":
        oportals[(y, x)] = donut[(y + 1, x)] + donut[(y + 2, x)]
# LEFT
x = outertopleft[1]
for y in range(outertopleft[0], outerbottomleft[0]):
    if donut[(y, x)] == ".":
        oportals[(y, x)] = donut[(y, x - 2)] + donut[(y, x - 1)]
# RIGHT
x = outertopright[1]
for y in range(outertopright[0], outerbottomright[0]):
    if donut[(y, x)] == ".":
        oportals[(y, x)] = donut[(y, x + 1)] + donut[(y, x + 2)]

# INNER
# TOP
y = innertopleft[0]
for x in range(innertopleft[1], innertopright[1]):
    if donut[(y, x)] == ".":
        iportals[(y, x)] = donut[(y + 1, x)] + donut[(y + 2, x)]
# BOTTOM
y = innerbottomleft[0]
for x in range(innerbottomleft[1], innerbottomright[1]):
    if donut[(y, x)] == ".":
        iportals[(y, x)] = donut[(y - 2, x)] + donut[(y - 1, x)]
# LEFT
x = innertopleft[1]
for y in range(innertopleft[0], innerbottomleft[0]):
    if donut[(y, x)] == ".":
        iportals[(y, x)] = donut[(y, x + 1)] + donut[(y, x + 2)]
# RIGHT
x = innertopright[1]
for y in range(innertopright[0], innerbottomright[0]):
    if donut[(y, x)] == ".":
        iportals[(y, x)] = donut[(y, x - 2)] + donut[(y, x - 1)]

iportalpairs = {}
oportalpairs = {}
start = None
end = None


# portals = {}
# for p in (iportals, oportals):
#     portals.update(p)

for k, v in iportals.items():
    for k2, v2 in oportals.items():
        if v == v2 and k != k2:
            iportalpairs[k] = k2
        if v == "AA":
            start = (k[0], k[1], 0)
        if v == "ZZ":
            end = (k[0], k[1], 0)
for k, v in oportals.items():
    for k2, v2 in iportals.items():
        if v == v2 and k != k2:
            oportalpairs[k] = k2
        if v == "AA":
            start = (k[0], k[1], 0)
        if v == "ZZ":
            end = (k[0], k[1], 0)


visited = {}


distance = 0
Q = [(start, 0)]
visited[(start, 0)] = 0

while Q:
    node, distance = Q.pop(0)
    if node == end:
        print(distance)
        break
    if node not in visited:
        visited[node] = distance
        neighbors = []
        if donut[(node[0] - 1, node[1])] == ".":
            neighbors.append((node[0] - 1, node[1], node[2]))
        if donut[(node[0], node[1] + 1)] == ".":
            neighbors.append((node[0], node[1] + 1, node[2]))
        if donut[(node[0] + 1, node[1])] == ".":
            neighbors.append((node[0] + 1, node[1], node[2]))
        if donut[(node[0], node[1] - 1)] == ".":
            neighbors.append((node[0], node[1] - 1, node[2]))
        if (node[0], node[1]) in iportalpairs:
            x, y = iportalpairs[(node[0], node[1])]
            neighbors.append((x, y, node[2] - 1))
        if (node[0], node[1]) in oportalpairs:
            if node[2] != 0:
                x, y = oportalpairs[(node[0], node[1])]
                neighbors.append((x, y, node[2] + 1))
        
        for neighbor in neighbors:
            if neighbor not in visited:
                Q.append((neighbor, distance + 1))