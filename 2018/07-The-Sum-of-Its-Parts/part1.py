from string import ascii_uppercase
import sys
    
file = open(sys.argv[1], "r")

steps = dict()

for line in file:

    after = line[5]
    before = line[36]

    if not before in steps:
        steps[before] = after
    else:
        steps[before] = steps[before] + after

order = ""

while len(steps) > 0:
#    for key in sorted(steps):
#        print key + ": " + steps[key]

    for atoz in ascii_uppercase:
        if atoz not in steps and atoz not in order:
            order = order + atoz 
            stepstodelete = ""
            for k in steps:
                steps[k] = steps[k].replace(atoz, "")
                if steps[k] == "":
                    stepstodelete = stepstodelete + k
#            print "stepstodelete: " + stepstodelete
            for c in stepstodelete:
                del steps[c]
            break
#    print "order: " + order

for atoz in ascii_uppercase:
    if atoz not in order:
        order = order + atoz

print "order: " + order
