import sys
from itertools import cycle

class Ring:
    def __init__(self, num):
        self.size = num
        self.elves = {}
        for i in range(1, num + 1):
            self.elves[i] = Elf()

    def __str__(self):
        s = ""
        for k, v in self.elves.items():
            s += "  " + str(k) + ": " + str(v) + "\n"
        return s    

    def nextelf(self, num):
        # print("1", num)
        num += 1
        if num > self.size:
            num = 1
        while self.elves[num].presents == 0:
            # print("Elf", num, "has no presents and is skipped.")
            num += 1
            # print(num, self.size)
            if num > self.size:
                num = 1
            # print("endnum:", num)
            
        # print("2", num)
        return num

    def transferpresents(self, giver, getter):
        # print("Elf", getter, "takes Elf", str(giver) + "'s present(s).")
        self.elves[getter].presents += self.elves[giver].presents
        self.elves[giver].presents = 0
        # self.elves.pop(giver, None)



class Elf:
    def __init__(self):
        self.presents = 1

    def __str__(self):
        return str(self.presents)

elfcount = int(sys.argv[1])
ring = Ring(elfcount)

curelf = 1

while elfcount > 1:
    # print("elfcount:", elfcount)
    # print("ring:\n",  ring)

    ne = ring.nextelf(curelf)
    ring.transferpresents(ne, curelf)
    elfcount -= 1
    curelf = ring.nextelf(curelf)

print(curelf)




# elves = []
# for i in range(0, 5):
#     elves.append(1)

# pool = cycle(elves)

# i = 0
# while len(pool) > 1:
#     del(pool[i + 1])
#     i += 1
# print(pool)