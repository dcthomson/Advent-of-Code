import sys

class grove:

    def __init__(self):
        self.grove = {}

        with open(sys.argv[1], "r") as f:

            y = 0

            for line in f:
                line = line.strip()

                x = 0

                for c in line:
                    self.grove[(x,y)] = c
                    if c == "#":
                        
