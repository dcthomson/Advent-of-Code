from itertools import combinations
import os
import copy
import sys


class Item:
    def __init__(self, name, itemtype, floor):
        self.name = name
        self.type = itemtype
        self.floor = floor
        self.generator = None

    def setbuddygenerator(self, items):
        if self.type == "M":
            for _, v in items.items():
                if v.name == self.name:
                    if v.type == "G":
                        self.generator = v

    def __str__(self):
        return str(self.name) + str(self.type) + str(self.floor)


class ElevatorSystem:
    def __init__(self, stuff, elevator=1, move=0):
        self.move = move
        self.elevator = elevator
        self.stuff = stuff

    # def __str__(self):
    #     return self.stringify()

    def stringify(self):
        retstr = "E" + str(self.elevator)
        for k in sorted(self.stuff.keys()):
            v = self.stuff[k]
            retstr += "-" + v.name + v.type + str(v.floor)
        return retstr

    def __str__(self):
        retstr = ""
        for f in range(4, 0, -1):
            retstr += "F" + str(f) + " "
            if self.elevator == f:
                retstr += "E"
            else:
                retstr += "."
            retstr += "  "
            for k in sorted(self.stuff):
                if self.stuff[k].floor == f:
                    retstr += k
                else:
                    retstr += ".  "
                retstr += " "
            retstr += "\n"
            
        return retstr.rstrip()

    def checkValidity(self):
        # check for microchips without generators
        for _, v in self.stuff.items():
            if v.type == "M":
                # if v.generator is not None:
                    if v.floor != v.generator.floor:
                        for _, i2 in self.stuff.items():
                            if i2.type == "G" and i2.floor == v.floor:
                                return False
        return True
                
        # for k, v in self.stuff.items():
        #     if k.endswith("M"):
        #         name = k.rstrip("M")
        #         if v != self.stuff[name + "G"]:
        #             # microchip is not with its generator
        #             for k2, v2 in self.stuff.items():
        #                 if k2.endswith("G") and v2 == v:
        #                     return False
        # return True


    def getNextMoves(self):
        moves = []
        
        stuffonfloor = []
        for _, v in self.stuff.items():
            if v.floor == self.elevator:
                stuffonfloor.append(v)
        for j in (1, -1):
            newfloor = self.elevator + j
            if newfloor in (1, 2, 3, 4):
                for combnum in (1, 2):
                    comb = combinations(stuffonfloor, combnum)
                    for c in list(comb):
                        stuff = copy.deepcopy(self.stuff)
                        for item in c:
                            stuff[item.name + item.type] = Item(item.name, item.type, newfloor)
                        for _, v in stuff.items():
                            v.setbuddygenerator(stuff)
                        es = ElevatorSystem(stuff, newfloor, self.move + 1)
                        if es.checkValidity():
                            moves.append(es)
        return moves

    def allup(self):
        for _, v in self.stuff.items():
            if v.floor != 4:
                return False
        return True
                

stuff = {}

with open(sys.argv[1]) as f:
    for line in f:
        floor, name, t = line.rstrip().split()
        stuff[name + t] = Item(name, t, int(floor))

for _, v in stuff.items():
    v.setbuddygenerator(stuff)

es = ElevatorSystem(stuff)

visited = {es.stringify(): True}

Q = [es]

count = 0

while Q:
    # print(len(Q))
    count += 1
    v = Q.pop(0)
    if v.allup():
        print(v.move)
        # v.printsteps()
        break
    # print(visited)
    for n in v.getNextMoves():
        nstr = n.stringify()
        if nstr not in visited:
            Q.append(n)
            visited[nstr] = True