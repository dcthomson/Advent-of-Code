import sys

class Pot:

    def __init__(self, num, plant=False, left=False, right=False):
        self.num = num
        self.plant = plant
        if plant:
            self.char = "#"
        else:
            self.char = "."
        self.left = left
        self.right = right

    def getNextGen(self, rules):
        if self.left:
            left1 = self.left.char
            if left1.left:
                left2 = left1.left.char
            else:
                left2 = "."
        else:
            left1 = "."
        if self.right:
            right1 = self.right.char
            if left1.left:
                right2 = right1.right.char
            else:
                right2 = "."
        else:
            right1 = "."

        if left2 + left1 + self.char + right1 + right2 not in rules:
            return "."
        else:
            return rules[left2 + left1 + self.char + right1 + right2] 

        

file = open(sys.argv[1], 'r')

rules = dict()

for line in file:
    if line.startswith("initial"):
        initialstate = line.split(": ")[1]
        potnum = 0
        currentPot = False
        for c in initialstate:
            if c == "#":
                plant = True
            else:
                plant = False
            if not currentPot:
                currentPot = Pot(potnum, plant)
            else:
                currentPot = Pot(potnum, plant, currentPot)
                currentPot.left.right = currentPot

    elif " => " in line:
        (pattern, plant) = line.rstrip().split(" => ")
        rules[pattern] = plant

def printPots(pot):
    nextLeft = pot.left
    while nextLeft:
        pot = pot.left
        nextLeft = pot.left
    nextRight = pot.right
    print pot.num
    while nextRight:
        if pot.plant:
            sys.stdout.write("#")
        else:
            sys.stdout.write(".")
        pot = pot.right
        nextRight = pot.right
    print

def getFirstPlant(pot):
    nextLeft = pot.left
    plantpot = False
    while nextLeft:
        if pot.plant:
            plantpot = pot
        pot = pot.left
        nextLeft = pot.left
    if plantpot:
        return plantpot
    else:
        for _ in range(0, 10):
            pot = pot.right
        return getFirstPlant(pot)

printPots(currentPot)

for i in range(0, 20):

