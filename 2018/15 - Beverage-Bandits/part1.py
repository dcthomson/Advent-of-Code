import sys

import operator

file = open(sys.argv[1], "r")

class Unit:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
        self.alive = True
        self.distances = dict()
        self.closestEnemyAdj = False # (x, y, count)

    def __str__(self):
        retstr = ""
        if self.char == "G":
            retstr += "Goblin"
        elif self.char == "E":
            retstr += "Elf"
        retstr += ": (" + str(self.x) + ", " + str(self.y) + ")"
        retstr += " hp-" + str(self.hp)
        return retstr

    def __lt__(self, other):
        if self.y < other.y:
            return True
        elif self.y > other.y:
            return False
        else:
            if self.x < other.x:
                return True
            else:
                return False

    def attack(self, enemy, board):
        enemy.hp -= 3
        if enemy.hp <= 0:
            enemy.alive = False
            board.grid[(enemy.x, enemy.y)] = "."

    def getAdjacents(self, board):
        return board.getAdjacents((self.x, self.y))

    def dirToClosestEnemy(self, board):
        queue = [((self.x, self.y), False, 1)]
        visited = {}
        first = True
        foundlevel = False
        possiblesquares = []
        while len(queue):
            current = queue.pop(0)
            if foundlevel and current[2] > foundlevel:
                firstsquare = False
                for square in possiblesquares:
                    if not firstsquare:
                        firstsquare = square
                    else:
                        if square[0][1] < firstsquare[0][1]:
                            firstsquare = square
                        elif square[0][1] == firstsquare[0][1]:
                            if square[0][0] < firstsquare[0][0]:
                                firstsquare = square
                return firstsquare[1]
            for adj in board.getAdjacents(current[0]):
                if board.grid[adj] == ".":
                    if adj not in visited:
                        if first:
                            visited[adj] = adj
                            queue.append((adj, adj, current[2] + 1))
                        else:
                            visited[adj] = current[1]
                            queue.append((adj, current[1], current[2] + 1))
                elif board.grid[adj] == self.enemy:
                    if not foundlevel:
                        foundlevel = current[2]
                    possiblesquares.append(current)
            first = False
        if foundlevel:
            firstsquare = False
            for square in possiblesquares:
                if not firstsquare:
                    firstsquare = square
                else:
                    if square[0][1] < firstsquare[0][1]:
                        firstsquare = square
                    elif square[0][1] == firstsquare[0][1]:
                        if square[0][0] < firstsquare[0][0]:
                            firstsquare = square
            return firstsquare[1]
        return False

    def move(self, coord, board):
        # fix board.units dict
        board.units.pop((self.x, self.y))
        board.units[coord] = self

        # fix board chars
        board.grid[(self.x, self.y)] = '.'
        board.grid[coord] = self.char

        # fix object coords
        self.x = coord[0]
        self.y = coord[1]

class Elf(Unit):
    def __init__(self, x, y):
        Unit.__init__(self, x, y)
        self.char = "E"
        self.enemy = "G"

class Goblin(Unit):
    def __init__(self, x, y):
        Unit.__init__(self, x, y)
        self.char = "G"
        self.enemy = "E"

class Board:
    def __init__(self, file):
        self.grid = dict()     # key: (x, y) value: board char
        self.units = dict()
        self.round = 0
        linenum = 0
        colnum = 0
        for line in file:
            colnum = 0
            for c in line:
                c = c.rstrip()
                self.grid[(colnum, linenum)] = c
                if c == "G":
                    self.units[(colnum, linenum)] = Goblin(colnum, linenum)
                elif c == "E":
                    self.units[(colnum, linenum)] = Elf(colnum, linenum)
                colnum += 1
            linenum += 1
        self.x = colnum
        self.y = linenum

    def getAdjacents(self, coord):
        x = coord[0]
        y = coord[1]
        adjacents = list()
        adjacents.append((x, y - 1))
        adjacents.append((x - 1, y))
        adjacents.append((x + 1, y))
        adjacents.append((x, y + 1))
        return adjacents

    def getUnits(self):
        units = []
        for y in range(0, self.y):
            for x in range(0, self.x):
                if (x, y) in self.units:
                    units.append(self.units[(x, y)])
        return units

    def __str__(self):
        boardstr = ""
        if self.round == 0:
            boardstr += "Initially:\n"
        else:
            boardstr += "\nAfter " + str(self.round) + " round:\n"
        for y in range(0, self.y):
            unitcoords = []
            for x in range(0, self.x):
                boardstr += self.grid[(x, y)]
                if self.grid[(x, y)] == 'E' or self.grid[(x, y)] == 'G':
                    unitcoords.append((x, y))
            if len(unitcoords):
                boardstr += "   "
                while len(unitcoords):
                    uc = unitcoords.pop(0)
                    boardstr += self.units[uc].char + "("
                    boardstr += str(self.units[uc].hp) + ")"
                    if len(unitcoords):
                        boardstr += ", "
            boardstr += "\n"
        return boardstr.rstrip()

    def runRound(self):
        for unit in self.getUnits():
            if unit.alive:
                if not self.teamsAlive():
                    return False
                foundenemy = False
                for adj in unit.getAdjacents(self):
                    if self.grid[adj] == unit.enemy:
                        foundenemy = True
                        break
                if not foundenemy:
                    coord = unit.dirToClosestEnemy(self)
                    if coord:
                        unit.move(coord, self)
                lowesthp = False
                for adj in unit.getAdjacents(self):
                    if self.grid[adj] == unit.enemy:
                        if not lowesthp or lowesthp.hp > self.units[adj].hp:
                            lowesthp = self.units[adj]
                if lowesthp:
                    unit.attack(lowesthp, self)
        self.round += 1


        unitstodelete = []
        for key in self.units:
            if not self.units[key].alive:
                unitstodelete.append(key)
        for key in unitstodelete:
            self.units.pop(key)

        return True

    def teamsAlive(self):
        e = False
        g = False
        for y in range(0, self.y):
            for x in range(0, self.x):
                if self.grid[(x, y)] == 'E':
                    e = True
                elif self.grid[(x, y)] == 'G':
                    g = True
                if g and e:
                    return True
        return False


    def getOutcome(self):
        totalhp = 0
        for unit in self.getUnits():
            totalhp += unit.hp
        # return totalhp * (self.round - 1)
        return totalhp * self.round

    def printOutcome(self):
        totalhp = 0
        for unit in self.getUnits():
            if unit.hp > 0:
                totalhp += unit.hp
        print("\nCombat ends after", self.round, "full rounds")
        whowon = False
        for unit in self.getUnits():
            if unit.char == "E":
                whowon = "Elves"
            else:
                whowon = "Goblins"
            break
        print(whowon, "win with", totalhp, "total hit points")
        print("Outcome:", self.round, "*", totalhp, "=", totalhp * self.round)


board = Board(file)
print(board)
while board.runRound():
    print(board)
print(board)
# print(board.getOutcome())
board.printOutcome()