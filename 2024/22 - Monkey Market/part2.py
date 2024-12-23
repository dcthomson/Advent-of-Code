import sys

class seller:
    def __init__(self, num):
        self.num = num
        self.changes = []
        self.sequences = {}

    def updatesequences(self):
        for n, change in enumerate(self.changes):
            try:
                changeset = (self.changes[n+1]-self.changes[n],
                             self.changes[n+2]-self.changes[n+1],
                             self.changes[n+3]-self.changes[n+2],
                             self.changes[n+4]-self.changes[n+3])
                if changeset not in self.sequences:
                    self.sequences[changeset] = self.changes[n+4]
            except:
                pass

sellers = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        sellers.append(seller(int(line)))

total = 0


for seller in sellers:
    # num = int(str(num)[-1])
    num = seller.num
    for _ in range(0, 2000):
        seller.changes.append(int(str(num)[-1]))
        i = num * 64
        num = i ^ num
        num = num % 16777216

        i = int(num / 32)
        num = i ^ num
        num = num % 16777216

        i = num * 2048
        num = i ^ num
        num = num % 16777216

    # print(int(str(num)[-1]))
    seller.updatesequences()
    # print(seller.changes)
    # print(seller.sequences)

sequences = {}

for seller in sellers:
    for sequence in seller.sequences:
        sequences[sequence] = 0

for sequence in sequences:
    for seller in sellers:
        try:
            sequences[sequence] += seller.sequences[sequence]
        except:
            pass

bananas = 0

for sequence in sequences:
    if sequences[sequence] > bananas:
        bananas = sequences[sequence]

print(bananas)