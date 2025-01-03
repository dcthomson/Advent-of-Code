import sys
import copy

mps = []

class Mirrorpatch():

    def __init__(self, h, v):
        self.vert = v
        self.horiz = h
        self.oldfold = False

    def __str__(self):
        retstr = ""
        retstr += "\n".join(self.horiz)
        return retstr

    def findhorizontalfold(self):
        foldfound = False
        for n, l in enumerate(self.horiz):
            try:
                if self.horiz[n] == self.horiz[n+1]:
                    foldfound = n + 1
                    for i in range(0, len(self.horiz)):
                        if self.horiz[n-i] != self.horiz[n+1+i]:
                            foldfound = False
                            break
                        if n-i == 0:  # need to check cuz python neg indexes
                            return foldfound
            except IndexError:
                return foldfound
        return foldfound
    
    def findverticalfold(self):
        foldfound = False
        for n, l in enumerate(self.vert):
            try:
                if self.vert[n] == self.vert[n+1]:
                    foldfound = n + 1
                    for i in range(0, len(self.vert)):
                        if self.vert[n-i] != self.vert[n+1+i]:
                            foldfound = False
                            break
                        if n-i == 0:  # need to check cuz python neg indexes
                            return foldfound
            except IndexError:
                return foldfound
        return foldfound
    
    def flipsmudge(x, y):
        
horiz = []
vert = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if line == "":
            mps.append(Mirrorpatch(horiz, vert))
            horiz = []
            vert = []          
        else:
            horiz.append(line)
        for i, c in enumerate(line):
            try:
                vert[i] += c
            except IndexError:
                vert.append(c)
    mps.append(Mirrorpatch(horiz, vert))

total = 0

for mp in mps:
    mirrornum = 0
    hf = mp.findhorizontalfold()
    if hf:
        mp.oldfold = "H" + str(hf)
    vf = mp.findverticalfold()
    if vf:
        mp.oldfold = "V" + str(vf)

for mp in mps:
    mpcopy = copy.deepcopy(mp)
    for each coord in grid:
        change coord
        mtotal =0
        hf = mp.findhorizontalfold()
        if hf:
            mtotal += 100 * hf
        vf = mp.findverticalfold()
        if vf:
            mtotal += vf
        if mtotal:
            total += mtotal
            break
    

print(total)