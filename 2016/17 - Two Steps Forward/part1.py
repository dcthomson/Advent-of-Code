import sys

path = ""

with open(sys.argv[1]) as f:
    path = f.readline()

# BFS
# copied from day 13
explored = []
Q = [(0, 0)]
while Q:
    node = Q.pop(0)
    if node not in explored:
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