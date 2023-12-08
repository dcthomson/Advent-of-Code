import sys

with open(sys.argv[1], "r") as f:

    points = 0

    for line in f:
        line = line.strip()
        (_, nums) = line.split(": ")
        (winningnumsstr, mynumsstr) = nums.split(" | ")
        winningnums = winningnumsstr.split()
        winningnums = [int(x) for x in winningnums]
        mynums = mynumsstr.split()
        mynums = [int(x) for x in mynums]

        linepoints = 0
        for m in mynums:
            if m in winningnums:
                if linepoints == 0:
                    linepoints = 1
                else:
                    linepoints *= 2
        points += linepoints
    print(points)