import sys
from itertools import cycle
from math import floor

class Ring:
    def __init__(self, num):
        self.size = num
        self.elves = []
        for i in range(1, num + 1):
            self.elves.append(i)

    # def __str__(self):
    #     s = ""
    #     for i in self.elves:
    #         s += "  " + str(i) + \n"
    #     return s    

    def nextelf(self, num):
        # print("1", num)
        num += 1
        if num > self.size:
            num = 1
        
        while num not in self.elves:
            # print("Elf", num, "has no presents and is skipped.")
            num += 1
            # print(num, self.size)
            if num > self.size:
                num = 1
            # print("endnum:", num)
            
        # print("2", num)
        return num

    def acrosself(self, num, size):
        # print(self.elves)
        # print("num:", num)
        # print("size:", size)
        # print("num:", num)
        # print("half", half)

        half = floor(size / 2)
        # print("half:", half)
        index = num + half
        # print("index:", index)
        if index in self.elves:
            return index
        else:
            return half - (size - num)
            

    def transferpresents(self, giver):
        # print("removed elf:", self.elves[giver])
        
        del self.elves[giver]



# elfcount = int(sys.argv[1])
elfcount = 5
ring = Ring(elfcount)

curelf = 0

while elfcount > 1:
    # try:
        # if not elfcount % 1000:
        print("elfcount:", elfcount)
        # print("ring:\n",  ring)

        ae = ring.acrosself(curelf, elfcount)
        # print("ae", ae)
        ring.transferpresents(ae)
        elfcount -= 1
        curelf = ring.nextelf(curelf)
    # except:
    #     print(ring.elves)
    #     break

print(curelf)
print(ring.elves[0])