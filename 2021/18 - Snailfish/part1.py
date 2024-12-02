import sys

numbers = list()

class Pair:

    def __init__(self):
        self.l = 0
        self.r = 0

def 

with open(sys.argv[1], "r") as f:
    for line in f:
        num = 
        for c in line:

        numbers.append(line.rstrip())

level = 0

for number in numbers:
    for i, c in enumerate(number):
        print(c)
        print(i)
        print()
        if c == "[":
            level += 1
        elif c == "]":
            level -= 1
        if c.isdigit():
            if number[i + 1] == ",":
                if number[i + 2].isdigit():
                    # we found a pair
                    if level >= 4:
                        # explode
                        