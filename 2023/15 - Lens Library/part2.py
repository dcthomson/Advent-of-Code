import sys

steps = []

class Box:

    def __init__(self):
        self.lenses = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        steps = line.split(",")

total = 0

for step in steps:
    val = 0
    for c in step:
        val += ord(c)
        val *= 17
        val = val % 256
    total += val
print(total)