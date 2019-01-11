import sys

f = open(sys.argv[1], 'r')

checksum = 0

for line in f:
    low = False
    high = False
    for num in list(map(int, line.rstrip().split())):
        if not low or num < low:
            low = num
        if not high or num > high:
            high = num
    checksum += high - low

print(checksum)
