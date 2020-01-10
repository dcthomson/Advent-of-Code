import sys
import copy
import curses
import time

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

class Node:
    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.avail = avail
        self.thedata = False
    
    def __str__(self):
        retstr = "(" + str(self.x) + ", " + str(self.y) + "): "
        retstr += str(self.used) + " / " + str(self.size)
        if self.thedata:
            retstr += " DATA"
        return retstr


def drawgrid(grid, stdscr):
    longest = 0
    for _, n in grid.items():
        l = len(str(n.used) + "/" + str(n.size))
        if l > longest:
            longest = l

    empty = None

    for _, node in grid.items():
        s = str(node.used) + "/" + str(node.size)

        for _ in range(len(s), longest):
            s = " " + s
        
        if node.used == 0:
            empty = (node.x, node.y)
            stdscr.attron(curses.color_pair(1))
        elif node.thedata:
            stdscr.attron(curses.color_pair(3))
        stdscr.addstr(node.y + 1, node.x * (longest + 1), s)
        stdscr.attroff(curses.color_pair(1))
        stdscr.attroff(curses.color_pair(3))
        stdscr.refresh()
    return empty

def mainprog(stdscr):

    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    moves = 0

    grid = {}

    with open(sys.argv[1]) as f:
        for line in f:
            if line.startswith("/dev/grid"):
                splitline = line.split()
                (_, x, y) = splitline[0].split("-")
                x = int(x.lstrip("x"))
                y = int(y.lstrip("y"))
                size = int(splitline[1].rstrip("T"))
                used = int(splitline[2].rstrip("T"))
                avail = int(splitline[3].rstrip("T"))
                grid[(x,y)] = Node(x, y, size, used, avail)

    for _, n in grid.items():
        try:
            _ = grid[(n.x, n.y - 1)]
        except:
            try:
                _ = grid[(n.x + 1, n.y)]
            except:
                n.thedata = True

    empty = drawgrid(grid, stdscr)

    while not grid[(0, 0)].thedata:

        k = stdscr.getch()
        for dir in ((curses.KEY_DOWN, "down", (empty[0], empty[1] + 1)),
                    (curses.KEY_UP, "up", (empty[0], empty[1] - 1)),
                    (curses.KEY_RIGHT, "right", (empty[0] + 1, empty[1])),
                    (curses.KEY_LEFT, "left", (empty[0] - 1, empty[1]))):
            if k == dir[0]:
                try:
                    if grid[empty].size >= grid[dir[2]].used:
                        if grid[dir[2]].thedata:
                            grid[empty].thedata = True
                            grid[dir[2]].thedata = False
                        grid[empty].used = grid[dir[2]].used
                        grid[dir[2]].used = 0
                        empty = drawgrid(grid, stdscr)
                        moves += 1

                    else:
                        stdscr.addstr(0, 0, "Can't move " + dir[1] + "not enough room                          ")
                except:
                    stdscr.addstr(0, 0, "Can't move " + dir[1] + ", " + dir[1] + " doesn't exist                                    ")
        
    return moves



def main():
    moves = curses.wrapper(mainprog)
    print(moves)

if __name__ == "__main__":
    main()