import sys

planets = {}

with open(sys.argv[1]) as f:
    for line in f:
        (a, b) = line.rstrip().split(")")
        planets[b] = a

santapath = {}
curplanet = planets["SAN"]
nodecount = 0
while curplanet != "COM":
    santapath[curplanet] = nodecount
    nodecount += 1
    curplanet = planets[curplanet]

curplanet = planets["YOU"]
nodecount = 0
while curplanet not in santapath:
    curplanet = planets[curplanet]
    nodecount += 1

print(santapath[curplanet] + nodecount)