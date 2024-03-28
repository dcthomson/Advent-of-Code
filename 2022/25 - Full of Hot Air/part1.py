import sys
import math

with open(sys.argv[1], "r") as f:

    total = 0

    for line in f:
        line = line.strip()

        dec = 0
        pow = 0

        while line != "":
            line, c = line[:-1], line[-1] 
            if c == "-":
                c = -1
            elif c == "=":
                c = -2
            c = int(c)
            dec += int(c * math.pow(5, pow))
            pow += 1

        total += dec

val = 0
place = 1
snafu = ""

while True:
    val = int(math.pow(5, place))
    val *= 2
    if val > total:
        break
    place += 1

while place >= 0:
    val = int(math.pow(5, place))
    place -= 1
    nextdigit = "0"
    check1 = abs(val - abs(total))
    if check1 < abs(total):
        if total < 0:
            nextdigit = "-"
        else:
            nextdigit = "1"
    check2 = abs((val * 2) - abs(total))
    if check2 < abs(total) and check2 < check1:
        if total < 0:
            nextdigit = "="
        else:
            nextdigit = "2"
    if nextdigit == "0":
        val = 0
    elif nextdigit in "2=":
        val *= 2
    snafu += nextdigit
    if total > 0:
        total -= val
    else:
        total += val
print(snafu)