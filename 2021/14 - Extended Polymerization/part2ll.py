import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            nextnode = node.next
            yield node
            node = nextnode

polymer = ""
pairs = dict()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if " -> " in line:
            (pair, insert) = line.split(" -> ")
            pairs[pair] = insert
        elif line != '':
            polymer = LinkedList(list(line))

print(polymer)

for j in range(0, 30):
    print(j, ": ", end="")
    count = 0
    for n in polymer:
        count += 1
        # if n.next != None:
        try:
            newnode = Node(pairs[n.data + n.next.data])
            newnode.next = n.next
            n.next = newnode
        except AttributeError:  # if n.next == None
            pass

    print(count)

exit()

elements = dict()
for c in polymer:
    if c in elements:
        elements[c] += 1
    else:
        elements[c] = 0

lowest = None
highest = 0

for e, count in elements.items():
    if count > highest:
        highest = count
    if lowest is None or count < lowest:
        lowest = count

print(highest - lowest)