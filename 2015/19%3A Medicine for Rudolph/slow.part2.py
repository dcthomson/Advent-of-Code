import sys

molecule = ""
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

def changemolecule(mol, molecule, steps, mollen):
    print(mol)
    for start in changes:
        i = 0
#        print(start)
        while i <= len(mol):
            l = len(start)
            if start == mol[i:i + l]:
                for replacement in changes[start]:
                    front = mol[:i]
                    back = mol[i + l:]
                    newmol = front + replacement + back
                    if len(newmol) > mollen:
                        continue
                    if newmol == molecule:
                        print("steps", steps + 1)
                    else:
                        changemolecule(newmol, molecule, steps + 1, mollen)
            i += 1

changemolecule('e', molecule, 0, len(molecule))