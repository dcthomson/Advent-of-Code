from operator import itemgetter
import sys

file = open(sys.argv[1], "r")

players = ""
lastmarble = ""

for line in file:
    players = int(line.split(" ")[0])
    lastmarble = int(line.split(" ")[6])

    marblenum = 0
    marblelist = [0]
    listindex = 0
    playerscores = dict()
    while marblenum <= lastmarble:

        player = marblenum % players
        if player == 0:
            player = players

        if not marblenum % 100000:
            print "marble: " + str(marblenum)

        if marblenum % 23 != 0:
            # not divisible by 23
            for i in range(0, 2):
                listindex += 1
                if len(marblelist) < listindex:
                    listindex = 0
            if listindex + 1 == len(marblelist):
                listindex += 1
                marblelist.append(marblenum)
            else:
                marblelist.insert(listindex + 1, marblenum)
        else: 
            # divisible by 23
            if marblenum != 0:
                if player not in playerscores:
                    playerscores[player] = 0
                playerscores[player] += marblenum
        #        print listindex
                marble = 0
#                print "li:     " + str(listindex)
#                print "new li: " + str(listindex - 6)
                listindex -= 6
                if listindex < 0:
                    print "got a negative"
                    print "li: %s" % (listindex)
                    if listindex == -4:
                        listindex = len(marblelist) + listindex
                    else:
                        listindex = len(marblelist) + listindex + int(sys.argv[2])
                    marble = marblelist[listindex]
                    print "marble: " + str(marble)
                else:
                    marble = marblelist[listindex]
                playerscores[player] += marble
                del marblelist[listindex]
                listindex -= 1

        if marblenum == 0:
            player = "-"

#        sys.stdout.write("[" + str(player) + "]")
#        print marblelist

        marblenum += 1

    for k,v in sorted(playerscores.items(), key=itemgetter(1), reverse=True):
        print "player: %s   score: %s" % (k, v)
        break
    print
