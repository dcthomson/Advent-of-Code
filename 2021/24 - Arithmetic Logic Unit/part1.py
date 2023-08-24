import sys

class ALU:

    def __init__(self):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.ok = True

    def aluget(self, c):
        if c == 'w':
            return self.w
        elif c == 'x':
            return self.x
        elif c == 'y':
            return self.y
        elif c == 'z':
            return self.z
        else:
            raise ValueError("Value is not a register: w,x,y,z")
        
    def aluset(self, c, n):
        if c == 'w':
            self.w = n
        elif c == 'x':
            self.x = n
        elif c == 'y':
            self.y = n
        elif c == 'z':
            self.z = n


    def inp(self, a, b):
        self.aluset(a, b)
         
    def add(self, a, b):
        try:
            self.aluset(a, self.aluget(a) + self.aluget(b))
        except ValueError:
            self.aluset(a, self.aluget(a) + int(b))

    def mul(self, a, b):
        try:
            self.aluset(a, self.aluget(a) * self.aluget(b))
        except ValueError:
            self.aluset(a, self.aluget(a) * int(b))

    def div(self, a, b):
        try:
            if self.aluget(b) == 0:
                self.ok = False
                return
        except ValueError:
            if b == 0:
                self.ok = False
                return
        try:
            self.aluset(a, int(self.aluget(a) / self.aluget(b)))
        except ValueError:
                self.aluset(a, int(self.aluget(a) / int(b)))

    def mod(self, a, b):
        if self.aluget(a) < 0:
            self.ok = False
            return
        try:
            if self.aluget(b) <= 0:
                self.ok = False
                return
        except ValueError:
            if int(b) <= 0:
                self.ok = False
                return
        try:
            self.aluset(a, self.aluget(a) % self.aluget(b))
        except ValueError:
            self.aluset(a, self.aluget(a) % int(b))

    def eql(self, a, b):
        try:
            if self.aluget(a) == self.aluget(b):
                self.aluset(a, 1)
            else:
                self.aluset(a, 0)
        except ValueError:
            if self.aluget(a) == int(b):
                self.aluset(a, 1)
            else:
                self.aluset(a, 0)

    def __str__(self) -> str:
        retstr = "w: " + str(self.w)
        retstr += " -- "
        retstr += "x: " + str(self.x)
        retstr += " -- "
        retstr += "y: " + str(self.y)
        retstr += " -- "
        retstr += "z: " + str(self.z)
        return retstr

instructions = []

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        instructions.append(line)

num =       100000000000000

while num > 10000000000000:
    num -= 1
    nstr = str(num)
    # print("num: ", nstr)
    if '0' in nstr: # skip number if it has a 0
        zeroindex = nstr.find('0')
        s = nstr[:zeroindex]
        while len(s) < 14:
            s += "0"
            prevnum = num
        num = int(s)
        print("0 Found -- SKIP:", nstr, "->", s)
        continue
    alu = ALU()
    currnum = ""
    for instruction in instructions:
        # print(instruction)
        i = instruction.split()
        if i[0] == 'inp':
            # print("new")
            # print(alu)
            # print()
            n = int(nstr[0])
            currnum += str(n)
            nstr = nstr[1:]
            alu.inp(i[1], n)
        elif i[0] == 'add':
            alu.add(i[1], i[2])
        elif i[0] == 'mul':
            alu.mul(i[1], i[2])
        elif i[0] == 'div':
            alu.div(i[1], i[2])
        elif i[0] == 'mod':
            alu.mod(i[1], i[2])
        elif i[0] == 'eql':
            alu.eql(i[1], i[2])
        if not alu.ok: # skip num if it has an error
            while len(currnum) < 14:
                currnum += "0"
                prevnum = num
            num = int(currnum)
            print("ALU-NOT OK -- SKIP:", nstr, "->", currnum)
            break
        # print(alu)
        prevnum = num
    if not alu.ok:
        continue
    if alu.z == 0:
        print(str(num))
        break
    else:
        pass
        # print("z:", alu.z)