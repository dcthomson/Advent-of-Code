import sys

step = int(sys.argv[1])

# use linked list

class Node:

    def __init__(self, num):
        self.num = num
        self.next = self

    def insertafter(self, node):
        node.next = self.next
        self.next = node
        return node

index = Node(0)

for i in range(1, 50000000):
    print(i, round(i / 50000000 * 100, 2))
    for j in range(0, step):
        index = index.next
    index = index.insertafter(Node(i))

index = index.next
print(index.num)