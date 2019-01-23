import sys
import re

molecule = ""
molecules = dict()
changes = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if " => " in line:
            (start, end) = line.split(" => ")
            if start not in changes:
                changes[start] = list()
            changes[start].append(end)
        elif line != "":
            molecule = line

molecules = dict()

for start in changes:
    i = 0
    while i <= len(molecule):
        l = len(start)
        if start == molecule[i:i + l]:
            for replacement in changes[start]:
                front = molecule[:i]
                back = molecule[i + l:]
                if front + replacement + back not in molecules:
                    molecules[front + replacement + back] = 1
                else:
                    molecules[front + replacement + back] += 1

        i += 1

print(len(molecules))
