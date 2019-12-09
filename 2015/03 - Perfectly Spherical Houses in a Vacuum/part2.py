import sys

santa = dict()
santa[0] = [0, 0]
santa[1] = [0, 0]
s = 1

deliveries = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        for dir in line:
            if s:
                s = 0
            else:
                s = 1
            if (santa[s][0], santa[s][1]) in deliveries:
                deliveries[(santa[s][0], santa[s][1])] += 1
            else:
                deliveries[(santa[s][0], santa[s][1])] = 1
            if dir == "^":
                santa[s][1] += 1
            elif dir == "v":
                santa[s][1] -= 1
            elif dir == ">":
                santa[s][0] += 1
            elif dir == "<":
                santa[s][0] -= 1

print(len(deliveries))