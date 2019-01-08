from operator import itemgetter
import sys

class Marble:
    
    def __init__(self, number, prevmarble=False, nextmarble=False):
        if not prevmarble:
            self.prev = self
        else:
            self.prev = prevmarble
        if not nextmarble:
            self.next = self
        else:
            self.next = nextmarble
        self.number = number

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setNext(self, marble):
        self.next = marble

    def setPrev(self, marble):
        self.prev = marble

    def getNum(self):
        return self.number



file = open(sys.argv[1], "r")

players = ""
lastmarble = ""

for line in file:
    players = int(line.split(" ")[0])
    lastmarble = int(line.split(" ")[6])

    marblenum = 0
    playerscores = dict()
    currentMarble = False
    while marblenum <= lastmarble:
        player = marblenum % players
        if player == 0:
            player = players
        if marblenum % 100000 == 0:
            print "marblenum: %s" % (marblenum)
        if marblenum == 0 or marblenum % 23 != 0:
            if not currentMarble:
                currentMarble = Marble(marblenum)
                firstMarble = currentMarble
            else:
                for i in range(1,3):
                    currentMarble = currentMarble.getNext()
                currentMarble = Marble(marblenum, currentMarble.prev, currentMarble)
                currentMarble.prev.setNext(currentMarble)
                currentMarble.next.setPrev(currentMarble)

        else:
            if player not in playerscores:
                playerscores[player] = 0
#            print "adding: %s for player: %s" % (marblenum, player)
            playerscores[player] += marblenum
            for _ in range(1,8):
                currentMarble = currentMarble.getPrev()
#            print "adding: %s for player: %s" % (currentMarble.number, player)
            playerscores[player] += currentMarble.number

            currentMarble.prev.setNext(currentMarble.next)
            currentMarble.next.setPrev(currentMarble.prev)
            currentMarble = currentMarble.getNext()
        marblenum += 1

#        printmarb = firstMarble
#        printmarbs = True
#        while printmarbs:
#            if printmarb == currentMarble:
#                sys.stdout.write("(")
#                sys.stdout.write(str(printmarb.number))
#                sys.stdout.write(")")
#            else:
#                sys.stdout.write(str(printmarb.number))
#            sys.stdout.write(" ")
#            printmarb = printmarb.getNext()
#            if printmarb == firstMarble:
#                printmarbs = False
#        print

    for k,v in sorted(playerscores.items(), key=itemgetter(1), reverse=True):
        print "player: %s    score: %s" % (k, v)
        break
    print
