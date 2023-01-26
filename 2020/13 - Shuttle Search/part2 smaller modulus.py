import sys

earliest = 0
buses = []
lines = []

with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line)

    numdict = {}
    numlist = []
    try:
        numlist = lines[1].split(',')
    except:
        numlist = lines[0].split(',')
    largest = 0
    for i in range(0, len(numlist)):
        if numlist[i] != "x":
            num = int(numlist[i])
            numdict[num] = [i, 0]
            if num > largest:
                largest = num


print(largest, numdict)

i = 0
found = False

while not found:
    if i % 10000000 == 0:
        print("{:,}".format(i))
    i += largest
    found = True
    for k in numdict:
        if k != largest:
            if (i - numdict[k][1] (numdict[largest][0] - numdict[k][0])) % k != 0:
                found = False
                # break
            else:
                numdict[k][1] 
smallest = i
b = 0
for k in numdict:
    if smallest > i - (numdict[largest] - numdict[k]):
         smallest = i - (numdict[largest] - numdict[k])
print(smallest)