import sys

preamble = 25
numlist  = []
xmas = []

with open(sys.argv[1], "r") as f:
    for line in f:
        numlist.append(int(line.rstrip()))

notsum = False

for num in numlist:
    if len(xmas) < preamble:
        xmas.append(num)
    else:
        sums = []
        for i in range(len(xmas) - preamble, len(xmas)):
            for j in range(len(xmas) - preamble, len(xmas)):
                if i != j:
                    sums.append(xmas[i] + xmas[j])
        if not num in sums:
            notsum = num
            break
        else:
            xmas.append(num)

for segsize in range(2, len(numlist)):
    for i in range(0, len(numlist)):
        segsum = 0
        smallseg = False
        largeseg = 0
        for j in range(i, i + segsize):
            try:
                num = numlist[j]
            except:
                pass
            segsum += num
            if num > largeseg:
                largeseg = num
            if not smallseg or num < smallseg:
                smallseg = num
        if segsum == notsum:
            print(smallseg + largeseg)
            exit()