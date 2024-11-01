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
        flow = int(flow.split("=")[1])

        valves[name] = Valve(name, flow, othervalves)

highestpressure = 0
hp = 0

# def printstatus(minute, open):
#     print("== Minute ", minute, "==")
#     if not open:
#         print("No valves are open.")
#     else:
#         p = 0
#         s = ""
#         for v in open:
#             s += v  + " and "
#             p += valves[v].flow
#         s = s[:-4]
#         print("Valve " + s + " is open, releasing " + str(p) + " pressure.")

def printpath(path):

    global hp

    open = []
    totalpressure = 0

    print(path)

    for min, step in enumerate(path.split("-"), 1):
        print("== Minute " + str(min) + " ==")
        if not len(open):
            print("No valves are open.")
        else:
            toprint = "Valve"
            if len(open) > 1:
                toprint += "s"
            toprint += " "
            pressure = 0
            for o in open:
                pressure += valves[o].flow
                toprint += o
                toprint += " "
            totalpressure += pressure
            toprint += "are open, releasing " + str(pressure) + " pressure."
            print(toprint)
        if step.startswith("M"):
            (_,movetovalve) = step.split('=')
            print("You move to valve " + movetovalve + ".")
        elif step.startswith("O"):
            (_,openvalve) = step.split('=')
            print("You open valve " + openvalve + ".")
            open.append(openvalve)
        if totalpressure > hp:
            hp = totalpressure
        print("Total pressure: " + str(totalpressure))
        print("HP: " + str(hp))
        print()
    print()
    print()
    print()

numvalveswithflow = 0
for v in valves:
    if valves[v].flow > 0:
        numvalveswithflow += 1

printpath("M=DD-O=DD-M=CC-M=BB-O=BB-M=AA-M=II-M=JJ-O=JJ-M=II-M=AA-M=DD-M=EE-M=FF-M=GG-M=HH-O=HH-M=GG-M=FF-M=EE-O=EE-M=DD-M=CC-O=CC-STAY-STAY-STAY-STAY-STAY-STAY")

exit()

def moveandrelease(valve, open = [], minute = 0, path = ""):

    global highestpressure
    global numvalveswithflow

    # printstatus(minute, open)

    minute += 1

    if minute == 30:
        print(path)
        return

    if numvalveswithflow == len(open):
        # if all valves are open, no need to move
        moveandrelease(valve, open.copy(), minute, path + "STAY-")
    else:
            
        if valve not in open and valves[valve].flow > 0:
            open.append(valve)
            moveandrelease(valve, open.copy(), minute, path + "O=" + valve + "-")

        for v in valves[valve].valves:
            # print("You move to valve ")
            moveandrelease(v, open.copy(), minute, path + "M=" + v + "-")

moveandrelease("AA")