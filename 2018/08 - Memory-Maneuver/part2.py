# create nodes recursively and return node amount

import sys

file = open("input.txt", "r")

input = list()

for line in file:
    input = map(int, line.split())

def getNode(input, indent=0):
    numofchildnodes = input.pop(0)
    numofmetadataentries = input.pop(0)
    totalvalue = 0
    children = list()
    for _ in range(1, numofchildnodes + 1):
        (input, value) = getNode(input, indent + 1)
        children.append(value)
    for i in range(0, numofmetadataentries):
        metaref = input.pop(0)
        if numofchildnodes == 0:
            totalvalue += metaref
        else:
            try:
                totalvalue += children[metaref - 1]
            except IndexError:
                pass
    return(input, totalvalue)

print getNode(input)[1]
