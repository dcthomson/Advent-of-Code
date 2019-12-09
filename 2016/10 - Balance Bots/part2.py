import sys

class Bot():

    def __init__(self):
        self.values = []

    def addValue(self, v):
        self.values.append(int(v))
        self.values.sort()

    def setInstructions(self, ldest, lbotnum, hdest, hbotnum):
        if ldest == "bot":
            self.lowerbot = True
        else:
            self.lowerbot = False
        self.lowerbotnum = int(lbotnum)

        if hdest == "bot":
            self.higherbot = True
        else:
            self.higherbot = False
        self.higherbotnum = int(hbotnum)

    def runInstructions(self, bots, outputs):
        if self.lowerbot:
            bots[self.lowerbotnum].addValue(self.values[0])
        else:
            outputs[self.lowerbotnum] = self.values[0]
        if self.higherbot:
            bots[self.higherbotnum].addValue(self.values[1])
        else:
            outputs[self.higherbotnum] = self.values[1]
        self.values = []
        

bots = {}
outputs = {}

with open ( sys.argv[1] ) as f:
    for line in f:
        if line.startswith('value'):
            (_, val, _, _, _, bot) = line.split()
            val = int(val)
            bot = int(bot)
            if bot not in bots:
                bots[bot] = Bot()
            bots[bot].addValue(val)
        if line.startswith('bot'):
            (_, bot, _, _, _, ldest, lval, _, _, _, hdest, hval) = line.split()
            bot = int(bot)
            lval = int(lval)
            hval = int(hval)
            if bot not in bots:
                bots[bot] = Bot()
            bots[bot].setInstructions(ldest, lval, hdest, hval)

foundtwo = True
while foundtwo:
    foundtwo = False
    for k, v in bots.items():
        if len(v.values) >= 2:
            foundtwo = True
            v.runInstructions(bots, outputs)

print(outputs[0] * outputs[1] * outputs[2])