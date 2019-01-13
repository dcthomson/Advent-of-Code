import sys

step = sys.argv[1]

# use linked list

def stepforward(index, cb):
    return cb[index]

def insertafter(index, val, cb):
    tmp = cb[index]
    cb[index] = val
    cb[val] = tmp
    return cb

cb = dict()

cb[0] = 0

index = 0

for i in range(1, 2107):
    for j in (0, step):
        index = stepforward(index, cb)
    cb = insertafter(index, i, cb)
