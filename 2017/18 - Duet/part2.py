import sys

class Program:

    def __init__(self, prognum):
        self.prognum = prognum
        self.registers = dict()
        self.registers['p'] = Register('p')
        self.registers['p'].set(prognum)
        self.lastvalue = False
        self.waiting = False
        self.rcvreg = False
        self.rcvqueue = []
        self.totalsends = 0

    def setbuddyprog(self, buddy):
        self.buddyprog = buddy

    def runqueue(self):
        if self.rcvqueue:
            self.registers[self.rcvreg].set(self.rcvqueue.pop(0))
            self.waiting = False
            return True
        return False

    def run(self, instruction):
        if self.waiting:
            if self.runqueue():
                return 1
            else:
                return 0
        else:
            instlist = instruction.split()
            # print(self.prognum, instlist)
            # print(self.prognum, instlist, self.getregsstr())
            instruction = instlist[0]
            regletter = instlist[1]
            if len(instlist) == 3:
                try:
                    # 3rd arg is int
                    value = int(instlist[2])
                except ValueError:
                    # 3rd arg is letter
                    try:
                        value = self.registers[instlist[2]].value
                    except KeyError:
                        print(instlist)
                        sys.exit()
                if regletter not in self.registers:
                    # add regletter
                    self.registers[regletter] = Register(regletter)
                retval = self.registers[regletter].run(instruction, value)
            else:
                # only 2 args (snd and rcv)
                value = None
                retval = 1
                if instruction == 'snd':
                    try:
                        self.buddyprog.rcvqueue.append(int(regletter))
                    except ValueError:
                        self.buddyprog.rcvqueue.append(self.registers[regletter].value)
                    self.totalsends += 1
                elif instruction == 'rcv':
                    self.rcvreg = regletter
                    self.registers[regletter] = Register(regletter)
                    self.waiting = True
                    if not self.runqueue():
                        retval = 0
            return retval

    def getregsstr(self):
        retstr = ""
        for k in self.registers:
            retstr += str(self.registers[k].name) + ": "
            retstr += str(self.registers[k].value) + ", "
        return retstr.rstrip(", ")


class Register:

    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def run(self, instruction, val=None):
        method = getattr(self, instruction)
        if val is None:
            retval = method()
        else:
            retval = method(val)
        return retval

#     def snd(self):
# #        print("snd:", self.name)
#         try:
#             self.buddy.rcvqueue.append(int(self.value))
#         except TypeError:
#             self.buddy.rcvqueue.append(self.regist)
#
#         return "sound-" + str(self.value)

    def set(self, val):
#        print("set:", self.name, val)
        self.value = val
        return 1

    def add(self, val):
#        print("add:", self.name, val)
        self.value += val
        return 1

    def mul(self, val):
#        print("mul:", self.name, val)
        self.value *= val
        return 1

    def mod(self, val):
#        print("mod:", self.name, val)
        self.value = self.value % val
        return 1

#     def rcv(self):
#         if self.
# #        print("rcv:", self.name)
#         if self.value:
#             return "recover"
#         else:
#             return 1

    def jgz(self, val):
#        print("jgz:", self.name, val)
        if self.value > 0:
            return val
        else:
            return 1

instructions = list()

with open(sys.argv[1], 'r') as f:
    for line in f:
        instructions.append(line.strip())

instnum0 = instnum1 = 0

p0 = Program(0)
p1 = Program(1)
p0.setbuddyprog(p1)
p1.setbuddyprog(p0)
while not p0.waiting or not p1.waiting:
    try:
        ret0 = p0.run(instructions[instnum0])
        instnum0 += ret0
        # print("instnum0: ", instnum0)
        ret1 = p1.run(instructions[instnum1])
        instnum1 += ret1
        # print("instnum1: ", instnum1)
    except TypeError:
#        cpu.printregs()
        break
print(p1.totalsends)