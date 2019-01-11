import time

file = open("input.txt", "r")

lastletter = ""

for line in file:
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
    print len(line) - 1
