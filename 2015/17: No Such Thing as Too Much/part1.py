import sys

containers = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        containers.append(int(line.strip()))

#containers = [20, 15, 10, 5, 5]

goal = 150

count = 0

import copy
def combinations(target,data, goal, count):
    if sum(target) > goal:
        return count
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_data = copy.copy(data)
        new_target.append(data[i])
        new_data = data[i+1:]
        if sum(new_target) == goal:
            count += 1
#            print(new_target)
        count = combinations(new_target, new_data, goal, count)
    return count

target = []
print(combinations(target, containers, goal, count))