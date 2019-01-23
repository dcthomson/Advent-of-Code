import sys

containers = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        containers.append(int(line.strip()))

goal = 150

containercombinations = list()

import copy

def combinations(target, data, goal, containercombinations):
    if sum(target) > goal:
        return containercombinations
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        if sum(new_target) == goal:
            containercombinations.append(new_target)
#            print(new_target)
        containercombinations = combinations(new_target, new_data, goal, containercombinations)
    return containercombinations

target = []
containercombinations = combinations(target, containers, goal, containercombinations)

smallest = False
for cc in containercombinations:
    if not smallest or len(cc) < smallest:
        smallest = len(cc)

count = 0
for cc in containercombinations:
    if len(cc) == smallest:
        count += 1
print(count)