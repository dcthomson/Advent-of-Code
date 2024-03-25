import sys

gusts = ""

with open(sys.argv[1], "r") as f:

    for line in f:
        gusts = line.strip()

class Rock():

    def __init__(self, loc):
        self.loc = loc
        self.resetloc = loc

    def reset(self):
        self.loc = self.resetloc

    def setstate(self, chamber, state):
        for coord in self.loc:
            chamber[coord] = state
    
    def gethighestpoint(self):
        highest = 0
        for coord in self.loc:
            if coord[1] > highest:
                highest = coord[1]
        return highest

    def move(self, chamber, x, y):

        newloc = []
        for coord in self.loc:
            newloc.append((coord[0] + x, coord[1] + y))
        for coord in newloc:
            # print(coord)
            if coord in chamber and chamber[coord] == "landed":
                return False
            if coord[0] < 0:
                return False
            if coord[0] >= 7:
                return False
            if coord[1] == 0:
                return False

        for coord in self.loc:
            if coord in chamber and chamber[coord] == "falling":
                del chamber[coord]
        for coord in newloc:
            chamber[coord] = "falling"
        
        self.loc = newloc
        return True

def printchamber(chamber):

    maxy = 0

    for coord in chamber:
        if coord[1] > maxy:
            maxy = coord[1]
    
    for y in range(maxy, 0, -1):
        print("|", end="")
        for x in range(0, 7):
            if (x,y) in chamber:
                if chamber[(x,y)] == "falling":
                    print("@", end="")
                elif chamber[(x,y)] == "landed":
                    print("#", end="")
            else:
                print(".", end="")
        print("|")
    print("+-------+")
    print()


chamber = {}
rocks = []

rocks.append(Rock([(0,0), (1,0), (2,0), (3,0)])) # ----
rocks.append(Rock([(1,0), (0,1), (1,1), (2,1), (1,2)])) # +
rocks.append(Rock([(0,0), (1,0), (2,0), (2,1), (2,2)])) # L
rocks.append(Rock([(0,0), (0,1), (0,2), (0,3)])) # |
rocks.append(Rock([(0,0), (0,1), (1,0), (1,1)])) # #

gustindex = 0

highestpoint = 0

for i in range(0, 1000000000000):
    if not i % 1000000:
        print(i)
    rock = rocks[i % 5]

    dropheight = highestpoint + 4

    rock.move(chamber, 2, dropheight)

    rock.setstate(chamber, "falling")

    # printchamber(chamber)

    hitbottom = False
    while not hitbottom:
        try:
            direction = gusts[gustindex]
            gustindex += 1
        except IndexError:
            direction = gusts[0]
            gustindex = 1

        if direction == ">":
            rock.move(chamber, 1, 0)
        elif direction == "<":
            rock.move(chamber, -1, 0)
        rock.setstate(chamber, "falling")
        # printchamber(chamber)
        if not rock.move(chamber, 0, -1):
            hitbottom = True
            rock.setstate(chamber, "landed")
            rockhigh = rock.gethighestpoint()
            if rockhigh > highestpoint:
                highestpoint = rockhigh
            rock.reset()
        else:
            rock.setstate(chamber, "falling")
        # printchamber(chamber)

print(str(highestpoint))