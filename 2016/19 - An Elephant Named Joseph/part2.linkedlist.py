import sys
from math import floor

class Node:
    def __init__(self, num):
        self.num = num
        self.nref = None
        self.pref = None

class DoublyLinkedList:
    def __init__(self, num):
        new_node = Node(1)
        self.start_node = new_node
        n = new_node
        for i in range(2, num + 1):
            new_node = Node(i)
            n.nref = new_node
            new_node.pref = n
            n = new_node

        # link end to start
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.nref = self.start_node
        self.start_node.pref = n

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.num , " ")
                n = n.nref

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n
    
    def take_presents(self, curr_node, num):
        n = curr_node
        for _ in range(0, num):
            n = n.nref
        # print("Removing:", n.num)
        n.pref.nref = n.nref
        n.nref.pref = n.pref
        return n

    def link_end_to_start(self):
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.nref = self.start_node
        self.start_node.pref = n
        

elfcount = int(sys.argv[1])

elves = DoublyLinkedList(elfcount)

# elves.traverse_list()

# elves.insert_in_emptylist(1)

# for i in range(2, elfcount + 1):
#     print(i)
#     elves.insert_at_end(i)

# elves.create_list(elfcount)

curr_elf = elves.start_node

while elfcount > 1:
    print(elfcount)
    half = floor(elfcount / 2)
    elves.take_presents(curr_elf, half)
    elfcount -= 1
    curr_elf = curr_elf.nref

print(curr_elf.num)

# firstelf.prevelf = lastelf

# currelf = lastelf
# while currelf.num != 1