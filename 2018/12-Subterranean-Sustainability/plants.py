import sys

file = open("input.txt", "r")

class pot:
    def __init__(self, id, plant):
        self.id = id
        self.plant = plant
        self.nextGen = ""

    def createNextGen(self, pots, rules):
        fivepots = ""
        for i in range(self.id - 2, self.id + 3):
            fivepots += pots[i].plant.rstrip()
#        print "fivepots: " + fivepots
        try:
            self.nextGen = rules[fivepots]
        except KeyError:
            pass
#            print self
#            print "fivepots: " + fivepots
#            print

    def moveGen(self):
        self.plant = self.nextGen

    def __str__(self):
        retstr = "id: " + str(self.id) + "   plant: " + self.plant.rstrip()
        if self.nextGen != "":
            retstr += " -> " + self.nextGen.rstrip()
        return retstr



state = ""
rules = dict()

# get input
for line in file:
    if line.startswith("initial state"):
        (_, state) = line.split(": ")
    elif " => " in line:
        (rule, outcome) = line.split(" => ")
        rules[rule] = outcome

# set pots
pots = dict()
i = 0
for c in state:
    if c == '.' or c == '#':
        pots[i] = pot(i, c)
        i += 1

for _ in range(0, 22):
    # get first pot with a plant
    # so we can add some padding
    firstplant = None
    for k in sorted(pots.iterkeys()):
        if pots[k].plant.rstrip() == "#":
            firstplant = k
            break
    for j in range(firstplant - 4, firstplant):
        if j not in pots:
            pots[j] = pot(j, ".")

    # do the same for the end
    lastplant = None
    for k in sorted(pots.iterkeys(), reverse=True):
        if pots[k].plant.rstrip() == "#":
            lastplant = k
            break
    for j in range(lastplant, lastplant + 4):
        if j not in pots:
            pots[j] = pot(j, ".")

    #for k in sorted(pots.iterkeys()):
    #    print pots[k]

    # create next gen
    for k in pots:
        if k - 2 in pots:
            if k + 2 in pots:
                pots[k].createNextGen(pots, rules)

    # move to next gen
    for k in pots:
        pots[k].moveGen()

    # print
#    for k in sorted(pots.iterkeys()):
#        sys.stdout.write(pots[k].plant.rstrip())
#        sys.stdout.flush()
#    print
#    for k in sorted(pots.iterkeys()):
#        sys.stdout.write(pots[k].nextGen.rstrip())
#        sys.stdout.flush()
#    print

    total = 0
    for k in pots:
        if pots[k].plant.rstrip() == "#":
            total += k

    print "total: " + str(total)
