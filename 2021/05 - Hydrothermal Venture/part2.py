import sys
import itertools

vents = dict()

with open(sys.argv[1], "r") as f:

    for line in f:
        l,r = line.rstrip().split(" -> ")
        a,b = l.split(",")
        c,d = r.split(",")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if b == d:
            if a > c:
                r = a
                l = c
            else:
                r = c
                l = a
            for i in range(l, r + 1):
                if not (i, b) in vents:
                    vents[(i, b)] = 1
                else:
                    vents[(i, b)] += 1
        elif a == c:
            if b > d:
                r = b
                l = d
            else:
                r = d
                l = b

            for i in range(l, r + 1):
                if not (a, i) in vents:
                    vents[(a, i)] = 1
                else:
                    vents[(a, i)] += 1
        elif abs(c - a) == abs(d - b):
            ls = a
            if c > a:
                le = c + 1
                li = 1
            else:
                le = c - 1
                li = -1
            rs = b
            if d > b:
                re = d + 1
                ri = 1
            else:
                re = d - 1
                ri = -1
            for (i, j) in zip(range(ls, le, li), range(rs, re, ri)):
                if not (i, j) in vents:
                    vents[(i, j)] = 1
                else:
                    vents[(i, j)] += 1   

twoplus = 0
for k in vents:
    if vents[k] >= 2:
        twoplus += 1
print(twoplus)