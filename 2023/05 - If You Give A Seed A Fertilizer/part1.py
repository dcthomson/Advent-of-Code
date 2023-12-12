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

for seed in seeds:
    num = seed
    for m in maps:
        for line in m:
            (dest, source, length) = line
            if source <= num <= source + length:
                num = dest + num - source
                break
            
    if not lowest or num < lowest:
        lowest = num
print(lowest)