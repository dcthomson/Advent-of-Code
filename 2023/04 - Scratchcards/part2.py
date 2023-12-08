import sys

class Card():

    def __init__(self, s):
        self.num = 1
        (winningnumsstr, mynumsstr) = s.split(" | ")
        w = winningnumsstr.split()
        self.winners = [int(x) for x in w]
        m = mynumsstr.split()
        self.mynums = [int(x) for x in m]

    def getwinnercount(self):
        matches = 0
        for m in self.mynums:
            if m in self.winners:
                matches += 1
        return matches

    def __str__(self):
        retstr = ""
        retstr += str(self.num)
        retstr += ": "
        retstr += str(" ".join(map(str, self.winners)))
        retstr += " | "
        retstr += str(" ".join(map(str, self.mynums)))
        return retstr

cards = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()
        (card, nums) = line.split(": ")
        (_, card) = card.split()
        card = int(card)
        cards[card] = Card(nums)

for c in cards:
    for i in range(c+1, c+1+cards[c].getwinnercount()):
        cards[i].num += cards[c].num
    
total = 0
for c in cards:
    total += cards[c].num
print(total)