import sys
import hashlib

class Num:

    def __init__(self, num, salt):
        self.md5 = hashlib.md5(str(salt + str(num)).encode('utf-8')).hexdigest()

        for _ in range(0, 2016):
            self.md5 = hashlib.md5(self.md5.encode('utf-8')).hexdigest()

        self.three = False
        curc = ""
        curnum = 0
        for c in self.md5:
            if curc == c:
                curnum += 1
            else:
                curnum = 1
            if curnum == 3:
                self.three = c
                break
            curc = c

        self.five = {}

        curc = ""
        curnum = 0
        for c in self.md5:
            if curc == c:
                curnum += 1
            else:
                curnum = 1
            if curnum == 5:
                self.five[curc] = True
            curc = c

salt = sys.argv[1]

keys = []
index = 0
nums = {}

while len(keys) < 64:

    if not index in nums:
        nums[index] = Num(index, salt)

    if nums[index].three:
        for i in range(index + 1, index + 1001):
            if not i in nums:
                nums[i] = Num(i, salt)
            if nums[index].three in nums[i].five:
                keys.append(index)
                print(index)
                break
    index += 1

print(keys[63])