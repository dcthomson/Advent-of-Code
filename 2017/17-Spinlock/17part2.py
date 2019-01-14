import sys

step = int(sys.argv[1])

# use linked list

cb = dict()

cb[0] = 0

index = 0

for i in range(1, 50000001):
    if i % 10000 == 0:
        print(i)
    for j in range(0, step):
        index = cb[index]
    tmp = cb[index]
    cb[index] = i
    cb[i] = tmp
    index = cb[index]
zero = cb[0]
print(cb[zero])