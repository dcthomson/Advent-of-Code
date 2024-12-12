import sys
import math
import functools

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        m = min(len(str(x)), len(str(y))) // 2
        x1, x0 = divmod(x, 10**m)
        y1, y0 = divmod(y, 10**m)
        z0 = karatsuba(x0, y0)
        z1 = karatsuba((x0 + x1), (y0 + y1))
        z2 = karatsuba(x1, y1)
        return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

class Stone:
    def __init__(self, num):
        self.num = num
        self.next = False

    @functools.cache
    def blink(self):
        if self.num == 0:
            self.num = 1
        else:
            cnum = int(math.log10(self.num))+1
            if not cnum % 2:
                # print("num:", self.num)
                # print("cnum:", cnum)
                half = cnum / 2
                l = self.num // int(10 ** half) 
                r = self.num % int(10 ** half)
                # print(l, r)
                stone = Stone(self.num % int(10 ** half))
                self.num = self.num // int(10 ** half)
                stone.next = self.next
                self.next = stone
                # print()
                return stone.next
            else:
                # print("self.num:", self.num)
                # thousand = int(s + "000")
                # print("self.num:", self.num)
                # self.num <<= 10
                # self.num += thousand
                # print("self.num:", self.num)
                # print()
                self.num = karatsuba(self.num, 2024)
        return self.next

    def __repr__(self):
        return str(self.num)

def main():
    head = False

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

    for i in range(0, 26):
        print("i:",i)
        
        stone = head
        while stone.next:
            stone = stone.blink()
        stone.blink()


    count = 0
    stone = head
    while True:
        # print(stone.num, end=" ")
        count += 1
        if not stone.next:
            break
        stone = stone.next
    # print()
    print(count)

main()
#cProfile.run('main()')