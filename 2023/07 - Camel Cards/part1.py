import sys
import functools 
from functools import total_ordering

@total_ordering
class Hand:

    def __init__(self, cards, bid):
        self.cardorder = "AKQJT98765432"
        self.cards = cards
        self.bid = int(bid)
        self.cardcount = {}

        for c in cards:
            if c in self.cardcount:
                self.cardcount[c] += 1
            else:
                self.cardcount[c] = 1

        if 5 in self.cardcount.values():
            self.type = 7       # Five of a kind
        elif 4 in self.cardcount.values():
            self.type = 6       # Four of a kind
        elif 3 in self.cardcount.values():
            if len(self.cardcount) == 2:
                self.type = 5   # Full house
            else:
                self.type = 4   # Three of a kind
        elif 2 in self.cardcount.values():
            if len(self.cardcount) == 3:
                self.type = 3   # Two pair
            else:
                self.type = 2   # One pair
        else:
            self.type = 1       # High card

    def getval(self, i):
        return self.cardorder.index(self.cards[i])

    def __eq__(self, obj):
        return (self.cards == obj.cards)
    
    def __gt__(self, obj):
        if self.type > obj.type:
            return True
        elif self.type < obj.type:
            return False
        else:
            for i in range(0, 5):
                if self.getval(i) < obj.getval(i):
                    return True
                elif self.getval(i) > obj.getval(i):
                    return False
                
    def __repr__(self):
        return self.cards

hands = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        (c, b) = line.split()
        h = Hand(c, b)
        hands.append(h)

total = 0

for i, h in enumerate(sorted(hands)):
    total += h.bid * (i + 1)

print(total)