file = open("input.txt", "r")

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

    def addr(self):

        self.after[self.regc] = self.rega + self.regb
        return self.after

    def addi(self):
        self.after[self.regc] = self.rega + self.valb
        return self.after

    def mulr(self):
        self.after[self.regc] = self.rega * self.regb
        return self.after

    def muli(self):
        self.after[self.regc] = self.rega * self.valb
        return self.after

    def setr(self):
        self.after[self.regc] = self.rega
        return self.after

    def seti(self):
        self.after[self.regc] = self.vala
        return self.after

    def gtir(self):
        if self.vala > self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def gtri(self):
        if self.rega > self.valb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def gtrr(self):
        if self.rega > self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def eqir(self):
        if self.vala == self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def eqri(self):
        if self.rega == self.valb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def eqrr(self):
        if self.rega == self.regb:
            self.after[self.regc] = 1
        else:
            self.after[self.regc] = 0
        return self.after

    def banr(self):
        self.after[self.regc] = self.rega & self.regb
        return self.after

    def bani(self):
        self.after[self.regc] = self.rega & self.valb
        return self.after

    def borr(self):
        self.after[self.regc] = self.rega | self.regb
        return self.after

    def bori(self):
        self.after[self.regc] = self.rega | self.valb
        return self.after

blank = 0
oper = None
codes = dict()
totalcount = 0
firstpart = True
for line in file:
    if firstpart:
        if line.startswith("Before:"):
            before = line.split("[")[1]
            before = before.split("]")[0]
            before = before.split(", ")
            oper = Operation(before)
            blank = 0
        elif line.startswith("After:"):
            after = line.split("[")[1]
            after = after.split("]")[0]
            after = after.split(", ")
            after = oper.strtoint(after)
            blank = 0
            count = 0
            if oper.addr() == after:
                count += 1 
            if oper.addi() == after:
                count += 1
            if oper.mulr() == after:
                count += 1 
            if oper.muli() == after:
                count += 1 
            if oper.banr() == after:
                count += 1 
            if oper.bani() == after:
                count += 1 
            if oper.borr() == after:
                count += 1 
            if oper.bori() == after:
                count += 1 
            if oper.setr() == after:
                count += 1 
            if oper.seti() == after:
                count += 1 
            if oper.gtir() == after:
                count += 1 
            if oper.gtri() == after:
                count += 1 
            if oper.gtrr() == after:
                count += 1 
            if oper.eqir() == after:
                count += 1 
            if oper.eqri() == after:
                count += 1 
            if oper.eqrr() == after:
                count += 1 
            if count >= 3:
                totalcount += 1
            
        elif line.rstrip() == "":
            blank += 1
            if blank == 2:
                firstpart = False
        else:
            instructions = line.split()
            oper.setInstructions(instructions)

print(totalcount)
