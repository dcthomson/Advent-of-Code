import sys
import string

l = string.ascii_lowercase

def increase(s):
    new_s = []
    continue_change = True
    for c in s[::-1].lower():
        if continue_change:
            if c == 'z':
                new_s.insert(0, 'a')
            else:
                new_s.insert(0, l[l.index(c) + 1])
                continue_change = False
        else:
            new_s.insert(0, c)

    return ''.join(new_s)

passwd = sys.argv[1]

goodpass = 0

while goodpass != 2:

    part1 = False
    i = 0
    while i < len(passwd):
        try:
            if passwd[i] + passwd[i + 1] + passwd[i + 2] in string.ascii_lowercase:
                part1 = True
                break
        except IndexError:
            break
        i += 1
    if not part1:
        passwd = increase(passwd)
        continue

    part2 = True
    for c in "iol":
        if c in passwd:
            part2 = False
    if not part2:
        passwd = increase(passwd)
        continue

    part3 = False
    i = 0
    doubles = list()
    while i < len(passwd):
        try:
            if passwd[i] == passwd[i + 1]:
                if i - 1 not in doubles:
                    doubles.append(i)
        except IndexError:
            break
        i += 1
    if len(doubles) >= 2:
        part3 = True
    if not part3:
        passwd = increase(passwd)
        continue

    goodpass += 1
    if goodpass == 2:
        break
    passwd = increase(passwd)
print(passwd)