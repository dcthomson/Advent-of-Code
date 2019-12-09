import sys

class Range:
    def __init__(self, low, high):
        self.lower = low
        self.higher = high

    def __str__(self):
        return (str(self.lower) + "-" + str(self.higher) )

    def combine(self, r):
        newrange = False
        if self.lower < r.lower:
            if r.lower < self.higher:
                if r.higher < self.higher:
                    # EAT
                    newrange = Range(self.lower, self.higher)
                else:
                    # Make Bigger
                    newrange = Range(self.lower, r.higher)
            elif self.higher + 1 == r.lower:
                newrange = Range(self.lower, r.higher)

        if r.lower < self.lower:
            if self.lower < r.higher:
                if self.higher < r.higher:
                    # EAT
                    newrange = Range(r.lower, r.higher)
                else:
                    # Make Bigger
                    newrange = Range(r.lower, self.higher)
            elif r.higher + 1 == self.lower:
                newrange = Range(r.lower, self.higher)

        if self.lower == r.lower:
            if self.lower < r.lower:
                newrange = Range(self.lower, r.higher)
            else:
                newrange = Range(self.lower, self.higher)
        if self.higher == r.higher:
            if self.lower < r.lower:
                newrange = Range(self.lower, r.higher)
            else:
                newrange = Range(r.lower, r.higher)
        if self.lower == r.higher:
            newrange = Range(r.lower, self.higher)
        if r.lower == self.higher:
            newrange = Range(self.lower, r.higher)
        
        
        return newrange

ranges = []

with open(sys.argv[1]) as f:
    for line in f:
        (start, end) = line.rstrip().split("-")
        start = int(start)
        end = int(end)
        ranges.append(Range(start, end))

oldrangelen = 0
while oldrangelen != len(ranges):
    newranges = False
    oldi = None
    oldj = None
    oldrangelen = len(ranges)
    for i, iv in enumerate(ranges):
        for j, jv in enumerate(ranges):
            if i != j:
                newrange = iv.combine(jv)
                if newrange:
                    # print("converting:", iv, "and", jv, "->", newrange)
                    oldi = i
                    oldj = j
                    break
        else:
            continue
        break

    if oldi is not None and oldj is not None:
        if oldi > oldj:
            del ranges[oldi]
            del ranges[oldj]
        elif oldi < oldj:
            del ranges[oldj]
            del ranges[oldi] 
        ranges.append(newrange)


totalpossible = 4294967296
blacklisted = 0

for r in ranges:
    blacklisted += r.higher - r.lower + 1

print(totalpossible - blacklisted)

# anotherRange = True

# while anotherRange:
#     anotherRange = False
    

#     for r in ranges: 
# print(low)
# print(high)

# for r in ranges:
#     if r.lower == high + 1:
#         print(r)