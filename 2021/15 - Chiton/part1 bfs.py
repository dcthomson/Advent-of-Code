#from logging.config import _RootLoggerConfiguration
import sys
import time
import os


##############################################
### LETS TRY BFS
##############################################

grid = {}

maxx = 0
maxy = 0

with open(sys.argv[1], "r") as f:
    y = 0
    for line in f:
        x = 0
        for c in list(line.rstrip()):
            grid[(x,y)] = int(c)
            x += 1
        maxx = x
        y += 1
    maxy = y

def printshortest(shortest):
    
    os.system('cls')

    longest = 0

    for k in shortest:
        stepslen = len(str(shortest[k]))
        if stepslen > longest:
            longest = stepslen

    for y in range(0, maxy):
        for x in range(0, maxx):
            if (x,y) not in shortest:
                for i in range(0, longest):
                    print("_", end="")
            else:
                stepsstr = str(shortest[(x,y)])
                for i in range(0, longest - len(stepsstr)):
                    print("_", end="")
                print(stepsstr, end="")
            print(" ", end="")
        print()
    

queue = []
shortest = {}
steps = 0

queue.append(((0,0), 0))

while queue:
    (coord, steps) = queue.pop(0)

    printshortest(shortest)

    if coord not in shortest or steps < shortest[coord]:
        shortest[coord] = steps

        for i in range(1, 10):
            for c in ((coord[0], coord[1] + 1),
                    (coord[0] + 1, coord[1]),
                    (coord[0], coord[1] - 1),
                    (coord[0] - 1, coord[1])):
                try:
                    if grid[c] == i:
                        queue.append((c, steps + grid[c]))
                except:
                    pass

print(shortest[(maxx-1, maxy-1)])