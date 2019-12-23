import sys

decksize = 119315717514047

class Deck:
    def __init__(self, size):
        self.deck = []
        self.size = size
        for i in range(0, size):
            self.deck.append(i)

    def newstack(self):
        self.deck.reverse()

    def cut(self, num):
        self.deck = self.deck[num:] + self.deck[:num]

    def dealwithincrement(self, num):
        newdeck = [None] * self.size
        index = 0
        for i in self.deck:
            newdeck[index] = i
            index += num
            if index > self.size:
                index = index - self.size
        self.deck = newdeck

print("Creating deck...", end="")
deck = Deck(decksize)
print("DONE")

lines = []

with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.rstrip())

print("runnin lines")
for line in lines:
    if line == "deal into new stack":
        print(line, "...", end="")
        deck.newstack()
        print("DONE")
    if line.startswith("cut "):
        print(line, "...", end="")
        num = int(line.split()[1])
        deck.cut(num)
        print("DONE")
    if line.startswith("deal with increment"):
        print(line, "...", end="")
        num = int(line.split()[3])
        deck.dealwithincrement(num)
        print("DONE")

i = 0
for card in deck.deck:
    if card == 2019:
        print(i)
        break
    i += 1