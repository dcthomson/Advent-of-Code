file = open("input.txt", "r")

boxlist = list()

strsize = 0

for line in file:
    if len(line) > strsize:
        strsize = len(line)
    boxlist.append(line)

foundit = 0
smallerbox = ""
for i in range(strsize):
    boxdict = dict()
    for box in boxlist:
        smallerbox = box[:i] + box[i + 1:]
        if smallerbox in boxdict:
            foundit = 1
            break
        boxdict[smallerbox] = 1
    if foundit:
        break

print "commonletters:", str(smallerbox)
