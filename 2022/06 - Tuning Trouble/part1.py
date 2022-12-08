#  mjqjpqmgbljsphdztnvjfqwrcgsmlb

import sys

def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.rstrip()

        s = ""

        pos = 1

        for c in line:
            s += c
            if len(s) > 4:
                s = s[1:5]
            
            if len(s) == 4:
                if check_unique(s):
                    print(pos)
                    quit()
            pos += 1