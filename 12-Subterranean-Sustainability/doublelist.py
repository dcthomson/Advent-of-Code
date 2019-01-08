import sys

class Doublelist:

    def __init__(self):
        self.pos = list()
        self.neg = list()
        self.current = None

    def append(self, item):
        self.pos.append(item)

    def lappend(self, item):
        self.neg.append(item)

    def set(self, index, item):
        if index >= 0:
            print "index: %s" % (index)
            print "item:  %s" % (item)
            self.pos[index] = item
        else:
            self.neg[abs(index)] = item

    def get(self, index):
        if index >= 0:
            return self.pos[index]
        else:
            return self.neg[abs(index)]

    def getStart(self):
        return len(self.neg) * -1

    def getLast(self):
        return len(self.pos)

    def __iter__(self):
        return self

    def next(self):
        if self.current is None:
            self.current = self.getStart()
        if self.current > self.getLast():
            raise StopIteration
        else:
            if self.current < 0:
                return self.neg[abs(self.current)]
            else:
                return self.pos[self.current]

current = Doublelist()
nextgen = Doublelist()
rules = dict()

file = open(sys.argv[1], 'r')

for line in file:
    if line.startswith("initial"):
        initialstate = line.rstrip().split(": ")[1]
        potnum = 0
        for c in initialstate:
            current.append(c)
            potnum += 1

    elif " => " in line:
        (pattern, plant) = line.rstrip().split(" => ")
        rules[pattern] = plant

for i in current:
    print i
