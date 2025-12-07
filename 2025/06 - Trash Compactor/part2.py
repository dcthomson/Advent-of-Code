import sys

with open(sys.argv[1], "r") as f:

    grid = {}

    xmax = ymax = y = 0

    for line in f:
        x = 0
        line = line.strip('\n')
        for c in line:
            grid[(x,y)] = c
            if x > xmax:
                xmax = x
            x += 1
        if y > ymax:
            ymax = y
        y += 1

    total = problemtotal = 0

    for x in range(0, xmax + 1):
        if grid[(x, ymax)] in "*+":
            total += problemtotal
            problemtotal = 0
            addormultiply = grid[(x, ymax)]
        verticalnum = ""
        for y in range(0, ymax):
            if grid[(x,y)] not in " +*":
                verticalnum += grid[(x, y)]
        # print("vertnum:", verticalnum)
        if verticalnum != "":
            if problemtotal == 0:
                problemtotal = int(verticalnum)
            else:
                if addormultiply == "*":
                    problemtotal *= int(verticalnum)
                elif addormultiply == "+":
                    problemtotal += int(verticalnum)

            # print("probtotal:", problemtotal)

    total += problemtotal

    print(total)