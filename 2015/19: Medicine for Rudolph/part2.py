import sys
from random import shuffle

changes = list()
molecule = ""

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if "=>" in line:
            (start, end) = line.split(" => ")
            changes.append((start, end))
        elif line != "":
            molecule = line

mol = molecule
steps = 0

while True:
    anychanges = False
    for start, end in changes:
        i = 0
        l = len(end)
        while i <= len(mol):
            if mol[i:i + l] == end:
                mol = mol[:i] + start + mol[i + l:]
                steps += 1
                anychanges = True
            if mol == 'e':
                print(steps)
                sys.exit()
            i += 1

    if not anychanges:
        steps = 0
        mol = molecule
        shuffle(changes)