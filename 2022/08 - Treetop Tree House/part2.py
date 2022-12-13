import sys

trees = {}
mostvisible = 0

with open(sys.argv[1], "r") as f:

    y = 0

    for line in f:
        line = line.strip()

        x = 0

        for c in line:
            trees[(x,y)] = int(c)
            x += 1
        
        y += 1

for k in trees:
    visibleprod = 1
    increments = ((1,0), (-1,0), (0,1), (0,-1))
    for increment in increments:
        visible = 0
        curtreekey = (k[0] + increment[0], k[1] + increment[1])
        while True:
            if curtreekey not in trees:
                break
            elif trees[curtreekey] < trees[k]:
                visible += 1
            else:
                visible += 1
                break
            curtreekey = (curtreekey[0] + increment[0], curtreekey[1] + increment[1])
        visibleprod *= visible
    if visibleprod > mostvisible:
        mostvisible = visibleprod

print(mostvisible)