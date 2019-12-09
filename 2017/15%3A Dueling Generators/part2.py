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
listnum = 0
while True:
    A *= 16807
    B *= 48271
    A = A % 2147483647
    B = B % 2147483647

    # if int(str(A)[-2:]) % 4 == 0:
    #     alist.append(A)
    # if int(str(B)[-3:]) % 8 == 0:
    #     blist.append(B)

    if A % 100 % 4 == 0:
        alist.append(A)
    if B % 1000 % 8 == 0:
        blist.append(B)

    if len(alist) > listnum and len(blist) > listnum:
        testcount += 1
        abin = format(alist[listnum], 'b')
        bbin = format(blist[listnum], 'b')
        listnum += 1
        if abin[-16:] == bbin[-16:]:
            count += 1
        if testcount == 5000000:
            break

print(count)