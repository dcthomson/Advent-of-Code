import sys

class Program:

    def __init__(self, prognum):
        self.prognum = prognum
        self.registers = dict()
        self.registers['p'] = Register('p')
        self.registers['p'].set(prognum)
        self.waiting = False
        self.rcvreg = False
        self.rcvqueue = []
        self.totalsends = 0

    def setbuddyprog(self, buddy):
        self.buddyprog = buddy

    def run(self, instruction):
        self.waiting = False

        instlist = instruction.split()
        # print(self.prognum, instlist, self.rcvqueue)
        # print(self.prognum, instlist, self.getregsstr())
        instruction = instlist[0]
        regletter = instlist[1]

        retval = 1

        if len(instlist) == 3:
            try:
                value = int(regletter)
                print("INSTLIST", instlist)
                retval = 3
            except:
                if regletter not in self.registers:
                    # add regletter
                    self.registers[regletter] = Register(regletter)
                try:
                    # 3rd arg is int
                    value = int(instlist[2])
                except ValueError:
                    # 3rd arg is letter
                    try:
                        value = self.registers[instlist[2]].value
                    except KeyError:
                        print("ERROR:", instlist)
                        sys.exit()

                retval = self.registers[regletter].run(instruction, value)
        else:
            # only 2 args (snd and rcv)
            value = None
            retval = 1
            if instruction == 'snd':
                try:
                    self.buddyprog.rcvqueue.append(int(instlist[1]))
                except:
                    self.buddyprog.rcvqueue.append(self.registers[regletter].value)
                self.totalsends += 1
            elif instruction == 'rcv':
                if regletter not in self.registers:
                    # add regletter
                    self.registers[regletter] = Register(regletter)
                # print(self.prognum, "len:", len(self.rcvqueue))
                if len(self.rcvqueue):
                    self.registers[regletter].set(self.rcvqueue.pop(0)) 
                else:
                    # print("waiting")
                    self.waiting = True
                    retval = 0
        return retval

    def getregsstr(self):
        retstr = ""
        for k in self.registers:
            retstr += str(self.registers[k].name) + ": "
            retstr += str(self.registers[k].value) + ", "
        retstr += "\n  Q: " + str(self.rcvqueue)
        return retstr.rstrip(", ")


class Register:

    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def run(self, instruction, val):
        method = getattr(self, instruction)
        retval = method(val)
        return retval

    def set(self, val):
        self.value = val
        return 1

    def add(self, val):
        self.value += val
        return 1

    def mul(self, val):
        self.value *= val
        return 1

    def mod(self, val):
        self.value = self.value % val
        return 1

    def jgz(self, val):
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
    # try:
        print("0", instructions[instnum0])
        instnum0 += p0.run(instructions[instnum0])
        print(p0.getregsstr())
        print(p1.getregsstr())
        # print("instnum0: ", instnum0)
        print()
        print("1", instructions[instnum1])
        instnum1 += p1.run(instructions[instnum1])
        print(p0.getregsstr())
        print(p1.getregsstr())
        print()
        print(p0.waiting, p1.waiting)
        # input()
        # print(p1.totalsends)
        # print("instnum1: ", instnum1)
    # except:
    #     print("ERROR")
    #     break

print(p1.totalsends)