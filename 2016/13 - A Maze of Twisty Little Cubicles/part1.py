import sys
import curses
import time

lastx = 7
lasty = 4

def walloropen(x, y, fav):
    sum = x*x + 3*x + 2*x*y + y + y*y + fav
    s = '{0:b}'.format(sum)
    onenum = s.count('1')
    if onenum % 2:
        return "#"
    else:
        return "."

with open(sys.argv[1]) as f:
    line = f.readline()
    (fav, lastx, lasty) = line.rstrip().split()
fav = int(fav)
lastx = int(lastx)
lasty = int(lasty)

# for y in range(0,45):
#     for x in range(0,37):
#         print(walloropen(x,y,fav), end='')
#     print()


def main(stdscr):
    curses.curs_set(0)
    office = {}
    steps = {(1, 1): 0}
    # BFS
    curr = (1,1)
    explored = []
    Q = [curr]
    while Q:
        node = Q.pop(0)
        if node not in explored:
            time.sleep(0.1)
            # stdscr.addstr(node[1], node[0], walloropen(node[0], node[1], fav))
            # stdscr.refresh()
            # print(node)
            if lastx == node[0] and lasty == node[1]:
                # print(steps[node])
                stdscr.addstr(node[1], node[0], "F")
                stdscr.refresh()
                largesty = 0
                for k in steps:
                    if k[1] > largesty:
                        largesty = k[1]
                stdscr.addstr(largesty + 1, 0, "steps: " + str(steps[node]))
                stdscr.refresh()
                time.sleep(10)
                break
            explored.append(node)
            neighbors = []
            l = walloropen(node[0] - 1, node[1], fav)
            r = walloropen(node[0] + 1, node[1], fav)
            u = walloropen(node[0], node[1] - 1, fav)
            d = walloropen(node[0], node[1] + 1, fav)

            stdscr.addstr(node[1], node[0] + 1, r)
            stdscr.refresh()
            stdscr.addstr(node[1] + 1, node[0], d)
            stdscr.refresh()
            if d == ".":
                neighbors.append((node[0], node[1] + 1))
            if r == ".":
                neighbors.append((node[0] + 1, node[1]))
            if node[1] - 1 >= 0:
                stdscr.addstr(node[1] - 1, node[0], u)
                stdscr.refresh()
                if u == ".":
                    neighbors.append((node[0], node[1] - 1))
            if node[0] - 1 >= 0:
                stdscr.addstr(node[1], node[0] - 1, l)
                stdscr.refresh()
                if l == ".":
                    neighbors.append((node[0] - 1, node[1]))
        
            for neighbor in neighbors:
                steps[neighbor] = steps[node] + 1
                Q.append(neighbor)

curses.wrapper(main)