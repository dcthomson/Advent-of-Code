import sys

def walloropen(x, y, fav):
    sum = x*x + 3*x + 2*x*y + y + y*y + fav
    s = '{0:b}'.format(sum)
    onenum = s.count('1')
    if onenum % 2:
        return "#"
    else:
        return "."

fav = int(sys.argv[1])

for y in range(0,7):
    for x in range(0,10):
        print(walloropen(x,y,fav), end='')
    print()