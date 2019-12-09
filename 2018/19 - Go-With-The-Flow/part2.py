import sys
import os
import time

file = open(sys.argv[1], "r")

class Device:
    def __init__(self, ipreg, instructions):
        self.ipreg = int(ipreg)
        self.ip = 0
        self.regs = [1,0,0,0,0,0]
        self.instructions = list()
        for i in instructions:
            (op, A, B, C) = i.split(" ")
            instList = [getattr(self, op), int(A), int(B), int(C)]
            self.instructions.append(instList)

    def run(self):
        while 0 <= self.ip < len(self.instructions):
            instruction = self.instructions[self.ip]
            self.A = instruction[1]
            self.B = instruction[2]
            self.C = instruction[3]
            self.regs[self.ipreg] = self.ip
#            prtstr = "ip=%s %s " % (self.ip, self.regs)
#            prtstr += "%s %s %s %s " % (op, self.A, self.B, self.C)
            instruction[0]()
#            prtstr += str(self.regs)
            self.ip = self.regs[self.ipreg] + 1
#            print prtstr
            print(self.regs)
#             i = 0
#             print(instruction)
#             for reg in self.regs:
#                 print(i, reg)
#                 i += 1
            # time.sleep(1)
            # os.system('clear')
        # print "reg 0: %s" % (self.regs[0])

    def __str__(self):
        return str(self.regs)

    def addr(self):
        self.regs[self.C] = self.regs[self.A] + self.regs[self.B]

    def addi(self):
        self.regs[self.C] = self.regs[self.A] + self.B

    def mulr(self):
        self.regs[self.C] = self.regs[self.A] * self.regs[self.B]

    def muli(self):
        self.regs[self.C] = self.regs[self.A] * self.B

    def setr(self):
        self.regs[self.C] = self.regs[self.A]

    def seti(self):
        self.regs[self.C] = self.A

    def gtir(self):
        if self.A > self.regs[self.B]:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def gtri(self):
        if self.regs[self.A] > self.B:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def gtrr(self):
        if self.regs[self.A] > self.regs[self.B]:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def eqir(self):
        if self.A == self.regs[self.B]:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def eqri(self):
        if self.regs[self.A] == self.B:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def eqrr(self):
        if self.regs[self.A] == self.regs[self.B]:
            self.regs[self.C] = 1
        else:
            self.regs[self.C] = 0

    def banr(self):
        self.regs[self.C] = self.regs[self.A] & self.regs[self.B]

    def bani(self):
        self.regs[self.C] = self.regs[self.A] & self.B

    def borr(self):
        self.regs[self.C] = self.regs[self.A] | self.regs[self.B]

    def bori(self):
        self.regs[self.C] = self.regs[self.A] | self.B


instructions = list()
for line in file:
    if line.startswith("#ip "):
        ip = line.split(" ")[1]
    else:
        instructions.append(line)
        
dev = Device(ip, instructions)
dev.run()