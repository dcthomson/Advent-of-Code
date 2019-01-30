import sys
import string
from operator import itemgetter

sectorsum = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        (front, checksum) = line.strip().split("[")
        checksum = checksum.strip(']')
        front = front.split("-")
        sector = int(front[-1])
        letters = "".join(front[:-1])
        checkdict = dict()
        for c in string.ascii_lowercase:
            checkdict[c] = letters.count(c)
        i = 0
        mycheck = ""
        for k, v in sorted(checkdict.items(), key=itemgetter(1), reverse=True):
            if i < 5:
                mycheck += str(k)
            else:
                break
            i += 1
        if mycheck == checksum:
            sectorsum += sector

print(sectorsum)