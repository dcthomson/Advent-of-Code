import sys
import time

class Node:

    def __init__(self, num, index):
        self.num = num
        self.next = index + 1
        self.prev = index - 1

    def __repr__(self):
        return str(self.prev) + str(self.num) + str(self.next)

coords = []

index = 0

def printcoords(coords):

    i = 0
    while True:
        print(coords[i].num, "", end="")
        i = coords[i].next
        if i == 0:
            print()
            break
    

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        coords.append(Node(int(line), index))

        index += 1

coords[index - 1].next = 0
coords[0].prev = index - 1

for n in range(index):
    if coords[n].num == 0:
        continue
    # remove from linkedlist
    coords[coords[n].prev].next = coords[n].next
    coords[coords[n].next].prev = coords[n].prev

    #insert back into linkedlist
    k = n
    if coords[n].num >= 0:
        for _ in range(coords[n].num):
            k = coords[k].next
    else:
        for _ in range(0, coords[n].num - 1, -1):
            k = coords[k].prev
    coords[n].next = coords[k].next
    coords[n].prev = coords[coords[n].next].prev
    coords[coords[n].next].prev = n
    coords[k].next = n

n = coords[0]

while True:
    if n.num == 0:
        break
    else:
        n = coords[n.next]

one = n
two = n
three = n

for _ in range(1000):
    one = coords[one.next]

for _ in range(2000):
    two = coords[two.next]

for _ in range(3000):
    three = coords[three.next]

print(one.num + two.num + three.num)