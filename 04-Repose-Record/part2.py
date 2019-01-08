file = open("input.txt", "r")

input = dict()

for line in file:
    (ymdhs, data) = line.split("] ")
    ymdhs = ymdhs.lstrip("[")
    input[ymdhs] = data

guardtotal = dict()
guarddata = dict()
guard = 0
sleepstartmin = 0

for key in sorted(input.iterkeys()):
    (date, time) = key.split()
    (hour, minute) = time.split(":")    
    if int(hour) != 00:
        minute = "00"

    if input[key].startswith("Guard"):
        (_, guard) = input[key].split("#")
        (guard, _) = guard.split(" ", 1)

    if input[key].startswith("falls"):
        sleepstartmin = minute

    if input[key].startswith("wakes"):
        for i in range(int(sleepstartmin), int(minute)):
            if guard in guardtotal:
                guardtotal[guard] += 1
            else:
                guardtotal[guard] = 1
            key = guard + "-" + str(i)
            if key in guarddata:
                guarddata[key] += 1
            else:
                guarddata[key] = 1

minutesofsleep = 0
sleepiestguard = 0
sleepiestminute = ""
for key in guarddata:
    if guarddata[key] > minutesofsleep:
        minutesofsleep = guarddata[key]
        (sleepiestguard, sleepiestminute) = key.split("-")

print str(int(sleepiestguard) * int(sleepiestminute))
