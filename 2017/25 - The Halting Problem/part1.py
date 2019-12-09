import sys

class State:

    def __init__(self, name):
        self.name = name
        self.zval = False
        self.zmove = False
        self.znext = False
        self.oval = False
        self.omove = False
        self.onext = False

    def setwriteval(self, curval, writeval):
        if curval:
            self.oval = int(writeval)
        else:
            self.zval = int(writeval)

    def setmove(self, curval, move):
        if curval:
            self.omove = int(move)
        else:
            self.zmove = int(move)

    def setnext(self, curval, next):
        if curval:
            self.onext = next
        else:
            self.znext = next

    def run(self, tape, cursor):
        if cursor not in tape:
            tape[cursor] = 0
        if tape[cursor] == 0:
            tape[cursor] = self.zval
            cursor += self.zmove
            next = self.znext
        elif tape[cursor] == 1:
            tape[cursor] = self.oval
            cursor += self.omove
            next = self.onext
        return tape, cursor, next

class Turing:

    def __init__(self):
        self.states = dict()
        self.tape = dict()
        self.cursor = 0
        self.iteration = 0

    def run(self):
        while self.iteration < self.checksum:
            self.tape, self.cursor, self.state = self.states[self.state].run(self.tape, self.cursor)
            self.iteration += 1

    def totalones(self):
        ones = 0
        for k in self.tape:
            if self.tape[k] == 1:
                ones += 1
        return ones

    def readinputfromfile(self, infile):
        with open(infile, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("Begin in state"):
                    self.state = line[-2]
                elif line.startswith("Perform a diagnostic"):
                    self.checksum = int(line.split(" ")[5])
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
                    self.states[state].setnext(curval, nextstate)

if __name__ == "__main__":
    turing = Turing()
    turing.readinputfromfile(sys.argv[1])
    turing.run()
    print(turing.totalones())