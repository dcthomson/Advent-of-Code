import sys

class State:

    def __init__(self, name):
        self.name = name
        self.zval = Fasle
        self.zmove = False
        self.znext = False
        self.oval = False
        self.omove = False
        self.onext = False

    def setwriteval(self, curval, writeval):
        if curval:
            self.oval = writeval
        else:
            self.zval = writeval

    def setmove(self, curval, move):
        if curval:
            self.omove = move
        else:
            self.zmove = move

    def setnext(self, curval, next):
        if curval:
            self.onext = next
        else:
            self.znext = next

    def run(self, val):
        if val == 0:
            

class Turing:

    def __init__(self):
        self.states = dict()

        with open(sys.argv[1], 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("Begin in state"):
                    startstate = line[-2]
                elif line.startswith("Perform a diagnostic"):
                    checksum = int(line.split(" ")[5])
                elif line.startswith("In state "):
                    state = line[-2]
                    self.states[state] = State(state)
                elif line.startswith("If the current value"):
                    curval = int(line[-2])
                elif line.startswith("- Write"):
                    newval = int(line[-2])
                    self.states[state].setwriteval(curval, newval)
                elif line.startswith("- Move"):
                    dir = line.split(" ")[-1].strip('.')
                    if dir == 'left':
                        move = -1
                    elif dir == 'right':
                        move = 1
                    self.states[state].setmove(curval, move)
                elif line.startswith("- Continue"):
                    nextstate = line[-2]
                    self.states[state].setmove(curval, nextstate)
