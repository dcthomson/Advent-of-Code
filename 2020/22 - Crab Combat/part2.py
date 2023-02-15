import sys

player1 = []
player2 = []

with open(sys.argv[1], "r") as f:
    player = []
    for line in f:
        line = line.rstrip()
        if line == "Player 1:":
            player = player1
        elif line == "Player 2:":
            player = player2
        elif line != "":
            player.append(int(line))

class Layout:

    def __init__(self, p1, p2):
        self.p1 = p1.copy()
        self.p2 = p2.copy()

    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2:
            return True
        else:
            return False

game = 1

def playgame(player1, player2):
    global game
    gamenum = game
    game += 1
    # print("=== Game", gamenum, "===")
    layouts = []
    # layouts.append(Layout(player1, player2))
    round = 1
    while len(player1) and len(player2):
        # print("-- Round", round, "(Game", gamenum, ") --")
        # print("Player 1's deck: ", end="")
        # for i in player1:
        #     print(i, " ", end="", sep=",")
        # print()
        # print("Player 2's deck: ", end="")
        # for i in player2:
        #     print(i, " ", end="", sep=",")
        # print()

        curlayout = Layout(player1, player2)
        for l in layouts:
            if l == curlayout:
                return 1
        layouts.append(Layout(player1, player2))
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        # print("Player 1 plays:", p1)
        # print("Player 2 plays:", p2)
        winner = 0
        if len(player1) >= p1 and len(player2) >= p2:
            # print("Playing a sub-game to determine the winner...\n")
            winner = playgame(player1[:p1], player2[:p2])
            if winner == 1:
                # print("Player 1 wins round", round, "of game", gamenum, "!\n")
                player1.append(p1)
                player1.append(p2)
            elif winner == 2:
                # print("Player 2 wins round", round, "of game", gamenum, "!\n")
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                # print("Player 1 wins round", round, "of game", gamenum, "!\n")
                player1.append(p1)
                player1.append(p2)
            elif p2 > p1:
                # print("Player 2 wins round", round, "of game", gamenum, "!\n")
                player2.append(p2)
                player2.append(p1)
        round += 1
    if player1:
        return 1
    else:
        return 2

winner = playgame(player1, player2)

if winner == 1:
    winner = player1
else:
    winner = player2

# print(winner)

total = 0
mult = len(winner)
for i in winner:
    total += i * mult
    mult -= 1
print(total)