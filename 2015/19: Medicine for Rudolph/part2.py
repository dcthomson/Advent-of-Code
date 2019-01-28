import sys

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

def changemolecule(mol, steps):
#    print("mol:", mol)
    if mol in molecules and steps >= molecules[mol]:
        return
    molecules[mol] = steps
    for start in changes:
        i = 0
#        print(start)
        while i <= len(mol):
            for replacement in changes[start]:
                l = len(replacement)
                if replacement == mol[i:i + l]:
                    front = mol[:i]
                    back = mol[i + l:]
                    # print(mol)
                    # print(front, start, back)
                    # print()
                    newmol = front + start + back
                    if newmol == 'e':
                        print("steps", steps + 1)
                    else:
                        changemolecule(newmol, steps + 1)
            i += 1

changemolecule(molecule, 0)