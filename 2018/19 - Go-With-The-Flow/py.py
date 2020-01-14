a = 0           # reg 0
b = 0           # reg 1
c = 0           # reg 2
# d = 948         # reg 3
d = 10551348    # reg 3
f = 1           # reg 5

while f <= d:
    c = 1
    while c <= d:
        b = f * c
        if b == d:
            a += f
        c += 1
    f += 1
    print(f)
print(a)

