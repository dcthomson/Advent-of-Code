import sys

modules = {}

highcount = 0
lowcount = 0

class Module:
    def __init__(self, name, next):
        self.name = name
        self.nextmodules = next

    def countpulse(self, pulse):
        global highcount
        global lowcount
        if pulse == "low":
            lowcount += 1
        elif pulse == "high":
            highcount += 1

class Flipflop(Module):
    def __init__(self, name, next):
        super().__init__(name, next)
        self.state = "off"

    def run(self, pulse, q, input):
        super().countpulse(pulse)
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
        super().countpulse(pulse)
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
        super().countpulse(pulse)
        for nextmodule in self.nextmodules:
            q.append((nextmodule, pulse, self.name))
        return q

nextlist = []

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()

        (m, n) = line.split(" -> ")
        next = n.split(", ")
        nextlist.extend(next)
        if m.startswith("&"):
            modulename = m[1:]
            modules[modulename] = Conjunction(modulename, next)
        elif m.startswith("%"):
            modulename = m[1:]
            modules[modulename] = Flipflop(modulename, next)
        else:
            modules[m] = Broadcast(m, next)

for n in nextlist:
    if n not in modules:
        modules[n] = Flipflop(n, [])


for i in range(0, 1000): 

    queue = [("broadcaster", "low", "")]

    while(queue):
        # print(queue)
        (module, pulse, input) = queue.pop(0)
        queue = modules[module].run(pulse, queue, input)

    # for m in modules:
    #     try:
    #         print(modules[m].name, ": ", modules[m].state)
    #     except:
    #         pass
    # print()

print(lowcount, "low *", highcount, "high =", lowcount * highcount)