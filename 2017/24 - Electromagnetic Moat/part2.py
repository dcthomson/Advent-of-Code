import sys
import copy

class Component:

    def __init__(self, l, r):
        self.port1 = l
        self.port2 = r

    def __str__(self):
        return str(self.port1) + "/" + str(self.port2)

class Bridge:

    def __init__(self):
        self.components = list()
        self.open = 0

    def getsize(self):
        return len(self.components)

    def addcomponent(self, component):

        if component[0] == self.open:
            self.components.append(component)
            self.open = component[1]
        elif component[1] == self.open:
            self.components.append(component)
            self.open = component[0]
        else:
            return False
        return True

        # if component.port1 == self.open:
        #     self.components.append(component)
        #     self.open = component.port2
        # elif component.port2 == self.open:
        #     self.components.append(component)
        #     self.open = component.port1
        # else:
        #     return False
        # return True

    def getstrength(self):
        strength = 0
        for i in self.components:
            strength += i[0] + i[1]
        return strength

    def __str__(self):
        retstr = ""
        for c in self.components:
            if retstr != "":
                retstr += "--"
            retstr += str(c[0]) + "/" + str(c[1])
        return retstr

components = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        l = line.split("/")
        # components.append(Component(int(l[0]), int(l[1])))
        components.append((int(l[0]), int(l[1])))

strongestbridge = 0
bridges = []
longestbridge = 0

def buildbridge(components, bridge=Bridge()):
    global longestbridge
    global bridges

    if bridge.getsize() > longestbridge:
        bridges = []
        longestbridge = bridge.getsize()
    if bridge.getsize() == longestbridge:
        bridges.append(bridge)

    # print(strongestbridge)
    for component in components:
        b = copy.deepcopy(bridge)
        if b.addcomponent(component):
            buildbridge([c for c in components if c != component], b)

buildbridge(components)

for b in bridges:
    print(b.getstrength())
    print(b.components)
    print()