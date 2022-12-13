import sys

def printpixel(cycle, reg):
    
    pos = cycle % 40
    if not pos:
        print()
    if pos >= reg - 1 and pos <= reg + 1:
        print("#", end="")
    else:
        print(".", end="")
    #print(" ", cycle, pos, reg)

with open(sys.argv[1], "r") as f:

    reg = 1
    signalstrength = 0
    cycle = 0

    for line in f:
        line = line.strip()

        if line == "noop":
            printpixel(cycle, reg)
            cycle += 1

        elif line.startswith("addx"):
            n = line.split()[1]
            printpixel(cycle, reg)
            cycle += 1
            #reg += int(n)
            printpixel(cycle, reg)
            cycle += 1
            reg += int(n)