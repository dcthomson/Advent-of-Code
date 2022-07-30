import sys

paper = dict()
maxx = 0
maxy = 0
folds = list()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        if "," in line:
            (x, y) = line.split(",")
            x = int(x)
            y = int(y)
            paper[(x, y)] = True
        else:
            if line.startswith("fold along"):
                (_,_,data) = line.split()
                (axis, line) = data.split("=")
                folds.append([axis, int(line)])

def printpaper(paper):
    (maxx, maxy) = getdimensions(paper)
    for y in range(0, maxy + 1):
        for x in range(0, maxx + 1):
            if (x,y) in paper:
                print("#", end='')
            else:
                print(".", end="")
        print()

def getdimensions(paper):
    maxx = 0
    maxy = 0
    for k in paper:
        x = k[0]
        y = k[1]
        if y > maxy:
            maxy = y
        if x > maxx:
            maxx = x
    return (maxx, maxy)

def fold(paper, axis, line):
    (maxx, maxy) = getdimensions(paper)
    if axis == 'y':
        for y in range(line+1, maxy+1):
            for x in range(0, maxx+1):
                if (x,y) in paper:
                    paper[(x, line - (y - line))] = True
                    paper.pop((x,y))
    if axis == 'x':
        for x in range(line+1, maxx+1):
            for y in range(0, maxy+1):
                if (x,y) in paper:
                    paper[(line - (x - line), y)] = True
                    paper.pop((x,y))

fold(paper, folds[0][0], folds[0][1])

print(len(paper))