import sys

planets = {}

with open(sys.argv[1]) as f:
    for line in f:
        (a, b) = line.rstrip().split(")")
        planets[b] = a

orbits = 0
for k in planets:
    curplanet = k
    while curplanet != "COM":
        # print(k, "orbits", v)
        curplanet = planets[curplanet]
        orbits += 1

print(orbits)