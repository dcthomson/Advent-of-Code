import sys

A = False
B = False

with open(sys.argv[1], 'r') as f:
    for line in f:
        if not A:
            A = int(line.split()[4])
        else:
            B = int(line.split()[4])

alist = list()
blist = list()

count = 0
testcount = 0
while True:
    A *= 16807
    B *= 48271
    A = A % 2147483647
    B = B % 2147483647

    if int(str(A)[-2:]) % 4 == 0:
        alist.append(A)
    if int(str(B)[-3:]) % 8 == 0:
        blist.append(B)

    if len(alist) and len(blist):
        testcount += 1
        abin = format(alist.pop(0), 'b')
        bbin = format(blist.pop(0), 'b')
        if abin[-16:] == bbin[-16:]:
            count += 1
            print(testcount)
        if testcount == 5000000:
            break

print(count)