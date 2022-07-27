import sys

prevone = False
prevtwo = False
prevthree = False
one = False
two = False
three = False

largercount = 0

prevsum = 0
sum = 0

with open(sys.argv[1], "r") as f:

    for line in f:
        i = int(line)

        three = i
        if prevone:
            prevsum = prevone + prevtwo + prevthree
            sum = one + two + three

            if sum > prevsum:
                largercount += 1
        prevone = one
        prevtwo = two
        one = two
        two = three
        prevthree = three

print(largercount)