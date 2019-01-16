import sys

input = sys.argv[1]

currentnum = False

numstr = input
count = False

for i in range(0, 50):
    newnumstr = ""
    for c in numstr:
        if not currentnum or c != currentnum:
            if count:
                newnumstr += str(count) + currentnum
            currentnum = c
            count = 1
        else:
            count += 1
    if count:
        newnumstr += str(count) + currentnum
    numstr = newnumstr
    currentnum = False
    count = False

print(len(numstr))