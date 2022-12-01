import sys

with open(sys.argv[1], "r") as f:

    calorielist = []
    calories = 0
    for line in f:
        line = line.strip()
        if line == "":
            calorielist.append(calories)
            calories = 0
        else:
            calories += int(line)
    if calories != 0:
        calorielist.append(calories)
calorielist.sort()
totalcalories = 0
for i in calorielist[-3:]:
    totalcalories += i
print(totalcalories)