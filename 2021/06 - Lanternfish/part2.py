import sys

fish = {0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0}

with open(sys.argv[1], "r") as f:

    for line in f:
        for num in line.rstrip().split(','):
            fish[int(num)] += 1

newfish = dict()
days = 256

for day in range(1, days+1):
    newfish = fish.copy()
    for i in range(8, -1, -1):
        if i != 0:
            newfish[i-1] = fish[i]
            if i == 8:
                newfish[8] = 0
        else:
            newfish[6] += fish[i]
            newfish[8] += fish[i]
    fish = newfish.copy()
totalfish = 0
for k in fish:
    totalfish += fish[k]
print(totalfish)