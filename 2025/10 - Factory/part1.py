import sys

class Machine():

    def __init__(self, s):
        l, s = s.split(" ", 1)
        b, j = line.rsplit(" ", 1)

        self.lightgoal = list(l.strip("[]"))
        self.lights = list("." * len(self.lightgoal))

        self.buttons = []
        for button in b.split():
            self.buttons.append(button.split(","))

    def correct(self):
        if self.lights == self.lightgoal:
            return True
        return False
    
    def push(self, button):
        for i in self.buttons[button]:
            if self.lights[i] == ".":
                self.lights[i] = "#"
            else:
                self.lights[i] = "."

with open(sys.argv[1], "r") as f:

    machines = []

    for line in f:
        line = line.strip()
        machines.append(Machine(line))

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    