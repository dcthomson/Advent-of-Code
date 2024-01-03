import sys

seeds = []
maps = []
with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        if line.startswith("seeds:"):
            (_, seeds) = line.split(": ")
            s = seeds.split()
            seeds = [int(x) for x in s]  
        elif "map:" in line:
            maps.append([])
        elif line == "":
            pass
        else:
            maps[-1].append([int(x) for x in line.split()])

lowest = False
seedpair = []

print(seeds)
min = None
max = 0

for line in maps[-1]:
    (dest, source, length) = line
    if min is None or dest < min:
        min = dest
    if dest + length > max:
        max = dest + length

print(min, max)

for num in range(0, max):
    n = num
    for m in reversed(maps):
        for line in m:
            (dest, source, length) = line
            if dest <= num <= dest + length:
                num = source + num - dest
                break
    for i in range(0, len(seeds), 2):
        if seeds[i] < num < seeds[i] + seeds[i+1]:
            print(n)
            exit()

exit()