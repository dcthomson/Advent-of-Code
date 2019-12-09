import sys

class Image:

    def __init__(self, s=False):
        if s:
            i = 0
            for i in s.split("/"):
                pass

rules = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        rule, out = line.split(" => ")
        rules[rule] = out

