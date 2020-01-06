import math

elfcount = 3014387

elves = []

for i in range(1, elfcount + 1):
    elves.append(i)

currelfindex = 0

elfcount = len(elves)

while elfcount > 1:
    # get elf across
    elfindextoremove = currelfindex + math.floor(elfcount / 2)
    try:
        del elves[elfindextoremove]
    except:
        elfindextoremove -= elfcount

        del elves[elfindextoremove]
        currelfindex -= 1
    elfcount -= 1
    currelfindex += 1
    if currelfindex >= elfcount:
        currelfindex = 0

print(elves[0])