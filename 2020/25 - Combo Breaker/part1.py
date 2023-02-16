import sys

door = False
key = False

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if not key:
            key = int(line)
        else:
            door = int(line)

subnum = 7
i = 1
num = 0
while i != key:
    i = (i*subnum) % 20201227
    num += 1
print(num)

subnum = door
i = 1
for _ in range(0, num):
    i = (i*subnum) % 20201227
print(i)