import sys

trees = {}

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            trees[(x,y)] = int(c)
            x += 1
        
        y += 1

totalvisible = 0

for k in trees:
    visible = False
    increments = ((1,0), (-1,0), (0,1), (0,-1))

    for increment in increments:
        if visible:
            break
        curtreekey = (k[0] + increment[0], k[1] + increment[1])
        while True:
            if curtreekey not in trees:
                visible = True
                totalvisible += 1
                break
            
            if trees[curtreekey] >= trees[k]:
                break
            curtreekey = (curtreekey[0] + increment[0], curtreekey[1] + increment[1])


print(totalvisible)