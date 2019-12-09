import sys
import time

# this takes a while, and should all be converted to a linked list instead...


stop = 01245
strstop = str(stop)
stopList = list(strstop)
# stopList = [0,1,2,4,5]
# stopList = [5,1,5,8,9]
# stopList = [9,2,5,1,0]
# stopList = [5,9,4,1,4]
stopList = [5,8,0,7,4,1]
printnums = False

recipes = [3, 7]

elf1 = 0
elf2 = 1

found = False

while not found:
    if printnums:
        for idx, val in enumerate(recipes):
            if idx == elf1 and idx == elf2:
                sys.stdout.write("<")
                sys.stdout.write(str(val))
                sys.stdout.write(">")
            elif idx == elf1:
                sys.stdout.write("(")
                sys.stdout.write(str(val))
                sys.stdout.write(")")
            elif idx == elf2:
                sys.stdout.write("[")
                sys.stdout.write(str(val))
                sys.stdout.write("]")
            else:
                sys.stdout.write(" ")
                sys.stdout.write(str(val))
                sys.stdout.write(" ")
        print

    # add new digit(s)
    newdigit = recipes[elf1] + recipes[elf2]
    if newdigit < 10:
        recipes.append(newdigit)
    else:
        for c in str(newdigit):
            recipes.append(int(c))

    # check for stop in list
#    print "stoplist: %s" % (stopList)
#    print "recipes:  %s" % (recipes[len(recipes) - len(stopList):len(recipes)])
    if stopList == recipes[len(recipes) - len(stopList):len(recipes)]:
        # found it
        back = 0
        found = True
    if stopList == recipes[len(recipes) - len(stopList) - 1:len(recipes) - 1]:
        back = 1
        found = True

    # move elves
    for _ in range(1, recipes[elf1] + 2):
        if elf1 + 1 >= len(recipes):
            elf1 = 0
        else:
            elf1 += 1
    for i in range(1, recipes[elf2] + 2):
        if elf2 + 1 >= len(recipes):
            elf2 = 0
        else:
            elf2 += 1

print len(recipes) - len(stopList) - back

# scores = ""
# for i in range(stop, stop + 10):
#     scores += str(recipes[i])
# print scores
