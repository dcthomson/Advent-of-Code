import sys

def abba(str):
    i = 0
    while i <= len(str):
        try:
            if str[i] == str[i + 3]:
                if str[i + 1] == str[i + 2]:
                    if str[i] != str[i + 1]:
                        return True
        except IndexError:
            break
        i += 1
    return False

def aba(strs):
    retlist = []
    for str in strs:
        i = 0
        while i <= len(str):
            try:
                if str[i] == str[i + 2]:
                    if str[i] != str[i + 1]:
                        retlist.append(str[i:i + 3])
            except IndexError:
                break
            i += 1
    return retlist

def bab(strs, abas):
    for abastr in abas:
        for str in aba(strs):
            if abastr[0] == str[1] and abastr[1] == str[0]:
                return True
    return False
count = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        hypernets = []
        strs = []
        tmpstr = ""
        hypernet = False
        for c in line:
            if c == '[':
                strs.append(tmpstr)
                tmpstr = ""
                hypernet = True
            elif c == ']':
                hypernets.append(tmpstr)
                tmpstr = ""
                hypernet = False
            else:
                tmpstr += c
        if tmpstr != "":
            if hypernet:
                hypernets.append(tmpstr)
            else:
                strs.append(tmpstr)

        if bab(hypernets, aba(strs)):
            count += 1

print(count)