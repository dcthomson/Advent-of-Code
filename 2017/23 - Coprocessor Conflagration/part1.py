import sys

class Cpu:

    def __init__(self):
        self.registers = dict()
        self.lastvalue = False

    def run(self, instruction):
        instlist = instruction.split()
        instruction = instlist[0]
        regletter = instlist[1]
        if len(instlist) == 3:
            try:
                value = int(instlist[2])
            except ValueError:
                value = self.registers[instlist[2]].value
        if instruction == "jnz":
            try:
                regval = int(regletter)
            except ValueError:
                if regletter not in self.registers:
                    self.registers[regletter] = Register(regletter)
                regval = self.registers[regletter].value
            if regval:
                retval = value
            else:
                retval = 1
        else:
            if regletter not in self.registers:
                self.registers[regletter] = Register(regletter)
            retval = self.registers[regletter].run(instruction, value)
        return retval

    def printregs(self):
        for k in self.registers:
            print(self.registers[k].name, self.registers[k].value)

class Register:

    def __init__(self, name, value=0):
        self.name = name
        self.value = value
        # if name == "a":
        #     self.value = 1
        self.mulrun = 0

    def run(self, instruction, val=None):
        method = getattr(self, instruction)
        if val is None:
            retval = method()
        else:
            retval = method(val)
        return retval

    def snd(self):
        # print("snd:", self.name)
        return "sound-" + str(self.value)

    def set(self, val):
        # print("set:", self.name, val)
        self.value = val
        return 1

    def add(self, val):
        # print("add:", self.name, val)
        self.value += val
        return 1

    def sub(self, val):
        # print("sub:", self.name, val)
        self.value -= val
        return 1

    def mul(self, val):
        # print("mul:", self.name, val)
        self.mulrun += 1
        self.value *= val
        return 1

    def mod(self, val):
        # print("mod:", self.name, val)
        self.value = self.value % val
        return 1

    def rcv(self):
        # print("rcv:", self.name)
        if self.value:
            return "recover"
        else:
            return 1

    def jnz(self, val):
        # print("jnz:", self.name, val, "--", self.value)
        # if self.value < 0:
        #     print("        ", end="")
        # print(self.value)
        if self.value:
            return val
        else:
            return 1

instructions = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        instructions.append(line.strip())

instnum = 0
cpu = Cpu()
while not str(instnum).startswith("recover"):
    try:
        ret = cpu.run(instructions[instnum])
        instnum += ret
    except IndexError:
        break

muls = 0
for k in cpu.registers:
    muls += cpu.registers[k].mulrun
print(muls)