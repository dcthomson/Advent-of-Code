import sys

def comparepackets(p1, p2):

    while p1 != "" and p2 != "":
        if p1.startswith(","):
            p1 = p1[1:]
        if p2.startswith(","):
            p2 = p2[1:]
        if p1.startswith("["):
            if p2.startswith("["):
                # both arrays
                # print("both arrays")
                p1 = p1[1:]
                idx = None
                n = idx = 0
                for c in p1:
                    if c == "[":
                        n += 1
                    elif c == "]":
                        if n == 0:
                            break
                        n -= 1
                    idx += 1
                # print(str(idx))
                p1 = p1[:idx] + p1[idx + 1:]
                p2 = p2[1:]
                n = idx = 0
                for c in p2:
                    if c == "[":
                        n += 1
                    elif c == "]":
                        if n == 0:
                            break
                        n -= 1
                    idx += 1
                # print(str(idx))
                p2 = p2[:idx] + p2[idx + 1:]
            else:
                # left array, right int
                num = ""
                therest = ""
                digitdone = False
                for c in p2:
                    if not digitdone and c.isdigit():
                        num += c
                    else:
                        digitdone = True
                        therest += c
                p2 = "[" + num + "]" + therest
        else:
            if p2.startswith("["):
                # left int, right array
                num = ""
                therest = ""
                digitdone = False
                for c in p1:
                    if not digitdone and c.isdigit():
                        num += c
                    else:
                        digitdone = True
                        therest += c
                p1 = "[" + num + "]" + therest

            else:
                # both ints
                lnum = ""
                ltherest = ""
                digitdone = False
                for c in p1:
                    if not digitdone and c.isdigit():
                        lnum += c
                    else:
                        digitdone = True
                        ltherest += c
                lnum = int(lnum)
                rnum = ""
                rtherest = ""
                digitdone = False
                for c in p2:
                    if not digitdone and c.isdigit():
                        rnum += c
                    else:
                        digitdone = True
                        rtherest += c
                rnum = int(rnum)
                
                if lnum < rnum:
                    return True
                elif lnum > rnum:
                    return False
                else:
                    p1 = ltherest
                    p2 = rtherest
    if p1 == "":
        # print("Left side ran out")
        return True
    elif p2 == "":
        # print("Right side ran out")
        return False

with open(sys.argv[1], "r") as f:

    p1 = p2 = False

    pairnum = 1
    sum = 0

    for line in f:
        line = line.strip()

        if line == "":
            pairnum += 1
            p1 = p2 = False
        elif not p1:
            p1 = line
        elif not p2:
            p2 = line
            if comparepackets(p1, p2):
                sum += pairnum
    print(sum)