import sys

step = int(sys.argv[1])

# use linked list

cb = list()

cb.append(0)

index = 0

for i in range(1, 11):
    if i % 10000 == 0:
        print(i)
    print(index, cb)
    for j in range(0, step):
        index = cb[index]
    print(index)
    tmp = cb[index]
    cb.insert(index, i)
    cb[i] = tmp
#    index = cb[index]
print(cb[index])