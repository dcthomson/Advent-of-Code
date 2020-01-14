a = 0   # reg 0
b = 0   # reg 1
c = 0   # reg 2
d = 0   # reg 3
# e = 0   # reg 4
f = 0   # reg 5

a = 0

# c = 123
# c = c & 456
# while c != 72:
#     c = c & 456

cs = []

c = 0
full = True
while full:
    # print("05:",a,b,c,d,f)
    f = c | 65536
    # print("06:",a,b,c,d,f)
    c = 5234604
    # print("07:",a,b,c,d,f)
    while True:
        d = f & 255
        # print("08:",a,b,c,d,f)
        c += d
        # print("09:",a,b,c,d,f)
        c = c & 16777215
        # print("10:",a,b,c,d,f)
        c *= 65899
        # print("11:",a,b,c,d,f)
        c = c & 16777215
        # print("12:",a,b,c,d,f)
        if f >= 256:
            d = 0
            # print("17:",a,b,c,d,f)
            while True:
                b = d + 1
                # print("18:",a,b,c,d,f)
                b *= 256
                # print("19:",a,b,c,d,f)
                if b > f:
                    b = 1
                    f = d
                    # print("26:",a,b,c,d,f)
                    break
                else:
                    b = 0
                    d += 1
                    # print("24:",a,b,c,d,f)
        else:
            if c not in cs:
                print(c)
                cs.append(c)
            if a == c:
                full = False
            break
