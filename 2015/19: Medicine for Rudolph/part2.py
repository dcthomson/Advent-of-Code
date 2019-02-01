import sys

molecule = ""
changes = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if " => " in line:
            (start, end) = line.split(" => ")

            changes.append((start, end))
        elif line != "":
            molecule = line

# lets change big substrings first
changes.sort(key=lambda tup: len(tup[1]), reverse=True)

molecules = dict()

def changemolecule(mol, steps):
#    if mol in molecules and steps >= molecules[mol]:
    if mol in molecules and steps >= molecules[mol]:
        molecules[mol] += 1
#        print("DUPLICATE: ", molecules[mol], "      ", mol)
        return
    else:
        molecules[mol] = 1
    for (start, end) in changes:
        i = 0
#        print(start)
        while i <= len(mol):
            l = len(end)
            if end == mol[i:i + l]:
                newmol = mol[:i] + start + mol[i + l:]
                if newmol == 'e':
                    print("steps", steps + 1)
                else:
                    changemolecule(newmol, steps + 1)
            i += 1
#        print("NOTHING ELSE TO CHANGE")

changemolecule(molecule, 0)