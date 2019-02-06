import sys

class Scanner:

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.scanner = 0
        self.dir = 'down'

    def move(self):
        if self.dir == 'down':
            if self.scanner == self.size - 1:
                self.dir = 'up'
                self.scanner -= 1
            else:
                self.scanner += 1
        else:
            if self.scanner == 0:
                self.dir = 'down'
                self.scanner += 1
            else:
                self.scanner -= 1


    def __str__(self):
        return(str(self.name) + ": " + str(self.scanner) + " " + self.dir)

scanners = dict()

largestscanner = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        num, size = line.strip().split(": ")
        num = int(num)
        size = int(size)
        scanners[num] = Scanner(num, size)
        if num > largestscanner:
            largestscanner = num

i = 0
severity = 0
while i <= largestscanner:
    if i in scanners:
        if scanners[i].scanner == 0:
            severity += i * scanners[i].size
    for k in scanners:
        scanners[k].move()
    i += 1

print(severity)