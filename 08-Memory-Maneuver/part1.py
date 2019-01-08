file = open("input.txt", "r")

input = list()

for line in file:
    input = line.split()

total = 0

def getnode(t):
    childnodes = int(input.pop(0))
    metadatas = int(input.pop(0))
    for i in range(childnodes):
        t = getnode(t)
    for i in range(metadatas):
        t += int(input.pop(0))
    return t

total = getnode(total)
    
print total
