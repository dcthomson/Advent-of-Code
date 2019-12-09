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
        strbool = False
        for str in strs:
            if abba(str):
                strbool = True
                break
        hypernetbool = False
        for hypernet in hypernets:
            if abba(hypernet):
                hypernetbool = True
                break

        if strbool and not hypernetbool:
            count += 1

print(count)