import time

searching = 1

freq = 0

freqdict = dict()

while searching:

    file = open("frequencies.txt", "r")

    for line in file:

        if freq in freqdict:
            print "found it!: ", str(freq)

            break
        freqdict[freq] = 1
    
        num = int(line[1:])

        if line[0] == "+":
            freq += num
        else:
            freq -= num

    file.close()
