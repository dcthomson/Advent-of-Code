import time
import sys

file = open("input.txt", "r")

class Device:
    def __init__(self, opcodes, a=0, b=0, c=0, d=0):
        self.opcodes = opcodes
        self.regs = [a, b, c, d]

    def runInstruction(self, inst):
        (opcode, self.A, self.B, self.C) = map(int, inst.split())
        method = getattr(self, opcodes[opcode])
        method()

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

class Operation:
    def __init__(self, before):
        self.before = self.strtoint(before)
        self.after = self.before

    def strtoint(self, quad):
        return [int(quad[0]), int(quad[1]), int(quad[2]), int(quad[3])]

    def setInstructions(self, i):
        self.instructions = self.strtoint(i)
        self.vala = self.instructions[1]
        self.valb = self.instructions[2]
        self.rega = self.before[self.instructions[1]]
        self.regb = self.before[self.instructions[2]]
        self.regc = self.instructions[3]
        self.opcode = self.instructions[0]


    def addr(self):
        self.after[self.regc] = self.rega + self.regb
#        print "addr:         " + str(self.after)
        return self.after

    def addi(self):
        self.after[self.regc] = self.rega + self.valb
#        print "addi:         " + str(self.after)
        return self.after

    def mulr(self):
        self.after[self.regc] = self.rega * self.regb
#        print "mulr:         " + str(self.after)
        return self.after

    def muli(self):
        self.after[self.regc] = self.rega * self.valb
#        print "muli:         " + str(self.after)
        return self.after

    def setr(self):
        self.after[self.regc] = self.rega
#        print "setr:         " + str(self.after)
        return self.after

    def seti(self):
        self.after[self.regc] = self.vala
#        print "seti:         " + str(self.after)
        return self.after

    def gtir(self):
        if self.vala > self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "gtir:         " + str(self.after)
        return self.after

    def gtri(self):
        if self.rega > self.valb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "gtri:         " + str(self.after)
        return self.after

    def gtrr(self):
        if self.rega > self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "gtrr:         " + str(self.after)
        return self.after

    def eqir(self):
        if self.vala == self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "eqir:         " + str(self.after)
        return self.after

    def eqri(self):
        if self.rega == self.valb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "eqri:         " + str(self.after)
        return self.after

    def eqrr(self):
        if self.rega == self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
#        print "eqrr:         " + str(self.after)
        return self.after

    def banr(self):
        self.after[self.regc] = self.rega & self.regb
#        print "banr:         " + str(self.after)
        return self.after

    def bani(self):
        self.after[self.regc] = self.rega & self.valb
#        print "bani:         " + str(self.after)
        return self.after

    def borr(self):
        self.after[self.regc] = self.rega | self.regb
#        print "borr:         " + str(self.after)
        return self.after

    def bori(self):
        self.after[self.regc] = self.rega | self.valb
#        print "bori:         " + str(self.after)
        return self.after

blank = 0
oper = None
opcodedict = dict()
opcodelists = dict()
totalcount = 0
firstpart = True
instructionList = list()
for line in file:
    if firstpart:
        if line.startswith("Before:"):
            before = line.split("[")[1]
            before = before.split("]")[0]
            before = before.split(", ")
            oper = Operation(before)
            blank = 0
#            print "before:       " + str(oper.before)
        elif line.startswith("After:"):
            after = line.split("[")[1]
            after = after.split("]")[0]
            after = after.split(", ")
            after = oper.strtoint(after)
#            print "after:        " + str(after)
            blank = 0
            count = 0
            opcode = list()
            if oper.addr() == after:
                opcode.append("addr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.addi() == after:
                opcode.append("addi")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.mulr() == after:
                opcode.append("mulr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.muli() == after:
                opcode.append("muli")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.banr() == after:
                opcode.append("banr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.bani() == after:
                opcode.append("bani")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.borr() == after:
                opcode.append("borr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.bori() == after:
                opcode.append("bori")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.setr() == after:
                opcode.append("setr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.seti() == after:
                opcode.append("seti")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.gtir() == after:
                opcode.append("gtir")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.gtri() == after:
                opcode.append("gtri")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.gtrr() == after:
                opcode.append("gtrr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.eqir() == after:
                opcode.append("eqir")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.eqri() == after:
                opcode.append("eqri")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.eqrr() == after:
                opcode.append("eqrr")
                if oper.opcode not in opcodedict:
                    opcodedict[oper.opcode] = dict()
                opcodedict[oper.opcode][opcode[-1]] = 1
            if oper.opcode not in opcodelists:
                opcodelists[oper.opcode] = list()
            opcodelists[oper.opcode].append(opcode)
            
        elif line.rstrip() == "":
            blank += 1
            if blank == 2:
                firstpart = False
        else:
            instructions = line.split()
            oper.setInstructions(instructions)
#            print "instructions: " + str(oper.instructions)
    elif firstpart == False:
        if " " in line.strip():
            instructionList.append(line.strip())

opcodes = dict()

def ruleout(d):
    found = False
    while not found:
        found = True
        dellist = list()
        for k in d:
            if len(d[k]) == 1:
                found = False
                for code in d[k]:
                    opcodes[k] = code
                    dellist.append(k)
        for todelete in dellist:
            for k in d[todelete]:
                todeletekey = k
            del d[todelete]
            for k in d:
                if todeletekey in d[k]:
                    del d[k][todeletekey]
    

    return opcodes

#print "-----FIRST-----"
#for k in opcodedict:
#    print str(k) + ": " + str(opcodedict[k])

opcodedict = ruleout(opcodedict)

dev = Device(opcodedict)

for instruction in instructionList:
    dev.runInstruction(instruction)

print dev
