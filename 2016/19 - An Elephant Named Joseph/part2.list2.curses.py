import math
import curses
import time

def main(stdscr):
    curses.curs_set(0)

    elfcount = 3014387
    # elfcount = 5

    elves = []

    for i in range(1, elfcount + 1):
        elves.append(i)

    currelfindex = 0

    elfcount = len(elves)

    stdscr.addstr(0, 0, "elfcount")
    stdscr.addstr(0, 10, "currindex")
    stdscr.addstr(0, 20, "indexrem")
    stdscr.addstr(0, 30, "Getting")
    stdscr.addstr(0, 40, "Giving")
    stdscr.refresh()

    while elfcount > 1:
        # get elf across
        elfindextoremove = None
        elfindextoremove = currelfindex + math.floor(elfcount / 2)
        if elfindextoremove >= elfcount:
            elfindextoremove -= elfcount
        stdscr.addstr(1, 0, str(elfcount) + "  ")
        stdscr.addstr(1, 10, str(currelfindex) + "  ")
        stdscr.addstr(1, 20, str(elfindextoremove) + "  ")
        stdscr.addstr(1, 30, str(elves[currelfindex]) + "  ")
        stdscr.addstr(1, 40, str(elves[elfindextoremove]) + "  ")
        stdscr.refresh()
        # print("currelfindex:", currelfindex, "  elfindextoremove:", elfindextoremove)
        # print("Elf", elves[currelfindex], "takes present from", elves[elfindextoremove])
        del elves[elfindextoremove]
        elfcount -= 1
        currelfindex += 1
        if currelfindex >= elfcount:
            currelfindex = 0
    stdscr.addstr(2, 0, str(elves[0]))
    stdscr.refresh()
    time.sleep(60)
    print(elves)

curses.wrapper(main)