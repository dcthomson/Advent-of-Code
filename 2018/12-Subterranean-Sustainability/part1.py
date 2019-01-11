import sys

current = dict()
nextgen = dict()
rules = dict()

file = open(sys.argv[1], 'r')

for line in file:
    if line.startswith("initial"):
        initialstate = line.rstrip().split(": ")[1]
        potnum = 0
        currentPot = False
        for c in initialstate:
            current[potnum] = c
            potnum += 1
    
    elif " => " in line:
        (pattern, plant) = line.rstrip().split(" => ")
        rules[pattern] = plant

double = dict()

i = 0
while i < 50000000000:

    print i

    # get current smallest plant index
    # SPEED UP
    smallest = None
    largest  = None
    for k in current:
        if current[k] == "#":
            if smallest is None or k < smallest:
                smallest = k
            if largest is None or k > largest:
                largest = k
#    print "smallest: %s" % (smallest)
#    print "largest:  %s" % (largest)

    print smallest

    # add four empty plants on each end
    for j in range(1, 5):
        if smallest - j not in current:
            current[smallest - j] = "."
        if largest + j not in current:
            current[largest + j] = "."

    # create next gen
    for k in sorted(current):
        if k - 2 in current and k + 2 in current:
            left2 = current[k - 2]
            left1 = current[k - 1]
            right1 = current[k + 1]
            right2 = current[k + 2]
            pattern = left2 + left1 + current[k] + right1 + right2
#            sys.stdout.write(pattern + ": ")
            if pattern in rules:
                nextgen[k] = rules[pattern]
#                print rules[pattern]
            else:
                nextgen[k] = "."
#                print "."
    plantstr = ""
    for k in nextgen:
        plantstr += nextgen[k]
        current[k] = nextgen[k]
    plantstr = plantstr.strip(".")
#    plantstr = str(smallest) + plantstr
    print plantstr
    if plantstr in double:
        print "found dupe: %s and %s smallest %s" % (double[plantstr], i, smallest)
    double[plantstr] = i

    i += 1

total = 0
for k in sorted(current):
    sys.stdout.write(current[k])
    if current[k] == "#":
        total += k
print
print "total: %s" % (total)

