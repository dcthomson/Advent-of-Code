import sys

step = int(sys.argv[1])

# use linked list

class Node:
    # don't really need prev
    # but we'll add it just in case part 2 needs it
    def __init__(self, num):
        self.num = num
        self.next = self
        self.prev = self

    def insertafter(self, node):
        self.prev = node
        self.next = node.next
        self.next.prev = self
        node.next = self
        return self

index = Node(0)
zero = index

for i in range(1, 2018):
    for j in range(0, step):
        index = index.next
    n = Node(i)
    index = n.insertafter(index)

index = index.next
print(index.num)