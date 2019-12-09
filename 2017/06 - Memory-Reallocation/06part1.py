import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        banks = [int(x) for x in line.strip().split()]

oldbanks = dict()

count = 0

while True:
    if "-".join(str(x) for x in banks) in oldbanks:
        break
    oldbanks["-".join(str(x) for x in banks)] = 1
    largest = 0
    i = 0
    while i < len(banks):
        if banks[i] > largest:
            index = i
            largest = banks[i]
        i += 1
    banks[index] = 0
    while largest:
        index += 1
        try:
            banks[index] += 1
        except IndexError:
            index = 0
            banks[index] += 1
        largest -= 1
    count += 1

print(count)