import sys

playerpos = {}
playerscore = {1:0, 2:0}

with open(sys.argv[1], "r") as f:
    for line in f:
        (_, player, _, _, pos) = line.rstrip().split()
        playerpos[int(player)] = int(pos)


diepos = 1
dierolls = 0

while playerscore[1] < 1000 and playerscore[2] < 1000:
    for player in range(1, 3):
        if playerscore[1] >= 1000 or playerscore[2] >= 1000:
            break
        tomove = 0
        print("Player", player, "rolls ", end="")
        for i in range(0, 3):
            if diepos > 100:
                diepos = 1
            print(diepos, end="")
            if i < 2:
                print("+", end="")
            tomove += diepos
            diepos += 1
            dierolls += 1
        print(" and moves to space ", end="")
        tomove %= 10
        if tomove == 0:
            tomove = 10
        if (playerpos[player] + tomove) % 10 == 0:
            playerpos[player] = 10
        else:
            playerpos[player] = (playerpos[player] + tomove) % 10

        print(playerpos[player], end="")
        playerscore[player] += playerpos[player]
        print(" for a total score of ", playerscore[player], ".")
            
lowest = None
for v in playerscore.values():
    if lowest is None:
        lowest = v
    elif v < lowest:
        lowest = v

print(dierolls * lowest)




1 1 1
1 1 2
1 1 3
1 2 1
1 2 2 
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2 
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2 
3 2 3
3 3 1
3 3 2
3 3 3