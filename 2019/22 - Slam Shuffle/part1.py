import sys

decksize = 10007

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

deck = Deck(decksize)

with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if line == "deal into new stack":
            deck.newstack()
        if line.startswith("cut "):
            num = int(line.split()[1])
            deck.cut(num)
        if line.startswith("deal with increment"):
            num = int(line.split()[3])
            deck.dealwithincrement(num)

i = 0
for card in deck.deck:
    if card == 2019:
        print(i)
        break
    i += 1