from string import ascii_lowercase

file = open("input.txt", "r")

for l in file:

    polydict = dict()

    for atoz in ascii_lowercase:
        print "running: " + atoz.upper()
        line = l
        line = line.replace(atoz, "")
        line = line.replace(atoz.upper(), "")

        endreached = 0
        while not endreached:
            index = 0
            lastletter = ""
            for c in line:
                if lastletter != c and lastletter.upper() == c.upper():
                    lastindex = index - 1
                    nextindex = index + 1
                    line = line[:lastindex] + line[nextindex:]
                    break
                lastletter = c
                index += 1
            else:
                endreached = 1

        polydict[atoz] = len(line) - 1
        print polydict

    value = -1
    smallest = ""
    for key in polydict:
        if value == -1:
            value = polydict[key]
            smallest = key

    print "smallest is: " + (str)smallest + " - " + (str)value
