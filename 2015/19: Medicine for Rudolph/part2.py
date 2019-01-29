import sys

molecule = ""
molecules = dict()
changes = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if " => " in line:
            (start, end) = line.split(" => ")

            changes.append((end, start))
        elif line != "":
            molecule = line

# lets change big substrings first
changes.sort(key=lambda tup: len(tup[0]), reverse=True)

molecules = dict()

def changemolecule(mol, steps):
#    print("mol:", mol)
    if mol in molecules and steps >= molecules[mol]:
        return
    molecules[mol] = steps
    for (end, start) in changes:
        i = 0
#        print(start)
        while i <= len(mol):
            l = len(end)
            if end == mol[i:i + l]:
                front = mol[:i]
                back = mol[i + l:]
#                print(mol, "--", end, "->", start, "--", front, start, back)
#                print()
                newmol = front + start + back
                if newmol == 'e':
                    print("steps", steps + 1)
                else:
                    changemolecule(newmol, steps + 1)
            i += 1
#        print("NOTHING ELSE TO CHANGE")

changemolecule(molecule, 0)