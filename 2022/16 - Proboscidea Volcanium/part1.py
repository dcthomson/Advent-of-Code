import sys

sys.setrecursionlimit(50000)

class Valve():

    def __init__(self, name, flow, valves):
        self.name = name
        self.flow = flow
        self.valves = valves

valves = {}

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        first = last = ""

        if "tunnels" in line:
            (first, last) = line.split("; tunnels lead to valves ")
        elif "tunnel " in line:
            (first, last) = line.split("; tunnel leads to valve ")
        othervalves = last.split(", ")
        (_,name,_,_,flow) = first.split()
        flow = flow.split("=")[1]

        valves[name] = Valve(name, flow, othervalves)


def moveandrelease(valve, open = [], pressure = 0, move = 0):

    for v in valves[valve].valves:
        p = moveandrelease(v, open, pressure, move)
        

    for v in valves[valve].valves:
        open.append(valve)
        moveandrelease(v, open, pressure, move)

    return p

print(moveandrelease("AA"))