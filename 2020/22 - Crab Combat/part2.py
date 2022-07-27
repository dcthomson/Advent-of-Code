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

while len(player1) and len(player2):
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    elif p2 > p1:
        player2.append(p2)
        player2.append(p1)

winner = []
if player1:
    winner = player1
elif player2:
    winner = player2

print(winner)

total = 0
mult = len(winner)
for i in winner:
    total += i * mult
    mult -= 1
print(total)