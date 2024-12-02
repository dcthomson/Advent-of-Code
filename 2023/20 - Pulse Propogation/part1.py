import sys

modules = {}

class Module:
    def __init__(self, name, next):
        self.name = name
        self.nextmodules = next

class Flipflop(Module):
    def __init__(self, name, next):
        super().__init__(name, next)
        self.state = "off"

    def run(self, pulse, q, input):       
        if pulse == "low":
            if self.state == "off":
                self.state = "on"
                for nextmodule in self.nextmodules:
                    q.append((nextmodule, "high", self.name))
            else:
                self.state = "off"
                for nextmodule in self.nextmodules:
                    q.append((nextmodule, "low", self.name))
        return q


class Conjunction(Module):
    def __init__(self, name, next):
        super().__init__(name, next)
        self.inputs = {}

    def run(self, pulse, q, input):
        self.inputs[input] = pulse
        allhigh = True
        for i in self.inputs:
            if self.inputs[i] == "low":
                allhigh = False
                break
        if allhigh:
            for nextmodule in self.nextmodules:
                q.append((nextmodule, "low", self.name))
        else:
            for nextmodule in self.nextmodules:
                q.append((nextmodule, "high", self.name))
        return q


class Broadcast(Module):
    def __init__(self, name, next):
        super().__init__(name, next)

    def run(self, pulse, q, input):
        for nextmodule in self.nextmodules:
            q.append((nextmodule, pulse, self.name))
        return q


with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()

        (m, next) = line.split(" -> ")
        nextlist = next.split(", ")
        if m.startswith("&"):
            modulename = m[1:]
            modules[modulename] = Conjunction(modulename, nextlist)
        elif m.startswith("%"):
            modulename = m[1:]
            modules[modulename] = Flipflop(modulename, nextlist)
        else:
            modules[m] = Broadcast(m, nextlist)


for i in range(0, 1000): 

    queue = [("broadcaster", "low", "")]

    while(queue):
        print(queue)
        (module, pulse, input) = queue.pop(0)
        if module != "output":
            queue = modules[module].run(pulse, queue, input)

    for m in modules:
        try:
            print(modules[m].name, ": ", modules[m].state)
        except:
            pass
    print()