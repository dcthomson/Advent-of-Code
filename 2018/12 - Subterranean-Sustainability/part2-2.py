string = "#...#...#...#...#...#...#...#......#....#...#...#...#...#...#....#...#...#...#...#...#....#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#...#....#....#...#...#...#"

indexlist = [i for i, ltr in enumerate(string) if ltr == "#"]

print indexlist

addamount = 50000000000 - 90

total = 0
for i in indexlist:
    print "total: %s" % (total)
    total += addamount + i

print total
