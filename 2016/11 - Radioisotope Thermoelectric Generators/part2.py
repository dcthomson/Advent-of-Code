from itertools import combinations
import os
import sys


class ElevatorSystem:
    def __init__(self, stuff, elevator=1, move=0):
        self.move = move
        self.elevator = elevator
        self.stuff = stuff

    def stringify(self):
        retstr = "E" + str(self.elevator)
        for k in sorted(self.stuff):
            retstr += "-" + k + str(self.stuff[k])
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
                if self.stuff[k] == f:
                    retstr += k
                else:
                    retstr += ".  "
                retstr += " "
            retstr += "\n"
            
        return retstr.rstrip()

    def checkValidity(self, oldfloor):
        # floors = {}
        # for k, v in self.stuff.items():
        #     if v not in floors:
        #         floors[v] = {"microchips": [], "generators": []}
        #     if k[-1] == "M":
        #         floors[v]["microchips"].append(k[:-1])
        #     else:
        #         floors[v]["generators"].append(k[:-1])
        # for floor in (self.elevator, oldfloor):
        #     if floor in floors:
        #         gens = len(floors[floor]["generators"])
        #         micros = len(floors[floor]["microchips"])
        #         if gens != 0 and micros != 0:
        #             for n in floors[floor]["microchips"]:
        #                 if n not in floors[floor]["generators"]:
        #                     if gens >= 1:
        #                         return False
        # return True

        # check for microchips without generators
        for k, v in self.stuff.items():
            # only check this floor and previous floor
            # other floors have not changed
            if v == oldfloor or v == self.elevator:
                if k[-1] == "M":
                    name = k[:-1]
                    if v != self.stuff[name + "G"]:
                        # microchip is not with its generator
                        for k2, v2 in self.stuff.items():
                            if k2[-1] == "G" and v2 == v:
                                return False
        return True
            




       


    def getNextMoves(self):
        moves = []
        
        stuffonfloor = []
        for k, v in self.stuff.items():
            if v == self.elevator:
                stuffonfloor.append(k)
        for j in (1, -1):
            newfloor = self.elevator + j
            if newfloor in (1, 2, 3, 4):
                for i in (1, 2):
                    comb = combinations(stuffonfloor, i)
                    for c in list(comb):
                        stuff = self.stuff.copy()
                        for thing in c:
                            stuff[thing] = newfloor
                        es = ElevatorSystem(stuff, newfloor, self.move + 1)
                        # print(es)
                        if es.checkValidity(self.elevator):
                            moves.append(es)
                        # print()
        return moves

    def allup(self):
        for _, v in self.stuff.items():
            if v != 4:
                return False
        return True
                

stuff = {}


with open(sys.argv[1]) as f:
    for line in f:
        floor, name, t = line.rstrip().split()
        stuff[name + t] = int(floor)

es = ElevatorSystem(stuff)

visited = {}

Q = [es]

while Q:
    v = Q.pop(0)
    if v.allup():
        print(v.move)
        break
    for n in v.getNextMoves():
        nstr = n.stringify()
        if nstr not in visited:
            Q.append(n)
            visited[nstr] = True