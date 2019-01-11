import sys
import time

stop = 580741

printnums = False

recipes = [3, 7]

elf1 = 0
elf2 = 1

while len(recipes) < stop + 12:
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

scores = ""
for i in range(stop, stop + 10):
    scores += str(recipes[i])
print scores
