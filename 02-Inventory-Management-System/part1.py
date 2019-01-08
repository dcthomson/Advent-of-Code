file = open("input.txt", "r")

two = 0
three = 0

for line in file:
    chardict = dict()
    for c in line:
        if c in chardict:
            chardict[c] += 1
        else:
            chardict[c] = 1

    mytwo = 0
    mythree = 0
    for key in chardict:
        if chardict[key] == 2:
            mytwo = 1
        elif chardict[key] == 3:
            mythree = 1

    if mytwo:
        two += 1
    if mythree:
        three += 1

checksum = two * three
print "checksum: ", str(checksum)
