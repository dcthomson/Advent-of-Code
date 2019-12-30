import sys

# startimage = "#./#."
startimage = ".#./..#/###"
# startimage = "##../##../..##/..##"
# startimage = "#..#/..../..../#..#"
# startimage = "###.../###.../###.../...###/...#.#/...###"

class Image:

    def __init__(self, s):
        self.s = s

    def printimage(self):
        for row in self.s.split("/"):
            print(row)

    def divide(self):
        rows = self.s.split("/")
        size = 0
        if not len(rows[0]) % 2:
            size = 2
        else:
            size = 3
        squares = []
        rownum = 0
        tmplines = []
        for row in rows:
            tmplines.append([row[i:i+size] for i in range(0, len(row), size)])
            rownum += 1
            if not rownum % size:
                tmpsquares = []
                for i in range(0, len(tmplines[0])):
                    sqr = ""
                    for l in tmplines:
                        sqr += l[i]
                        sqr += "/"
                    sqr = sqr.rstrip("/")
                    tmpsquares.append(sqr)
                tmplines = []
                squares.append(tmpsquares)

        return squares
    
    # def combine(self, squares):


    def getnumon(self):
        return self.s.count("#")

    def flipandrotate(self):
        # returns list of all possible (8) rotated and flipped variations of image
        
        # check if 2x2 or 3x3
        if len(self.s) != 11 and len(self.s) != 5:
            return False

        perms = []

        def _flip(s):
            rows = []
            for r in s.split("/"):
                rows.append(r)
            newrows = rows.copy()
            newrows[0] = rows[-1]
            newrows[-1] = rows[0]
            return "/".join(newrows)

        def _rotate(s):
            rows = []
            for r in s.split("/"):
                rows.append(list(r))
            newrows = []
            top = rows[0]
            bottom = rows[-1]
            left = []
            right = []
            for r in rows:
                left.append(r[0])
                right.append(r[-1])
            left.reverse()
            right.reverse()
            newrows.append(left)
            if len(rows) == 3:
                mid = []
                mid.append(bottom[1])
                mid.append(rows[1][1])
                mid.append(top[1])
                newrows.append(mid)
            newrows.append(right)

            s = ""
            for row in newrows:
                s += "".join(row)
                s += "/"
            s = s.rstrip("/")

            return s
        
        perms.append(self.s)
        perms.append(_flip(self.s))
        perms.append(_rotate(self.s))
        perms.append(_flip(_rotate(self.s)))
        perms.append(_rotate(_rotate(self.s)))
        perms.append(_flip(_rotate(_rotate(self.s))))
        perms.append(_rotate(_rotate(_rotate(self.s))))
        perms.append(_flip(_rotate(_rotate(_rotate(self.s)))))
        return perms
        
    def combine(self, a):
        self.s = ""
        for sa in a:
            for i in range(0, sa[0].count("/") + 1):
                for s in sa:
                    self.s += s.split("/")[i]
                self.s += "/"
        # print(self.s)
                       

rules = dict()

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        rule, out = line.split(" => ")
        rules[rule] = out

mainimage = Image(startimage)

# mainimage.printimage()
# print("\n")

for i in range(0, 5):
    perms = mainimage.flipandrotate()

    if perms:
        for perm in perms:
            i = Image(perm)
            # i.printimage()
            # print()

    # print(mainimage.divide())
    newsquares = []
    squares = mainimage.divide()
    for rownum in range(0, len(squares)):
        newsquares.append([])
        for i in range(0, len(squares[rownum])):
            # print(squares[rownum][i])
            img = Image(squares[rownum][i])
            for perm in img.flipandrotate():
                if perm in rules:
                    # print(perm, "=> ", end="")
                    img.s = rules[perm]
                    # print(img.s)
                    newsquares[-1].append(img.s)
                    break

    # print(newsquares)
    mainimage.combine(newsquares)

mainimage.printimage()

print(mainimage.getnumon())