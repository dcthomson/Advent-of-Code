import sys

disk = int(sys.argv[1])
data = sys.argv[2]

def filldisk(s, disksize):
    while len(s) < disksize:
        a = s
        b = '0'
        for c in a[::-1]:
            if c == '1':
                b += '0'
            else:
                b += '1'
        s = a + b
        print("filldisk:", len(s))
    return s[:disksize]

def checksum(s):
    while not len(s) % 2:
        # i = 0
        # for c in s:
        #     print(c, end='')
        #     if i % 2:
        #         print(" ", end="")
        #     i += 1
        # print()
        newchecksum = ""
        left = False
        for c in s:
            if not left:
                left = c
            else:
                right = c
                if left == right:
                    newchecksum += "1"
                else:
                    newchecksum += "0"
                left = False
        s = newchecksum
        # for c in s:
        #     print(c, " ", end='')
        # print()
        print("checksum:", len(s))
    return s

fd = filldisk(data, disk)
print("disk filled")
print(checksum(fd))