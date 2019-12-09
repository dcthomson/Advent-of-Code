import sys

class Component:

    def __init__(self, l, r):
        self.port1 = l
        self.port2 = r

class Bridge:

    def __init__(self):
        self.components = list()
        self.open = False

    def addcomponent(self, component):
        if len(self.components) == 0:
            if component.part1 == 0:
                self.components.append(component)
                self.open = component.part2
            elif component.part2 == 0:
                self.components.append(component)
                self.open = component.part1
            else:
                return False
        else:
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

components = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        l = line.split("/")
        components.append(Component(int(l[0]), int(l[1])))

print(components)

def addcomponent(components, bridge=Bridge()):

for component in components:
    b = Bridge()
    if b.addcomponent(component):
        addcomponent(components)

print(strength)