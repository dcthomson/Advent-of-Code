b = 107900
c = 124900
g = True
while True:
    f = 1
    d = 2
    while d != b:
        e = 2
        while e != b:
            if d * e == b:
                f = 0
            e += 1
        print("b:", b,"  c:", c,"  d:", d,"  e:", e,"  f:", f,"  g:", g)
        d += 1
    if f == 0:
        if h is None:
            h = 0
        h += 1
    if b == c:
        print(h)
        exit()
    b += 17