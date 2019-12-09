import sys

json = []

with open(sys.argv[1], 'r') as f:
    for line in f:
        json = list(line)

def array(json):
    total = 0
    c = json.pop(0)
    num = ""
    while c != "]":
        if c == "[":
            total += array(json)
        elif c == "{":
            total += object(json)
        elif c == '-' and num == "":
            num = "-"
        else:
            try:
                int(c)
                num += c
            except ValueError:
                if num != "" and num != "-":
                    total += int(num)
                    num = ""
        c = json.pop(0)
    if num != "" and num != "-":
        total += int(num)
    return total

def object(json):
    total = 0
    c = json.pop(0)
    num = ""
    redstr = ""
    red = False
    while c != "}":
        tmp = redstr + c
        if tmp not in "red":
            redstr = ""
        else:
            redstr = tmp
            if redstr == "red":
                red = True
        if c == "[":
            total += array(json)
        elif c == "{":
            total += object(json)
        elif c == '-' and num == "":
            num = "-"
        else:
            try:
                int(c)
                num += c
            except ValueError:
                if num != "" and num != "-":
                    total += int(num)
                    num = ""
        c = json.pop(0)
    if num != "" and num != "-":
        total += int(num)
    if red:
        return 0
    else:
        return total

total = 0

if json.pop(0) == '[':
    total += array(json)
elif json.pop(0) == '{':
    total += object(json)
print(total)