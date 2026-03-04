import sys

jbs = {}
distances = {}
circuits = []
connections = 1000

class JunctionBox:

    def __init__(self, s):
        self.id = s
        self.x,self.y,self.z = [int(x) for x in s.split(',')]


with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        jbs[line] = JunctionBox(line)

for id1 in jbs:
    for id2 in jbs:
        if id1 == id2:
            continue
        if (id1,id2) not in distances and (id2,id1) not in distances:
            d = (jbs[id2].x - jbs[id1].x) ** 2 + (jbs[id2].y - jbs[id1].y) ** 2 + (jbs[id2].z - jbs[id1].z) ** 2
            distances[(id1,id2)] = d

sorted_distances = {}
for k in sorted(distances, key=distances.get):
    sorted_distances[k] = distances[k]


for conns, k in enumerate(sorted_distances):
    if conns == connections:
        break
    jb0 = None
    jb1 = None
    for i, c in enumerate(circuits):
        if k[0] in c:
            jb0 = i
        if k[1] in c:
            jb1 = i
    if jb0 == None:
        if jb1 == None:
            circuits.append([k[0], k[1]])
        else:
            circuits[jb1].append(k[0])
    elif jb1 == None:
        circuits[jb0].append(k[1])
    elif jb0 == jb1:
        pass
    else:
        for i in circuits[jb1]:
            circuits[jb0].append(i)
        del circuits[jb1]


circuitlengths = []
for c in circuits:
    circuitlengths.append(len(c))
circuitlengths.sort(reverse=True)
print(circuitlengths[0] * circuitlengths[1] * circuitlengths[2])