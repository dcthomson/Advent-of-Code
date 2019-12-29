import sys

lastx = 31
lasty = 39

def walloropen(x, y, fav):
    sum = x*x + 3*x + 2*x*y + y + y*y + fav
    s = '{0:b}'.format(sum)
    onenum = s.count('1')
    if onenum % 2:
        return "#"
    else:
        return "."

fav = int(sys.argv[1])

# for y in range(0,45):
#     for x in range(0,37):
#         print(walloropen(x,y,fav), end='')
#     print()

office = {}
steps = {(1, 1): 0}
# BFS
curr = (1,1)
explored = []
Q = [curr]
while Q:
    node = Q.pop(0)
    if node not in explored:
        print(node)
        if steps[node] == 50:
            print(len(steps))
            break
        explored.append(node)
        neighbors = []
        if walloropen(node[0], node[1] + 1, fav) == ".":
            neighbors.append((node[0], node[1] + 1))
        if walloropen(node[0] + 1, node[1], fav) == ".":
            neighbors.append((node[0] + 1, node[1]))
        if node[1] - 1 >= 0:
            if walloropen(node[0], node[1] - 1, fav) == ".":
                neighbors.append((node[0], node[1] - 1))
        if node[0] - 1 >= 0:
            if walloropen(node[0] - 1, node[1], fav) == ".":
                neighbors.append((node[0] - 1, node[1]))
    
        for neighbor in neighbors:
            steps[neighbor] = steps[node] + 1
            Q.append(neighbor)