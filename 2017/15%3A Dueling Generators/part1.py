import sys

A = False
B = False

with open(sys.argv[1], 'r') as f:
    for line in f:
        if not A:
            A = int(line.split()[4])
        else:
            B = int(line.split()[4])

count = 0
for i in range(40000000):
    A *= 16807
    B *= 48271
    A = A % 2147483647
    B = B % 2147483647
    abin = format(A, 'b')
    bbin = format(B, 'b')
    if abin[-16:] == bbin[-16:]:
        count += 1
print(count)