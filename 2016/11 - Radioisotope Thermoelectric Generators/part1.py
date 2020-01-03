# 1 PRG PRM
# 2 COG CUG RUG PLG
# 3 COM CUM RUM PLM
# 4
from itertools import combinations
import os


class ElevatorSystem:
    def __init__(self, stuff, elevator=1, visited=[]):
        self.floors = [1, 2, 3, 4]
        self.elevator = elevator
        self.stuff = stuff
        self.visited = visited.copy()
        self.visited.append(self.stringify())

    def stringify(self):
        retstr = "E" + str(self.elevator)
        for k in sorted(self.stuff):
            retstr += "-" + k + str(self.stuff[k])
        return retstr

    def printsteps(self):
        strs = None
        for s in self.visited:
            strs = s.split("-")
            stuff = {}
            for s in strs:
                stuff[s[:-1]] = int(s[-1])
            for f in range(4, 0, -1):
                print("F" + str(f) + " ", end="")
                for k in sorted(stuff):
                    if k == "E":
                        if stuff[k] == f:
                            print("E ", end="")
                        else:
                            print(". ", end="")
                    else:
                        if stuff[k] == f:
                            print(k, end="")

                        else:
                            print(".  ", end="")
                    print(" ", end="")

                print()
            print()


        

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
            if newfloor in self.floors:
                for i in (1, 2):
                    comb = combinations(stuffonfloor, i)
                    for c in list(comb):
                        stuff = self.stuff.copy()
                        for thing in c:
                            stuff[thing] = newfloor
                        es = ElevatorSystem(stuff, newfloor, self.visited.copy())
                        if es.checkValidity():
                            moves.append(es)
        return moves

    def allup(self):
        for _, v in self.stuff.items():
            if v != 4:
                return False
        return True
                

# stuff = {}
# stuff['HG'] = 2
# stuff['HM'] = 1
# stuff['LG'] = 3
# stuff['LM'] = 1

# 1 PRG PRM
# 2 COG CUG RUG PLG
# 3 COM CUM RUM PLM
# 4

stuff = {}
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

print(es)

print(es.visited)
print()

# for m in es.getNextMoves():
#     print(m)
#     print(m.visited)
#     print()

visited = {}

Q = [es]

while Q:
    v = Q.pop(0)
    # os.system('cls||clear')
    # print(v)
    # print(v.visited)
    if v.allup():
        print(len(v.visited) - 1)
        # print(v.visited)
        # v.printsteps()
        break
    for n in v.getNextMoves():
        if n.stringify() not in v.visited:
            Q.append(n)



    # visited[str(elevator) + stringify(stuff)] = True
    # move = Q.pop(0)
