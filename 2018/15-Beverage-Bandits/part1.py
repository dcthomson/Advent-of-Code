import sys

import operator

file = open(sys.argv[1], "r")

class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 200
        self.ap = 3
        self.distances = dict()
        self.closestEnemyAdj = False # (x, y, count)

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

    def getAdjacents(self):
        adjacents = list()
        adjacents.append((self.x, self.y - 1))
        adjacents.append((self.x - 1, self.y))
        adjacents.append((self.x + 1, self.y))
        adjacents.append((self.x, self.y + 1))
        return adjacents

    def mapDistances(self, board):
        # make function that takes a coord
        # called recursively: u-l-r-d
        def traverseMap(x, y, count, board):
            if self.closestEnemyAdj:
                if count > self.closestEnemyAdj[2]:
                    return
            if not (x, y) in board.board:
                return
            elif board.board[(x, y)] == "#":
                return
            if count != 0:
                for u in board.units:
                    if u.x == x and u.y == y:
                        return
#                    if self.char != u.char:
#                        if (x, y) in u.getAdjacents():
#                            self.closestEnemyAdj = (x, y, count)

            if (x, y) not in self.distances:
                self.distances[(x, y)] = count
            else:
                if count < self.distances[(x, y)]:
                    self.distances[(x, y)] = count
                else:
                    return
            count += 1
            traverseMap(x, y - 1, count, board) # up
            traverseMap(x - 1, y, count, board) # left
            traverseMap(x + 1, y, count, board) # right
            traverseMap(x, y + 1, count, board) # down
            return

        traverseMap(self.x, self.y, 0, board)


class Elf(Unit):
    def __init__(self, x, y):
        Unit.__init__(self, x, y)
        self.char = "E"

class Goblin(Unit):
    def __init__(self, x, y):
        Unit.__init__(self, x, y)
        self.char = "G"

class Board:
    def __init__(self, file):
        self.board = dict()     # key: (x, y) value: board char
        self.units = list()
        linenum = 0
        colnum = 0
        for line in file:
            colnum = 0
            for c in line:
                c = c.rstrip()
                self.board[(colnum, linenum)] = c
                if c == "G":
                    self.board[(colnum, linenum)] = "."
                    self.units.append(Goblin(colnum, linenum))
                elif c == "E":
                    self.board[(colnum, linenum)] = "."
                    self.units.append(Elf(colnum, linenum))
                colnum += 1
            linenum += 1
        self.x = colnum - 1
        self.y = linenum

    def __str__(self):
        boardstr = ""
        for y in range(0, self.y):
            for x in range(0, self.x):
                printed = False
                for unit in self.units:
                    if unit.x == x and unit.y == y:
                        boardstr += unit.char
                        printed = True
                if not printed:
                    boardstr += self.board[(x, y)]
            boardstr += "\n"
        return boardstr.rstrip()

    def runRound(self):
        elfcount = 0
        goblincount = 0
        for u in self.units:
            if unit.char == "E":
                elfcount += 1
            elif unit.char == "G":
                goblincount += 1
        if elfcount == 0:
            print "Elves are dead :("
            return False
        elif goblincount == 0:
            print "Goblins are dead :)"
            return False


# pathing might have to use Dijkstra's
# visited and unvisited dicts
# go 1 at a time and map all open spots
# recursively u-l-r-d

# create board

board = Board(file)
print board
for u in board.units:
    u.mapDistances(board)
#    print u.distances
