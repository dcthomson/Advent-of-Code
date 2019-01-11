file = open("input.txt", "r")

grid = dict()

for line in file:
    [num, _, scoord, wh] = line.split()
    num = num.lstrip('#')
    [sx, sy] = scoord.split(",")
    sy = sy.rstrip(':')
    [whx, why] = wh.split("x")

    print line
    print "num: ", str(num)
    print "sx:  ", str(sx)
    print "sy:  ", str(sy)
    print "whx: ", str(whx)
    print "why: ", str(why)
    print "\n"

    for x in range(int(sx), int(sx) + int(whx)):
        for y in range(int(sy), int(sy) + int(why)):
            key = str(x) + "-" + str(y)
            if key in grid:
                grid[key] = grid[key] + "-" + num
            else:
                grid[key] = num

counts = dict()
for key in grid:
    nums = grid[key].split("-")
    for num in nums:
        if num in counts:
            if len(nums) > counts[num]:
                counts[num] = len(nums)
        else:
            counts[num] = len(nums)

for key in counts:
    if counts[key] == 1:
        print key




#overlaps = 0
#for key in grid:
#    if grid[key] > 1:
#        overlaps += 1
#
#print "overlaps: ", str(overlaps)
