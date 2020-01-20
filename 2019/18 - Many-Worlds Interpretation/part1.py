import sys
import string

maze = {}
door = {}
key = {}
current = None

with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        x = 0
        for c in line:
            maze[(x, y)] = c
            if c in string.ascii_lowercase:
                key[(x, y)] = c
            elif c in string.ascii_uppercase:
                door[(x,y)] = c
            elif c == "@":
                current = (x, y)
            x += 1
        y += 1

print(key)
print(door)
print(maze)