import sys
import functools

head = False

class Stone:
    def __init__(self, num):
        self.num = num
        self.next = None


    def blink(self):
        if self.num == 0:
            self.num = 1
            return self.next
        else:
            
            s = str(self.num)
            if not len(s) % 2:
                #split
                return self.split(s)
            else:
                self.num *= 2024
                return self.next
    # @functools.cache
    def split(self, s):
        mid = len(s) // 2
        self.num = int(s[:mid])
        stone = Stone(int(s[mid:]))
        stone.next = self.next
        self.next = stone
        return stone.next

    def __repr__(self):
        return str(self.num)

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        head = False

        for i in [int(x) for x in line.split()]:
            if not head:
                stone = Stone(i)
                head = stone
            else:
                stone.next = Stone(i)
                stone = stone.next

for i in range(0, 25):
    print(i)
    
    stone = head
    while stone.next:
        stone = stone.blink()
    stone.blink()

count = 0
stone = head
while True:
    count += 1
    if not stone.next:
        break
    stone = stone.next
print(count)