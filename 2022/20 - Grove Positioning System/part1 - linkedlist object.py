import sys
import time

class Node:

    def __init__(self, num, index):
        self.num = num
        self.next = index + 1
        self.prev = index - 1

    def __repr__(self):
        return str(self.prev) + str(self.num) + str(self.next)

class LinkedList:

    def __init__(self, numlist):
        self.nums = []
        index = 0
        for num in numlist:
            self.nums.append(Node(num, index))
            index += 1
        self.nums[index - 1].next = 0
        self.nums[0].prev = index - 1

    def __str__(self):
        i = 0
        liststr = ""
        while True:
            liststr += str(self.nums[i].num) + " "
            i = self.nums[i].next
            if i == 0:
                return liststr

nums = []

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        nums.append(int(line))

ll = LinkedList(nums)
print(ll)
    

# for n in range(index):
#     # remove from linkedlist
#     coords[coords[n].prev].next = coords[n].next
#     coords[coords[n].next].prev = coords[n].prev

#     #insert back into linkedlist
#     k = n
#     if coords[n].num >= 0:
#         for _ in range(coords[n].num):
#             k = coords[k].next
#     else:
#         for _ in range(coords[n].num, -1):
#             k = coords[k].prev
#     coords[n].next = coords[k].next
#     coords[n].prev = coords[coords[n].next].prev
#     coords[coords[n].next].prev = n
#     coords[k].next = n

#     printcoords(coords)
#     time.sleep(5)