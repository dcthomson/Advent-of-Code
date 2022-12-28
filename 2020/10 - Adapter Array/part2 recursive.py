import sys

adapters = []

with open(sys.argv[1], "r") as f:
    for line in f:
        adapters.append(int(line.rstrip()))

adapters.sort()

print(adapters)

max = adapters[-1]

arrangements = 0

def getnext(i):
    if i == max:
        global arrangements
        arrangements += 1
        if arrangements % 1000000 == 0:
            print(arrangements)
    for j in range(1, 4):
        if i + j in adapters:
            getnext(i + j)

getnext(0)

print(arrangements)