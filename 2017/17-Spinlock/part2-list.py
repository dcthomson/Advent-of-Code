import sys

step = int(sys.argv[1])

# use linked list

spinlist = [0]

class Node:

    def __init__(self, num):
        self.num = num
        self.next = self

    def insertafter(self, node):
        node.next = self.next
        self.next = node
        return node

index = 0

for i in range(1, 50000000):
    if i % 100000 == 0:
        print(i)
    jndex = 0
    # print(index, "", end="")
    # print(spinlist)
    # for j in range(i):
    #     print(jndex, end="")
    #     jndex = spinlist[jndex]
    # print()
    # print()

    for j in range(0, step):
        index = spinlist[index]
    #     print(index, end="")
    # print()
    spinlist.append(spinlist[index])
    spinlist[index] = i
    index = spinlist[index]
print(spinlist[0])