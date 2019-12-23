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

    def addcomponent(self, component):

        if component.port1 == self.open:
            self.components.append(component)
            self.open = component.port2
        elif component.port2 == self.open:
            self.components.append(component)
            self.open = component.port1
        else:
            return False
        return True

    def getstrength(self):
        strength = 0
        for i in self.components:
            strength += i.port1 + i.port2
        return strength

    def __str__(self):
        retstr = ""
        for c in self.components:
            if retstr != "":
                retstr += "--"
            retstr += str(c.port1) + "/" + str(c.port2)
        return retstr

components = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        l = line.split("/")
        components.append(Component(int(l[0]), int(l[1])))

strongestbridge = 0

def buildbridge(components, bridge=Bridge()):
    global strongestbridge
    # cs = components.copy()
    # print(bridge)
    bs = bridge.getstrength()
    if bs > strongestbridge:
        strongestbridge = bs
        print(bs)
    # print(strongestbridge)
    for component in components:
        b = copy.deepcopy(bridge)
        if b.addcomponent(component):
            buildbridge([c for c in components if c != component], b)



buildbridge(components)
print(strongestbridge)