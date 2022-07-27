import sys

low = False
high = False

horizontalpositions = list()

with open(sys.argv[1], "r") as f:
    for line in f:
        for num in line.rstrip().split(','):
            num = int(num)
            if not low or num < low:
                low = num
            if not high or num > high:
                high = num
            horizontalpositions.append(num)

totals = dict()

for i in range(low, high + 1):
    fuel = 0
    for hpos in horizontalpositions:
        fuel += abs(hpos - i)
    totals[i] = fuel

lowest = False

for k in totals:
    if not lowest or totals[k] < lowest:
        lowest = totals[k]

print(lowest)