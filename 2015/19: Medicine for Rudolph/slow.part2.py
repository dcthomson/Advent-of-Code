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

def changemolecule(mol, molecule, steps):
#    print("mol:", mol)
    if len(mol) > len(molecule):
        return
    for start in changes:
        i = 0
#        print(start)
        while i <= len(mol):
            l = len(start)
            if start == mol[i:i + l]:
                for replacement in changes[start]:
                    front = mol[:i]
                    back = mol[i + l:]
                    mol = front + replacement + back
                    if mol == molecule:
                        print("steps", steps)
                    else:
                        changemolecule(mol, molecule, steps + 1)
            i += 1

changemolecule('e', molecule, 0)