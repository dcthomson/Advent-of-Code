import sys

gusts = ""

with open(sys.argv[1], "r") as f:

    for line in f:
        gusts = line.strip()

class Rock():

    def __init__(self, shape):
        self.shape = shape



rocks = []

rocks.append(Rock([(0,0), (1,0), (2,0), (3,0)])) # ----
rocks.append(Rock([(1,0), (0,1), (1,1), (2,1), (1,2)])) # +
rocks.append(Rock([(2,0), (2,1), (0,2), (1,2), (2,2)])) # L
rocks.append(Rock([(0,0), (0,1), (0,2), (0,3)])) # |
rocks.append(Rock([(0,0), (0,1), (1,0), (1,1)])) # #

