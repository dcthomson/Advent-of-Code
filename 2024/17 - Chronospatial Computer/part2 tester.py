import sys

rega = regb = regc = 0
program = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        if line.startswith("Register A"):
            rega = int(line.split()[2])
        if line.startswith("Register B"):
            regb = int(line.split()[2])
        if line.startswith("Register C"):
            regc = int(line.split()[2])
        if line.startswith("Program:"):
            program = [int(x) for x in line.split()[1].split(",")]

# print(rega,regb,regc,program)

class opcode:

    def __init__(self, program, a=0, b=0, c=0):
        self.rega = a
        self.regb = b
        self.regc = c
        self.program = program
        self.ip = 0
        self.output = []

    def run(self):
        try:
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
        except:
            return False
        if opcode == 3:
            self.jnz(operand)
        else:
            if opcode == 0:
                self.adv(operand)
            elif opcode == 1:
                self.bxl(operand)
            elif opcode == 2:
                self.bst(operand)
            elif opcode == 4:
                self.bxc()
            elif opcode == 5:
                self.out(operand)
            elif opcode == 6:
                self.bdv(operand)
            elif opcode == 7:
                self.cdv(operand)
            self.ip += 2

        return True


    def adv(self, operand):
        self.rega = int(self.rega / pow(2, self.combo(operand)))
    def bxl(self, operand):
        self.regb = self.regb ^ operand
    def bst(self, operand):
        self.regb = self.combo(operand) % 8
    def jnz(self, operand):
        if self.rega != 0:
            self.ip = operand
        else:
            self.ip += 2
    def bxc(self):
        self.regb = self.regb ^ self.regc
    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
    def bdv(self, operand):
        self.regb = int(self.rega / pow(2, self.combo(operand)))
    def cdv(self, operand):
        self.regc = int(self.rega / pow(2, self.combo(operand)))

    def combo(self, i):
        if i <= 3:
            return i
        elif i == 4:
            return self.rega
        elif i == 5:
            return self.regb
        elif i == 6:
            return self.regc
        elif i == 7:
            print("Program Invalid")
            exit()

for i in range(4096):
    oc = opcode(program, i, regb, regc)
    # oc = opcode(program, int(sys.argv[2]), regb, regc)
    running = True
    while running:
        running = oc.run()
    if oc.output == program:
        print("Found!!!")
        print(i, ":", ",".join(str(x) for x in oc.output))
        break
    print(i, ":", ",".join(str(x) for x in oc.output))