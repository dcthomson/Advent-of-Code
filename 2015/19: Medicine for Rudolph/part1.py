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

print(changes)
print(molecule)

for start in changes:
    i = 0
    while i <= len(molecule):
        l = len(start)
        if start == molecule[i, i + l - 1]:


        i += 1
        for end in changes[start]:

