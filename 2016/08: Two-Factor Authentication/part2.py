import sys

displayx = 50
displayy = 6

def validpixel(coord):
    if 0 <= coord[0] < displayx:
        if 0 <= coord[1] < displayy:
            return True
    return False

def rotate(screen, dir, rowcol):
    if dir == 'row':
        wraptmp = screen[(displayx - 1, rowcol)]
        for i in range(displayx - 1, 0, -1):
            screen[(i, rowcol)] = screen[(i - 1, rowcol)]
        screen[(0, rowcol)] = wraptmp
    elif dir == 'column':
        wraptmp = screen[(rowcol, displayy - 1)]
        for i in range(displayy - 1, 0, -1):
            screen[(rowcol, i)] = screen[(rowcol, i - 1)]
        screen[(rowcol, 0)] = wraptmp
    return screen

screen = dict()
for y in range(0, displayy):
    for x in range(0, displayx):
        screen[(x, y)] = False

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith("rect"):
            (sizex, sizey) = line.split()[1].split('x')
            for x in range(0, int(sizex)):
                for y in range(0, int(sizey)):
                    if validpixel((x, y)):
                        screen[(x, y)] = True
        elif line.startswith("rotate"):
            (_, dir, rowcol, _, amount) = line.split()
            for i in range(int(amount)):
                screen = rotate(screen, dir, int(rowcol.split("=")[1]))


for y in range(0, displayy):
    for x in range(0, displayx):
        if screen[(x, y)]:
            print("#", end="")
        else:
            print(" ", end="")
    print()