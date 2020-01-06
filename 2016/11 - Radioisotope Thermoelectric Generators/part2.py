from itertools import combinations
import os


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

    # def __str__(self):
    #     retstr = ""
    #     for f in range(4, 0, -1):
    #         retstr += "F" + str(f) + " "
    #         if self.elevator == f:
    #             retstr += "E"
    #         else:
    #             retstr += "."
    #         retstr += "  "
    #         for k in sorted(self.stuff):
    #             if self.stuff[k] == f:
    #                 retstr += k
    #             else:
    #                 retstr += ".  "
    #             retstr += " "
    #         retstr += "\n"
            
    #     return retstr.rstrip()

    def checkValidity(self):
        # check for microchips without generators
        for k, v in self.stuff.items():
            if k.endswith("M"):
                name = k.rstrip("M")
                if v != self.stuff[name + "G"]:
                    # microchip is not with its generator
                    for k2, v2 in self.stuff.items():
                        if k2.endswith("G") and v2 == v:
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
                        if es.checkValidity():
                            moves.append(es)
        return moves

    def allup(self):
        for _, v in self.stuff.items():
            if v != 4:
                return False
        return True
                

stuff = {}



# stuff['HG'] = 2
# stuff['HM'] = 1
# stuff['LG'] = 3
# stuff['LM'] = 1

# 1 PRG PRM ELG ELM DIG DIM
# 2 COG CUG RUG PLG
# 3 COM CUM RUM PLM
# 4

stuff['ELG'] = 1
stuff['ELM'] = 1
stuff['DIG'] = 1
stuff['DIM'] = 1
stuff['PRG'] = 1
stuff['PRM'] = 1
stuff['COG'] = 2
stuff['CUG'] = 2
stuff['RUG'] = 2
stuff['PLG'] = 2
stuff['COM'] = 3
stuff['CUM'] = 3
stuff['RUM'] = 3
stuff['PLM'] = 3

es = ElevatorSystem(stuff)

visited = {}

Q = [es]

while Q:
    v = Q.pop(0)
    # os.system('cls||clear')
    # print(v)
    # print(v.visited)
    if v.allup():
        print(v.move)
        # print(v.visited)
        # v.printsteps()
        break
    for n in v.getNextMoves():
        if n.stringify() not in visited:
            Q.append(n)
            visited[n.stringify()] = True



    # visited[str(elevator) + stringify(stuff)] = True
    # move = Q.pop(0)
