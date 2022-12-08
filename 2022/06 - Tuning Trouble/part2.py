#  mjqjpqmgbljsphdztnvjfqwrcgsmlb

import sys

def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

packetlength = 14

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.rstrip()

        s = ""

        pos = 1

        for c in line:
            s += c
            if len(s) > packetlength:
                s = s[1:packetlength + 1]
            
            if len(s) == packetlength:
                if check_unique(s):
                    print(pos)
                    quit()
            pos += 1