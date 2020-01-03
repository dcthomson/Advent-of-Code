import time

a = 12
b = 11
while True:
    d = a
    a = 0
    while True:
        c = b
        while True:
            a += 1
            c -= 1
            # print("a:", a, "b:", b, "c:", c, "d:", d)
            if c == 0:
                break
        d -= 1
        if d == 0:
            break
    b -= 1
    c = b
    d = c
    while True:
        d -= 1
        c += 1
        if d == 0:
            break
    print("a:", a, "b:", b, "c:", c, "d:", d)
    if c == 0:
        break
c = 89
while True:
    d = 90
    while True:
        a += 1
        d -= 1
        if d == 0:
            break
    c -= 1
    if c == 0:
        break
    print("a:", a, "b:", b, "c:", c, "d:", d)
print("a:", a, "b:", b, "c:", c, "d:", d)