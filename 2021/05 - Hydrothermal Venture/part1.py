import sys

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
                j = c
                c = a
                a = j
            for i in range(a, c + 1):
                if not (i, b) in vents:
                    vents[(i, b)] = 1
                else:
                    vents[(i, b)] += 1
        elif a == c:
            if b > d:
                j = d
                d = b
                b = j
            for i in range(b, d + 1):
                if not (a, i) in vents:
                    vents[(a, i)] = 1
                else:
                    vents[(a, i)] += 1

twoplus = 0
for k in vents:
    if vents[k] >= 2:
        twoplus += 1
print(twoplus)