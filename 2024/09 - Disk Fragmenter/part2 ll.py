import sys
import time

class File:
    def __init__(self, size, id=False, prev=False):
        self.id = id
        self.size = size
        self.processed = False
        self.next = False
        self.prev = prev

    def __repr__(self):
        if self.id:
            return str(self.id) * self.size
        else:
            return "." * self.size

diskstart = diskend = False

with open(sys.argv[1], "r") as f:

    for line in f:
        line = line.strip()

        node = False

        id = 0
        for i, c in enumerate(line):
            if not i % 2:
                if not node:
                    diskstart = File(int(c), id)
                    node = diskstart
                else:
                    node.next = File(int(c), id, node)
                    node.next.prev = node
                    node = node.next
                id += 1
            else:
                node.next = File(int(c), False, node)
                node.next.prev = node
                node = node.next
        diskend = node

def printdisk(disk, reversed=False):
    node = disk
    while True:
        # time.sleep(1)
        if node.id is not False:
            print(str(node.id) * node.size, end="", flush=True)
        else:
            print("." * node.size, end="", flush=True)
        if not reversed:
            if node == diskend:
                break
            node = node.next
        else:
            if node == diskstart:
                break
            node = node.prev

filenode = diskend

while filenode != diskstart:
    fprev = filenode.prev
    if filenode.id is not False and filenode.processed is False:
        filenode.processed = True
        fnext = filenode.next
        spacenode = diskstart
        while True:
            start = end = False
            if filenode == spacenode:
                break
            if spacenode.id is False:
                if filenode.size <= spacenode.size:
                    sprev = spacenode.prev
                    snext = spacenode.next
                    spacenode.prev.next = filenode
                    filenode.prev = spacenode.prev
                    if filenode.size < spacenode.size:
                        # space bigger than file
                        newspace = File(spacenode.size - filenode.size)
                        spacenode.size = filenode.size           
                        filenode.next = newspace
                        newspace.prev = filenode
                        newspace.next = spacenode.next
                        spacenode.next.prev = newspace
                    elif filenode.size == spacenode.size:
                        # file same size as space
                        # filenode.prev = spacenode.prev
                        filenode.next = spacenode.next                   
                    fprev.next = spacenode
                    try:
                        fnext.prev = spacenode
                    except:
                        diskend = spacenode
                    snext.prev = filenode
                    spacenode.next = fnext
                    spacenode.prev = fprev

                    break
                
                spacenode = spacenode.next
            else:
                spacenode = spacenode.next
    filenode = fprev

i = total = 0
node = diskstart

while node != diskend:
    if node.id:
        for j in range(i, i + node.size):
            total += node.id * j
    i += node.size
    node = node.next
print(total)