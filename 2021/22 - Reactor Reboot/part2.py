import sys

cubes = dict()

instructions = []

with open(sys.argv[1], "r") as f:
    for line in f:
        i = {}
        line = line.rstrip()
        (i['state'], coords) = line.split()
        (x, y, z) = coords.split(",")
        (i['xmin'], i['xmax']) = x.split("=")[1].split("..")
        (i['ymin'], i['ymax']) = y.split("=")[1].split("..")
        (i['zmin'], i['zmax']) = z.split("=")[1].split("..")
        for k, v in i.items():
            if k != 'state':
                i[k] = int(i[k])
        instructions.append(i)

# for z in range(-50, 51):
#     for y in range(-50, 51):
#         for x in range(-50, 51):
#             cubes[(x, y, z)] = "off"

for i in instructions:
    print(i)
    for z in range(i['zmin'], i['zmax'] + 1):
        for y in range(i['ymin'], i['ymax'] + 1):
            for x in range(i['xmin'], i['xmax'] + 1):
                cubes[(x, y, z)] = i['state']

on = 0

for v in cubes.values():
    if v == "on":
        on += 1

print(on)