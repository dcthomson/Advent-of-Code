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

    def reset(self):
        self.scanner = 0
        self.dir = 'down'


class Packet:

    def __init__(self, delay, lastscanner):
        self.delay = delay
        self.scanner = 0
        self.lastscanner = lastscanner

    def move(self):
        self.scanner += 1

    def through(self):
        if self.scanner > self.lastscanner:
            return True
        else:
            return False

    def caught(self, scanners):
        if self.scanner in scanners:
            if scanners[self.scanner].scanner == 0:
                # caught
                return True
        return False


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

packets = dict()

delay = 0
while True:
    packets[delay] = Packet(delay, largestscanner)

    # check for caught packets
    caughtkeys = list()
    for k in packets:
        if packets[k].caught(scanners):
            caughtkeys.append(k)

    # remove caught packets
    for k in caughtkeys:
        packets.pop(k)

    # move scanners
    for k in scanners:
        scanners[k].move()

    # move packets
    for k in packets:
        packets[k].move()
        if packets[k].through():
            print(packets[k].delay)
            sys.exit()

    delay += 1